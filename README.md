# template-fastapi

**A starter template for building FastAPI-based backend applications.**  
This template helps you quickly spin up a new FastAPI project with sensible defaults, project structure, and ready-to-use configurations.

## 🚀 Features

- FastAPI framework
- Built-in project structure for scalability
- Uvicorn for ASGI server
- Example endpoints included
- Docker-ready
- `.env` support for environment configuration
- Pre-configured linting and formatting (optional)

## 📁 Project Structure

```
template-fastapi/
├── app/
│ ├── main.py # Entry point
│ ├── api/ # API routes
│ ├── core/ # Core configurations
│ ├── models/ # Data models
│ └── services/ # Business logic
├── .env # Environment variables
├── requirements.txt # Dependencies
├── Dockerfile # Docker configuration
└── README.md # Project info
```

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/template-fastapi.git
cd template-fastapi
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Run the app locally

```bash
uvicorn app.main:app --reload
```

### 4. Access your app

Open your browser and navigate to: http://localhost:8000

### 5. API Documentation

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## 🐳 Docker (Optional)

To run the project using Docker:

```bash
docker build -t template-fastapi .
docker run -d -p 8000:8000 template-fastapi
```

## 🛠️ Customize This Template

When starting a new project:

Rename the project folder

Update module names, routes, and configs

Replace or extend the structure as needed
