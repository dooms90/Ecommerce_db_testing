import pytest
from database import get_connection, close_connection

@pytest.fixture
def db():
    # SETUP - runs before every test
    connection = get_connection()
    cursor = connection.cursor()
    
    # Clean up test data before each test
    cursor.execute("DELETE FROM reviews WHERE customer_id = 1 AND product_id = 1")
    cursor.execute("DELETE FROM payments WHERE order_id = 1")
    cursor.execute("DELETE FROM orders WHERE customer_id = 1 AND product_id = 69 AND quantity = 2")
    cursor.execute("DELETE FROM customers WHERE email = 'test@gmail.com'")
    cursor.execute("DELETE FROM products WHERE name = 'Test Product'")
    connection.commit()
    
    # Give connection and cursor to test
    yield connection, cursor
    
    # TEARDOWN - runs after every test automatically
    cursor.execute("DELETE FROM reviews WHERE customer_id = 1 AND product_id = 1")
    cursor.execute("DELETE FROM payments WHERE order_id = 1")
    cursor.execute("DELETE FROM orders WHERE customer_id = 1 AND product_id = 69 AND quantity = 2")
    cursor.execute("DELETE FROM customers WHERE email = 'test@gmail.com'")
    cursor.execute("DELETE FROM products WHERE name = 'Test Product'")
    connection.commit()
    close_connection(connection, cursor)