# Bookmark Manager API

A simple, modern Bookmark Manager built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**. This project allows users to register, log in, and manage their bookmarks securely. It features a RESTful API and a minimal web frontend for demonstration and testing.

---

## Features

- User registration and login with hashed passwords
- JWT-based authentication for secure API access
- CRUD operations for bookmarks (Create, Read, Update, Delete)
- SQLite database for easy local development
- Modern FastAPI backend with Pydantic validation
- Simple HTML+JS frontend for API interaction
- Categorization and description for bookmarks

---

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Authentication:** JWT (JSON Web Tokens), Passlib (bcrypt)
- **Database:** SQLite (default, easy to swap)
- **Frontend:** Jinja2 templates, vanilla JS, HTML/CSS
- **Other:** Uvicorn (ASGI server)

---

## Getting Started

### Prerequisites

- Python 3.10+ (see `pyproject.toml` for version)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gokudaisensei/cisogenie-bookmark.git
   cd bookmark
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or, if using [Poetry](https://python-poetry.org/):

   ```bash
   poetry install
   ```

4. **Run the application:**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the app:**
   - API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Web frontend: [http://localhost:8000/](http://localhost:8000/)

---

## Usage

### Authentication

- Register a new user at `/api/register` (POST)
- Log in at `/api/login` (POST) to receive a JWT token
- Use the JWT token as a Bearer token in the `Authorization` header for all bookmark endpoints

### Example: Register & Login

```bash
# Register
curl -X POST http://localhost:8000/api/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'

# Login
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```

The login response will include an `access_token`. Use this token for authenticated requests:

```bash
curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/bookmarks/
```

---

## API Endpoints

### Authentication

- `POST /api/register`
  Register a new user.
  **Body:** `{ "email": "user@example.com", "password": "string" }`

- `POST /api/login`
  Log in and receive a JWT token.
  **Body:** `{ "email": "user@example.com", "password": "string" }`
  **Response:** `{ "access_token": "jwt", "token_type": "bearer" }`

---

### Bookmarks (Authenticated)

All endpoints below require the `Authorization: Bearer <token>` header.

- `GET /api/bookmarks/`
  List all bookmarks for the current user.

- `POST /api/bookmarks/`
  Create a new bookmark.
  **Body:**

  ```json
  {
    "url": "https://example.com",
    "title": "Example",
    "description": "Optional description",
    "category": "Optional category"
  }
  ```

- `PUT /api/bookmarks/{bookmark_id}`
  Update a bookmark's title, description, or category.
  **Body:** (any subset)

  ```json
  {
    "title": "New Title",
    "description": "New Description",
    "category": "New Category"
  }
  ```

- `DELETE /api/bookmarks/{bookmark_id}`
  Delete a bookmark.

---

### Other

- `GET /`
  Main web page (HTML demo interface)
- `GET /health`
  Health check endpoint

---

## Project Structure

```
bookmark/
├── app/
│   ├── database.py      # SQLAlchemy setup and DB session
│   ├── main.py          # FastAPI app, routes, and startup
│   ├── models.py        # SQLAlchemy models (User, Bookmark)
│   ├── routers/
│   │   ├── auth.py      # Authentication endpoints
│   │   └── bookmark.py  # Bookmark CRUD endpoints
│   ├── schemas.py       # Pydantic schemas for validation
│   └── security.py      # JWT, password hashing, auth utils
├── static/
│   └── script.js        # Frontend JS for demo UI
├── templates/
│   └── index.html       # Demo HTML frontend
├── README.md
├── pyproject.toml
└── ...
```

---

## Dependencies

Key dependencies (see `pyproject.toml` for full list):

- fastapi
- sqlalchemy
- jinja2
- passlib[bcrypt]
- python-jose
- pydantic[email]
- uvicorn

---

## Development & Testing

- Run with `uvicorn app.main:app --reload` for auto-reload during development.
- Use the `/docs` or `/redoc` endpoints for interactive API documentation.
- Test endpoints with the provided HTML frontend or tools like `curl`/Postman.

---

## Security Notes

- Passwords are hashed using bcrypt.
- JWT tokens are used for authentication; keep your `SECRET_KEY` safe in production.
- For production, use a robust database and consider HTTPS.

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Passlib](https://passlib.readthedocs.io/)
- [python-jose](https://python-jose.readthedocs.io/)

---
