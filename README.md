# E-commerce Backend API

A fully functional e-commerce backend built with Django and Django REST Framework (DRF). This project supports user authentication, product management, shopping cart operations, and order checkout with stock validation.

## 🚀 Features

- 🔐 Token-based authentication (Register & Login)
- 🛍️ Product and category management (CRUD)
- 🛒 Add to cart, update quantity, and remove items
- ✅ Checkout system with real-time stock update
- 🧾 Order creation with tracking
- 🧑‍💻 Admin panel support for managing all data

## 📦 Tech Stack

- Django
- Django REST Framework
- SQLite (you can switch to PostgreSQL/MySQL)
- Token Authentication

## ⚠️ Notes

- Payment integration is **not yet implemented**
- This is a learning/demo project, but structured in a clean, extendable way


## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint             | Description           |
|--------|----------------------|-----------------------|
| POST   | `/api/token/`        | To get the jwt token  |
| POST   | `/api/toekn/refresh/`| to refresh your token |

---

### 🛍️ Products

| Method | Endpoint                | Description               |
|--------|-------------------------|---------------------------|
| GET    | `/product/product/`     | List all products         |
| POST   | `/product/product/`     | Create a product (admin)  |
| GET    | `/product/product/{id}/`| Retrieve product details  |
| PUT    | `/api/product/{id}/`    | Update product (admin)    |
| DELETE | `/api/product/{id}/`    | Delete product (admin)    |

---


### 🛒 Cart

| Method | Endpoint                          | Description                |
|--------|-----------------------------------|----------------------------|
| GET    | `/cart/cart/view_cart/`           | View user's cart           |
| POST   | `/cart/cart/add_product_to_cart/` | Add product to cart        |
| POST   | `/cart/cart/update_quantity/`     | Update quantity in cart    |
| POST   | `/cart/cart/remove_product/`      | Remove product from cart   |

---


| Method | Endpoint          | Description          |
|--------|-------------------|----------------------|
| POST   | `/order/checkout/`| Place order from cart|


## ✅ How to Run

1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Migrate DB: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Run server: `python manage.py runserver`

---

> Feel free to fork, modify and use this project as a base for your own e-commerce ideas!

