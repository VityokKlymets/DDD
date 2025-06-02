# 🛠️ Django REST API with PostgreSQL, Docker, JWT Auth & Swagger

This project is a Django REST Framework (DRF) application with:

- ✅ User registration and JWT login
- ✅ CRUD operations on Orders
- ✅ PostgreSQL as database
- ✅ Swagger (drf-yasg) for API docs
- ✅ Docker + Docker Compose
- ✅ Environment variables via `.env`

---

## 📦 Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- `.env` file with your project settings

---

## 🚀 Quick Start

### 1. Clone the Project

```bash
git clone https://github.com/VityokKlymets/DDD
cd DDD
```
### 2. Copy and Configure Environment Variables

```bash
cp env_default.env .env
```

### 3. Build and Run the Project

```bash
docker-compose up --build
```
Django will be available at: http://localhost:8000

Swagger docs: http://localhost:8000/swagger/

### 🧪 Run Tests

```
docker-compose exec web python manage.py test
```
