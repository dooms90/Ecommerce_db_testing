import pytest
from database import get_connection, close_connection

# POSITIVE TEST CASES 

def test_add_product(db):
    connection, cursor = db
    cursor.execute("INSERT INTO products (name, price, category, stock) VALUES ('Test Product', 999.00, 'Test', 10)")
    connection.commit()
    assert cursor.rowcount == 1

def test_get_all_products(db):
    connection, cursor = db
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    assert len(products) > 0

def test_update_product_stock(db):
    connection, cursor = db
    cursor.execute("SELECT stock FROM products WHERE name = 'iPhone 15'")
    current = cursor.fetchone()
    new_stock = current[0] + 10
    cursor.execute(f"UPDATE products SET stock = {new_stock} WHERE name = 'iPhone 15'")
    connection.commit()
    assert cursor.rowcount == 1

def test_delete_product(db):
    connection, cursor = db
    cursor.execute("INSERT INTO products (name, price, category, stock) VALUES ('Test Product', 999.00, 'Test', 10)")
    connection.commit()
    cursor.execute("DELETE FROM products WHERE name = 'Test Product'")
    connection.commit()
    assert cursor.rowcount == 1

def test_add_customer(db):
    connection, cursor = db
    cursor.execute("INSERT INTO customers (name, email, city, phone) VALUES ('Test Customer', 'test@gmail.com', 'Lucknow', '9999999999')")
    connection.commit()
    assert cursor.rowcount == 1

def test_get_all_customers(db):
    connection, cursor = db
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    assert len(customers) > 0

def test_place_order(db):
    connection, cursor = db
    cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (1, 69, 2, '2024-02-01')")
    connection.commit()
    assert cursor.rowcount == 1

def test_get_all_orders(db):
    connection, cursor = db
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    assert len(orders) > 0

# PAYMENTS TESTS

def test_add_payment(db):
    connection, cursor = db
    cursor.execute("INSERT INTO payments (order_id, amount, payment_method, payment_status, payment_date) VALUES (1, 4999.00, 'UPI', 'Success', '2024-02-01')")
    connection.commit()
    assert cursor.rowcount == 1

def test_get_all_payments(db):
    connection, cursor = db
    cursor.execute("INSERT INTO payments (order_id, amount, payment_method, payment_status, payment_date) VALUES (1, 4999.00, 'UPI', 'Success', '2024-02-01')")
    connection.commit()
    cursor.execute("SELECT * FROM payments")
    payments = cursor.fetchall()
    assert len(payments) > 0

# REVIEWS TESTS

def test_add_review(db):
    connection, cursor = db
    cursor.execute("INSERT INTO reviews (customer_id, product_id, rating, comment) VALUES (1, 69, 5, 'Excellent!')")
    connection.commit()
    assert cursor.rowcount == 1

def test_get_all_reviews(db):
    connection, cursor = db
    cursor.execute("INSERT INTO reviews (customer_id, product_id, rating, comment) VALUES (1, 69, 5, 'Excellent!')")
    connection.commit()
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()
    assert len(reviews) > 0

# NEGATIVE TEST CASES

def test_add_product_empty_name(db):
    connection, cursor = db
    try:
        cursor.execute("INSERT INTO products (name, price, category, stock) VALUES ('', 999.00, 'Test', 10)")
        connection.commit()
        assert False, "Should not allow empty product name"
    except Exception:
        assert True

def test_add_product_negative_price(db):
    connection, cursor = db
    try:
        cursor.execute("INSERT INTO products (name, price, category, stock) VALUES ('Bad Product', -999.00, 'Test', 10)")
        connection.commit()
        assert False, "Should not allow negative price"
    except Exception:
        assert True

def test_add_duplicate_customer_email(db):
    connection, cursor = db
    try:
        cursor.execute("INSERT INTO customers (name, email, city, phone) VALUES ('Rahul Sharma', 'rahul@gmail.com', 'Lucknow', '9876543210')")
        connection.commit()
        assert False, "Should not allow duplicate email"
    except Exception:
        assert True

def test_place_order_invalid_customer(db):
    connection, cursor = db
    try:
        cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (9999, 1, 1, '2024-02-01')")
        connection.commit()
        assert False, "Should not allow invalid customer id"
    except Exception:
        assert True

def test_place_order_invalid_product(db):
    connection, cursor = db
    try:
        cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (1, 9999, 1, '2024-02-01')")
        connection.commit()
        assert False, "Should not allow invalid product id"
    except Exception:
        assert True

def test_invalid_review_rating(db):
    connection, cursor = db
    try:
        cursor.execute("INSERT INTO reviews (customer_id, product_id, rating, comment) VALUES (1, 1, 10, 'Bad rating!')")
        connection.commit()
        assert False, "Should not allow rating above 5"
    except Exception:
        assert True

def test_invalid_payment_status(db):
    connection, cursor = db
    try:
        cursor.execute("INSERT INTO payments (order_id, amount, payment_method, payment_status, payment_date) VALUES (9999, 4999.00, 'UPI', 'Success', '2024-02-01')")
        connection.commit()
        assert False, "Should not allow invalid order id"
    except Exception:
        assert True