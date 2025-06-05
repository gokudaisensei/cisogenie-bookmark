from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Bookmark, User
from schemas import BookmarkCreate, BookmarkResponse, BookmarkUpdate
from security import get_current_user

router = APIRouter(prefix="/api/bookmarks", tags=["Bookmarks"])


@router.get("/", response_model=List[BookmarkResponse])
def get_bookmarks(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    """Get all bookmarks for the authenticated user."""
    bookmarks = db.query(Bookmark).filter(Bookmark.owner_id == current_user.id).all()
    return bookmarks


@router.post("/", response_model=BookmarkResponse, status_code=status.HTTP_201_CREATED)
def create_bookmark(
    bookmark: BookmarkCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new bookmark for the authenticated user."""
    db_bookmark = Bookmark(
        url=str(bookmark.url),
        title=bookmark.title,
        description=bookmark.description,
        category=bookmark.category,
        owner_id=current_user.id,
    )

    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)

    return db_bookmark


@router.put("/{bookmark_id}", response_model=BookmarkResponse)
def update_bookmark(
    bookmark_id: int,
    bookmark_update: BookmarkUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update a bookmark's title, description, or category."""
    # Get the bookmark
    db_bookmark = (
        db.query(Bookmark)
        .filter(Bookmark.id == bookmark_id, Bookmark.owner_id == current_user.id)
        .first()
    )

    if not db_bookmark:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bookmark not found"
        )

    # Update fields if provided
    update_data = bookmark_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_bookmark, field, value)

    db.commit()
    db.refresh(db_bookmark)

    return db_bookmark


@router.delete("/{bookmark_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bookmark(
    bookmark_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a bookmark."""
    # Get the bookmark
    db_bookmark = (
        db.query(Bookmark)
        .filter(Bookmark.id == bookmark_id, Bookmark.owner_id == current_user.id)
        .first()
    )

    if not db_bookmark:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bookmark not found"
        )

    db.delete(db_bookmark)
    db.commit()

    return None
