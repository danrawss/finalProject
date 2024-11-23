import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('database.db')

# Create a cursor object
cursor = connection.cursor()

# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name VARCHAR(255),
    item_price DECIMAL(10, 2)
)
''')

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 10000.00
)
''')

# Create unique index for username
cursor.execute('''
CREATE UNIQUE INDEX IF NOT EXISTS username ON users (username)
''')

# Create shopping_cart table
cursor.execute('''
CREATE TABLE IF NOT EXISTS shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_name TEXT,
    product_price REAL,
    quantity INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# Create purchases table
cursor.execute('''
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_name TEXT,
    product_price REAL,
    quantity INTEGER,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')

# Insert statements for Xiaomi products
products = [
    ('Xiaomi Mi 11 Pro', 699),
    ('Xiaomi Mi 11', 599),
    ('Xiaomi Mi 10 Pro', 599),
    ('Xiaomi Mi 10', 499),
    ('Xiaomi Redmi Note 10 Pro', 299),
    ('Xiaomi Redmi Note 10', 249),
    ('Xiaomi Poco X3', 199),
    ('Xiaomi Mi True Wireless Earbuds Pro', 69),
    ('Xiaomi Mi True Wireless Earbuds 2', 49),
    ('Xiaomi Mi Wireless Earbuds', 39),
    ('Xiaomi Redmi SonicBass Wireless Earphones', 29),
    ('Xiaomi Mi Laptop Pro 15.6', 899),
    ('Xiaomi Mi Laptop Air 13.3', 699),
    ('Xiaomi RedmiBook 14', 549),
    ('Xiaomi Mi Gaming Laptop', 1299),
    ('Xiaomi Mi Notebook 15.6', 499),
    ('Xiaomi Mi Pad 5', 299),
    ('Xiaomi Mi Pad 4 Plus', 349),
    ('Xiaomi Mi Pad 4', 249),
    ('Xiaomi Mi Pad 3', 199),
    ('Xiaomi Mi Pad 2', 149),
    ('Xiaomi Mi Watch Revolve', 129),
    ('Xiaomi Mi Watch Lite', 79),
    ('Xiaomi Amazfit Bip U Pro', 59),
    ('Xiaomi Amazfit GTS 2', 149)
]

# Insert statements for Samsung products
products += [
    ('Galaxy Z Flip5', 999),
    ('Galaxy Z Fold5', 1919),
    ('Galaxy S22', 619),
    ('Galaxy A54', 449),
    ('Galaxy S23 Ultra', 1619),
    ('Galaxy S23', 859),
    ('Galaxy S23+', 999),
    ('Samsung Galaxy Buds Pro', 199),
    ('Samsung Galaxy Buds Live', 169),
    ('Samsung Galaxy Buds+', 129),
    ('Samsung Galaxy Buds', 99),
    ('Samsung Galaxy Book Pro 360', 1299),
    ('Samsung Galaxy Book Pro', 1099),
    ('Samsung Galaxy Book Flex', 999),
    ('Samsung Notebook 9 Pro', 899),
    ('Samsung Notebook 9', 749),
    ('Samsung Galaxy Tab S7', 649),
    ('Samsung Galaxy Tab S6 Lite', 349),
    ('Samsung Galaxy Tab A7', 229),
    ('Samsung Galaxy Tab Active3', 599),
    ('Samsung Galaxy Tab Active Pro', 799),
    ('Samsung Galaxy Watch 4', 249),
    ('Samsung Galaxy Watch 4 Classic', 299),
    ('Samsung Galaxy Watch 3', 199),
    ('Samsung Galaxy Watch Active 2', 149)
]

# Insert statements for Apple products
products += [
    ('iPhone 16 Pro', 1099),
    ('iPhone 16', 999),
    ('iPhone 15 Pro', 999),
    ('iPhone 15', 799),
    ('iPhone 14 Plus', 699),
    ('iPhone 14', 699),
    ('iPhone 13', 599),
    ('AirPods Max', 549),
    ('AirPods Pro', 249),
    ('AirPods 4', 169),
    ('AirPods 3', 149),
    ('MacBook Pro 16', 2399),
    ('MacBook Pro 14', 1999),
    ('MacBook Air 15', 1299),
    ('MacBook Air 13', 1099),
    ('iPad Pro 13', 799),
    ('iPad Air 11', 599),
    ('iPad 10', 449),
    ('iPad 9', 329),
    ('iPad Mini 7', 499),
    ('Apple Watch Series 10', 499),
    ('Apple Watch Series 9', 449),
    ('Apple Watch Ultra 2', 799),
    ('Apple Watch SE', 249)
]

# Insert the products into the products table
cursor.executemany('''
INSERT INTO products (item_name, item_price)
VALUES (?, ?)
''', products)

# Commit changes and close the connection
connection.commit()
connection.close()
