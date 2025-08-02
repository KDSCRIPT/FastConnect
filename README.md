# FastConnect API 🧩
> A containerized social media backend API built with FastAPI, PostgreSQL, and SQLAlchemy. Users can sign up, authenticate via JWT, and create, update, upvote/downvote posts.

---

## 🚀 Project Overview

FastConnect is a RESTful social media API where users can:

- ✅ Sign up and log in securely using JWT authentication
- 📝 Create, read, update, and delete (CRUD) posts
- 👍 Upvote or 👎 downvote other users’ posts
- 🐳 Run the entire app using Docker or manually with virtual environments
- 🔐 Secure secrets using GitHub Secrets
- 🔁 Perform automated CI/CD using GitHub Actions
- 🧪 Test functionality using Pytest
- 🔄 Handle DB migrations via Alembic

---

## 📹 Credits

This project is built by following an excellent [Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA) by Sanjeev Thiyagarajan, hosted on [freeCodeCamp’s YouTube channel](https://www.youtube.com/@freecodecamp).  
All educational credit goes to the original creator.

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM for DB interaction
- **Alembic** – Database migration tool
- **Pydantic** – Data validation
- **Docker** – Containerization
- **Pytest** – Testing framework
- **JWT** – Authentication
- **GitHub Actions + Secrets** – CI/CD pipeline

---

## 📦 Installation & Running the Project

### ✅ Option 1: Run with Docker (Recommended)

> Make sure you have Docker and Docker Compose installed.

```bash
docker-compose up --build
````

Access the interactive API docs at:
📍 `http://localhost:8000/docs`

To shut down the containers:

```bash
docker-compose down
```

---

### 🧪 Option 2: Run Locally Without Docker

```bash
# Clone the repo
git clone https://github.com/KDSCRIPT/FastConnect.git
cd FastConnect

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with DB and secret config
cp .env.example .env

# Run Alembic migrations
alembic upgrade head

# Start the API
uvicorn app.main:app --reload
```

---

## 🔐 Authentication

* JWT tokens are used to protect all endpoints except `/signup`
* Access tokens must be included in the `Authorization` header as:
  `Bearer <token>`

---

## 🧪 Running Tests

```bash
pytest
```
---

## 📚 API Documentation

Once the server is running, go to:

* **Swagger UI**: `http://localhost:8000/docs`
* **ReDoc**: `http://localhost:8000/redoc`

---

---

## 📄 License

This project is licensed under the **MIT License**.

---
