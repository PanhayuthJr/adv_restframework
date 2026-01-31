# 🛒 Final E-commerce Project (Django)

A complete E-commerce web application built with Django and Python.
This project provides a full online shopping experience, including product management, shopping cart, user authentication, REST APIs, and an admin dashboard for store management.

## 👥 Group Members

- **Thet Panhayuth** – Team Leader
- **Kong Thavrak** – Frontend Developer
- **Menrorn Virakvuth** – Backend & API Developer
- **Prum David** – Data Entry
- **Vonnvirak Khmera** – Quality Assurance (QA)

## 🚀 Features

### 👤 User Features (Frontend)
- **Product Catalog** – Browse products by category and view detailed product information
- **Shopping Cart** – Add, remove, and update product quantities
- **Wishlist** – Save favorite products for later
- **Checkout Process** – Simple and user-friendly checkout flow
- **User Authentication** – Secure registration, login, and logout

### 🛠️ Staff / Admin Dashboard
- **Admin Dashboard** – Overview of store activity
- **Product Management** – Full CRUD (Create, Read, Update, Delete) for products
- **Category Management** – Manage product categories easily

## 🧰 Tech Stack

- **Backend:** Django 5.2 (Python)
- **API:** Django Rest Framework (DRF)
- **Database:** PostgreSQL (Production), SQLite (Development)
- **Frontend:** Django Templates, HTML5, CSS3, JavaScript
- **API Documentation:** Swagger & ReDoc (drf-yasg)
- **Deployment:** Gunicorn, WhiteNoise

## 📋 Prerequisites

Make sure you have the following installed:
- Python 3.10+
- Git

## 📦 Installation Guide

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/mid-term-ecommerce.git
cd mid-term-ecommerce
```

### 2️⃣ Create a Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Configuration

Create a `.env` file in the project root (use `.env.example` as reference):

```ini
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5️⃣ Apply Database Migrations
```bash
python manage.py migrate
```

### 6️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

## 🔌 API Documentation

This project includes a RESTful API built with Django Rest Framework.

### 🔗 Base URL
`http://127.0.0.1:8000/api/v1/`

### 📌 Main Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/products/` | GET, POST | List and create products |
| `/categories/` | GET, POST | Manage product categories |
| `/cart/` | GET, POST | Shopping cart operations |
| `/wishlist/` | GET, POST | Wishlist management |
| `/orders/` | GET, POST | Create and view orders |

### 📘 Interactive API Docs
- **Swagger UI:** `/swagger/`
- **ReDoc:** `/redoc/`

## ▶️ Running the Project

Start the development server:
```bash
python manage.py runserver
```

## 🌐 Access URLs

- **Frontend:** `http://127.0.0.1:8000`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **API Docs:**
    - Swagger: `http://127.0.0.1:8000/swagger/`
    - ReDoc: `http://127.0.0.1:8000/redoc/`

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add YourFeature"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.
See the LICENSE file for more details.
