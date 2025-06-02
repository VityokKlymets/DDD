# 🛠️ Django REST API with PostgreSQL, Docker, JWT Auth & Swagger

This project is a Django REST Framework (DRF) application with:

- ✅ User registration and JWT login
- ✅ CRUD operations on Orders
- ✅ PostgreSQL as database
- ✅ Swagger (drf-yasg) for API docs
- ✅ Docker + Docker Compose

---

## 📦 Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

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

<img width="1512" alt="Знімок екрана 2025-06-03 о 01 28 17" src="https://github.com/user-attachments/assets/7dee435a-7cd1-47c2-b204-b1604c3d91d8" />
<img width="1512" alt="Знімок екрана 2025-06-03 о 01 29 24" src="https://github.com/user-attachments/assets/cd7f2947-5b82-48fe-8ff0-3e3e88e46ae6" />
<img width="1512" alt="Знімок екрана 2025-06-03 о 01 29 55" src="https://github.com/user-attachments/assets/639f1caa-1225-4cf2-8d86-4c1930d4822b" />
<img width="1512" alt="Знімок екрана 2025-06-03 о 01 30 08" src="https://github.com/user-attachments/assets/5dabf6b4-190b-469e-9a4f-6997c3bcbc06" />
<img width="1512" alt="Знімок екрана 2025-06-03 о 01 32 00" src="https://github.com/user-attachments/assets/d6b3d793-4bb7-456c-9edb-1c309d147552" />
<img width="1512" alt="Знімок екрана 2025-06-03 о 01 32 34" src="https://github.com/user-attachments/assets/3d632510-7967-4b73-b499-aed4eb2bd961" />
<img width="1512" alt="Знімок екрана 2025-06-03 о 01 33 10" src="https://github.com/user-attachments/assets/20b9e091-55b3-49ba-9b67-ea70a5ae5ad8" />
