# E-commerce Backend API

A complete backend for an e-commerce app built with Django and DRF, supporting user auth, product & cart management, and checkout with stock validation.

Features:
- Token-based auth (register/login)
- Product and category CRUD with admin control
- Cart operations (add, update, remove)
- Order checkout with real-time stock update
- Admin panel management

APIs cover auth, products, cart, and orders with clear endpoints.

Easy to set up and extend for your own e-commerce projects.

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
- SQLite (you can switch to PostgreSQL/MySql)
- Token Authentication


## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint                 | Description           |
|--------|--------------------------|-----------------------|
| POST   | `/api/token/`            | To get the jwt token  |
| POST   | `/api/toekn/refresh/`    | to refresh your token |
| POST   | `/api/accounts/login/`   | to login              |
| POST   | `/api/accounts/register/`| to register           |

---

### 🛍️ Products

| Method | Endpoint                | Description               |
|--------|-------------------------|---------------------------|
| GET    | `/api/product/`         | List all products         |
| POST   | `/api/product/`         | Create a product (admin)  |
| GET    | `/api/product/{id}/`    | Retrieve product details  |
| PUT    | `/api/product/{id}/`    | Update product (admin)    |
| DELETE | `/api/product/{id}/`    | Delete product (admin)    |

---


### 🛒 Cart

| Method | Endpoint                         | Description                |
|--------|----------------------------------|----------------------------|
| GET    | `/api/cart/view_cart/`           | View user's cart           |
| POST   | `/api/cart/add_product_to_cart/` | Add product to cart        |
| POST   | `/api/cart/update_quantity/`     | Update quantity in cart    |
| POST   | `/api/cart/remove_product/`      | Remove product from cart   |

---


| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| POST   | `/api/order/checkout/`| Place order from cart|


## ✅ How to Run

1. Clone the repo
2. cd ecommere-backend
3. Install requirements: `pip install -r requirements.txt`
4. Migrate DB: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Run server: `python manage.py runserver`




## How to Get Stripe Secret Key and Webhook Secret

<details>
  <summary>How to get Stripe Secret Key</summary>

  1. Go to [Stripe Dashboard](https://dashboard.stripe.com/login) and log in.
  2. Navigate to **Developers** > **API keys**.
  3. Copy your **Secret Key** under Standard keys.
  4. Keep it secret and use it in your project .env file.

</details>

<details>
  <summary>How to get Stripe Webhook Signing Secret</summary>

  1. In Stripe Dashboard, go to **Developers** > **Webhooks**.
  2. Click **Add endpoint** and enter your webhook URL (e.g., `https://yourdomain.com/api/stripe/webhook/`).
  3. Select the events you want to listen to, like `checkout.session.completed`.
  4. After saving, click on the webhook and copy the **Signing Secret**.
  5. Use this secret in your project to verify incoming webhook requests.

</details>

<details>
  <summary>How to use Stripe CLI if you don't have a domain name</summary>

  1. Download and install Stripe CLI from the official site: [https://stripe.com/docs/stripe-cli](https://stripe.com/docs/stripe-cli)
  2. Login to Stripe CLI by running:
     ```
     stripe login
     ```
  3. Forward webhook events to your local server by running:
     ```
     stripe listen --forward-to localhost:8000/api/order/webhook/
     ```
  4. This will generate a webhook signing secret in the CLI output. Copy it and use it in your project settings.
   4. This will generate a webhook signing secret in the CLI output. It looks like this:
     ```
     Ready! Your webhook signing secret is whsec_XXXXXXXXXXXXXXXXXXXXXXXXXXXX
     ```
  5. Now Stripe will forward webhook events to your local machine without needing a public domain.

</details>


---

> Feel free to fork, modify and use this project as a base for your own e-commerce ideas!

