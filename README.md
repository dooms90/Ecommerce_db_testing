# 🛒 E-Commerce Database Testing Framework

A complete **SQL Database Testing Project** built using **Python, MySQL and pytest**
to test an E-Commerce system database.

---

## 📌 Project Overview

This project tests the database layer of an E-Commerce system including:
- Products Management
- Customer Registration
- Order Processing
- Payment Handling
- Product Reviews

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming Language |
| MySQL | Database |
| pytest | Testing Framework |
| pytest-html | HTML Report Generation |
| mysql-connector-python | Python MySQL Connection |
| Git & GitHub | Version Control |

---

## 📁 Project Structure

ecommerce_testing/
├── myenvx/                 # Virtual Environment
├── conftest.py             # Test Fixtures & Setup
├── database.py             # MySQL Database Connection
├── test_ecommerce.py       # All Test Cases (19 Tests)
├── requirements.txt        # Project Dependencies
└── README.md               # Project Documentation


---

## 🗄️ Database Schema

### Tables:
- **products** → Stores all products
- **customers** → Stores all customers
- **orders** → Stores all orders
- **payments** → Stores all payments
- **reviews** → Stores all product reviews

---

## 🧪 Test Cases

### ✅ Positive Test Cases (12):
| Test | Description |
|---|---|
| test_add_product | Add new product |
| test_get_all_products | Fetch all products |
| test_update_product_stock | Update product stock |
| test_delete_product | Delete a product |
| test_add_customer | Add new customer |
| test_get_all_customers | Fetch all customers |
| test_place_order | Place new order |
| test_get_all_orders | Fetch all orders |
| test_add_payment | Add new payment |
| test_get_all_payments | Fetch all payments |
| test_add_review | Add product review |
| test_get_all_reviews | Fetch all reviews |

### ❌ Negative Test Cases (7):
| Test | Description |
|---|---|
| test_add_product_empty_name | Empty product name not allowed |
| test_add_product_negative_price | Negative price not allowed |
| test_add_duplicate_customer_email | Duplicate email not allowed |
| test_place_order_invalid_customer | Invalid customer not allowed |
| test_place_order_invalid_product | Invalid product not allowed |
| test_invalid_review_rating | Rating above 5 not allowed |
| test_invalid_payment_status | Invalid order id not allowed |

---
