# Final Ecommerce Project

A complete E-commerce application built with Django and Python. This project features a robust product management system, shopping cart functionality, user authentication, and a staff dashboard for managing the store.

Group Member
Thet Panhayuth (Leader)
Kong Thavrak (Frontebd)
Menrorn Virakvuth (Backend & API)
Prum David (Data Entry)
Vonnvirak Khmera (QA)

## 🚀 Features

### User Features (Frontend)
- **Product Catalog**: Browse products by category and view detailed product information.
- **Shopping Cart**: Fully functional cart to add, remove, and update item quantities.
- **Wishlist**: Save products to a wishlist for future purchase.
- **Checkout Process**: Streamlined checkout experience.
- **User Accounts**: Secure registration, login, and logout functionality.

### Staff / Admin Dashboard
- **Admin Dashboard**: Overview of store metrics.
- **Product Management**: Interface to Create, Read, Update, and Delete (CRUD) products.
- **Category Management**: Easy management of product categories.

## 🛠️ Tech Stack

- **Backend Framework**: Django 5.2 (Python)
- **API**: Django Rest Framework (DRF)
- **Database**: PostgreSQL (Production)
- **Frontend**: Django Templates, HTML5, CSS3, JavaScript
- **API Documentation**: Swagger / ReDoc (via `drf-yasg`)
- **Deployment**: Gunicorn, WhiteNoise

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

## 📦 Installation Guide

Follow these steps to set up the project locally.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/mid-term-ecommerce.git
   cd mid-term-ecommerce
   ```

2. **Create a Virtual Environment**
   It's recommended to use a virtual environment to manage dependencies.
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory. You can use `.env.example` as a reference.
   ```bash
   # Example .env content
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
  ```

5. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**
   Create an admin account to access the dashboard.
   ```bash
   python manage.py createsuperuser
   ```

## 🔌 API Documentation

The project includes a fully functional REST API built with Django Rest Framework.

### Base URL
`http://127.0.0.1:8000/api/v1/`

### Key Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/products/` | GET, POST | List and create products |
| `/categories/` | GET, POST | List and manage categories |
| `/cart/` | GET, POST | Manage user shopping cart |
| `/wishlist/` | GET, POST | Manage user wishlist |
| `/orders/` | GET, POST | Create and view orders |

### Interactive Documentation
You can explore the API using the built-in Swagger UI or ReDoc:
- **Swagger UI**: `/swagger/`
- **ReDoc**: `/redoc/`

## 🏃‍♂️ Running the Server

Start the local development server:
```bash
python manage.py runserver
```

- **Frontend**: Visit `http://127.0.0.1:8000`
- **Admin Panel**: Visit `http://127.0.0.1:8000/admin/`
- **API Docs**: Visit `http://127.0.0.1:8000/swagger/` or `http://127.0.0.1:8000/redoc/`

## 🤝 Contributing

Contributions are welcome!
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
