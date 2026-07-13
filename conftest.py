import pytest
from database import get_connection, close_connection

@pytest.fixture
def db():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM reviews WHERE customer_id = 1 AND product_id = 1")
    cursor.execute("DELETE FROM payments WHERE order_id = 1")
    cursor.execute("DELETE FROM orders WHERE customer_id = 1 AND product_id = 69 AND quantity = 2")
    cursor.execute("DELETE FROM customers WHERE email = 'test@gmail.com'")
    cursor.execute("DELETE FROM products WHERE name = 'Test Product'")
    connection.commit()
    
    yield connection, cursor
    
    cursor.execute("DELETE FROM reviews WHERE customer_id = 1 AND product_id = 1")
    cursor.execute("DELETE FROM payments WHERE order_id = 1")
    cursor.execute("DELETE FROM orders WHERE customer_id = 1 AND product_id = 69 AND quantity = 2")
    cursor.execute("DELETE FROM customers WHERE email = 'test@gmail.com'")
    cursor.execute("DELETE FROM products WHERE name = 'Test Product'")
    connection.commit()
    close_connection(connection, cursor)