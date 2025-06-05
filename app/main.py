from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import engine
from models import Base
from routers import auth, bookmark

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Bookmark Manager API",
    description="A simple bookmark manager with JWT authentication",
    version="1.0.0",
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")

# Include routers
app.include_router(auth.router)
app.include_router(bookmark.router)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Serve the main page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Bookmark Manager API is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
