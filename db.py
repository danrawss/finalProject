import sqlite3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to the database
DATABASE_URL = os.getenv("DATABASE_URL")
db_path = DATABASE_URL.replace("sqlite:///", "")
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Create tables
# Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 10000.00
)
''')


# Unique index for username
cursor.execute('''
CREATE UNIQUE INDEX IF NOT EXISTS username ON users (username)
''')


# Products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(255),
    product_price DECIMAL(10, 2),
    image_url TEXT,
    category VARCHAR(255),
    brand VARCHAR(255)
)
''')


# Shopping cart table
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


# Wishlist table
cursor.execute('''
CREATE TABLE IF NOT EXISTS wishlist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
''')


# Purchases table
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


# Orders table 
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    full_name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    order_time TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
''')


# Insert data for Apple products
products = [
    ('iPhone 16 Pro', 1099, 'static/images/apple/phones/iphone_16_pro.jpg', 'Phones', 'Apple'),
    ('iPhone 16', 999, 'static/images/apple/phones/iphone_16.jpg', 'Phones', 'Apple'),
    ('iPhone 15 Pro', 999, 'static/images/apple/phones/iphone_15_pro.jpg', 'Phones', 'Apple'),
    ('iPhone 15', 799, 'static/images/apple/phones/iphone_15.jpg', 'Phones', 'Apple'),
    ('iPhone 14 Plus', 699, 'static/images/apple/phones/iphone_14_plus.jpg', 'Phones', 'Apple'),
    ('iPhone 14', 699, 'static/images/apple/phones/iphone_14.jpg', 'Phones', 'Apple'),
    ('iPhone 13', 599, 'static/images/apple/phones/iphone_13.jpg', 'Phones', 'Apple'),
    ('AirPods Max', 549, 'static/images/apple/headphones/airpods_max.jpg', 'Headphones', 'Apple'),
    ('AirPods Pro', 249, 'static/images/apple/headphones/airpods_pro.jpg', 'Headphones', 'Apple'),
    ('AirPods 4', 169, 'static/images/apple/headphones/airpods_4.jpg', 'Headphones', 'Apple'),
    ('AirPods 3', 149, 'static/images/apple/headphones/airpods_3.jpg', 'Headphones', 'Apple'),
    ('MacBook Pro 16', 2399, 'static/images/apple/computers/macbook_pro_16.jpg', 'Computers', 'Apple'),
    ('MacBook Pro 14', 1999, 'static/images/apple/computers/macbook_pro_14.jpg', 'Computers', 'Apple'),
    ('MacBook Air 15', 1299, 'static/images/apple/computers/macbook_air_15.jpg', 'Computers', 'Apple'),
    ('MacBook Air 13', 1099, 'static/images/apple/computers/macbook_air_13.jpg', 'Computers', 'Apple'),
    ('iPad Pro 13', 799, 'static/images/apple/tablets/ipad_pro_13.jpg', 'Tablets', 'Apple'),
    ('iPad Air 11', 599, 'static/images/apple/tablets/ipad_air_11.jpg', 'Tablets', 'Apple'),
    ('iPad 10', 449, 'static/images/apple/tablets/ipad_10.jpg', 'Tablets', 'Apple'),
    ('iPad 9', 329, 'static/images/apple/tablets/ipad_9.jpg', 'Tablets', 'Apple'),
    ('iPad Mini 7', 499, 'static/images/apple/tablets/ipad_mini_7.jpg', 'Tablets', 'Apple'),
    ('Apple Watch Series 10', 499, 'static/images/apple/smartwatches/apple_watch_series_10.jpg', 'Smartwatches', 'Apple'),
    ('Apple Watch Series 9', 449, 'static/images/apple/smartwatches/apple_watch_series_9.jpg', 'Smartwatches', 'Apple'),
    ('Apple Watch Ultra 2', 799, 'static/images/apple/smartwatches/apple_watch_ultra_2.jpg', 'Smartwatches', 'Apple'),
    ('Apple Watch SE', 249, 'static/images/apple/smartwatches/apple_watch_se.jpg', 'Smartwatches', 'Apple')
]

# Insert data for Samsung products
products += [
    ('Galaxy Z Flip5', 999, 'static/images/samsung/phones/samsung_galaxy_z_flip5.avif', 'Phones', 'Samsung'),
    ('Galaxy Z Fold5', 1919, 'static/images/samsung/phones/samsung_galaxy_z_fold5.avif', 'Phones', 'Samsung'),
    ('Galaxy S22', 619, 'static/images/samsung/phones/samsung_galaxy_s22.avif', 'Phones', 'Samsung'),
    ('Galaxy A54', 449, 'static/images/samsung/phones/samsung_galaxy_a54.avif', 'Phones', 'Samsung'),
    ('Galaxy S23 Ultra', 1619, 'static/images/samsung/phones/samsung_galaxy_s23_ultra.avif', 'Phones', 'Samsung'),
    ('Galaxy S23', 859, 'static/images/samsung/phones/samsung_galaxy_s23.avif', 'Phones', 'Samsung'),
    ('Galaxy S23+', 999, 'static/images/samsung/phones/samsung_galaxy_s23_plus.avif', 'Phones', 'Samsung'),
    ('Samsung Galaxy Buds Pro', 199, 'static/images/samsung/headphones/samsung_galaxy_buds_pro.avif', 'Headphones', 'Samsung'),
    ('Samsung Galaxy Buds Live', 169, 'static/images/samsung/headphones/samsung_galaxy_buds_live.avif', 'Headphones', 'Samsung'),
    ('Samsung Galaxy Buds+', 129, 'static/images/samsung/headphones/samsung_galaxy_buds_plus.avif', 'Headphones', 'Samsung'),
    ('Samsung Galaxy Buds', 99, 'static/images/samsung/headphones/samsung_galaxy_buds.avif', 'Headphones', 'Samsung'),
    ('Samsung Galaxy Book Pro 360', 1299, 'static/images/samsung/computers/samsung_galaxy_book_pro_360.webp', 'Computers', 'Samsung'),
    ('Samsung Galaxy Book Pro', 1099, 'static/images/samsung/computers/samsung_galaxy_book_pro.avif', 'Computers', 'Samsung'),
    ('Samsung Notebook 9 Pro', 899, 'static/images/samsung/computers/samsung_notebook_9_pro.jpg', 'Computers', 'Samsung'),
    ('Samsung Notebook 9', 749, 'static/images/samsung/computers/samsung_notebook_9.webp', 'Computers', 'Samsung'),
    ('Samsung Galaxy Tab S7', 649, 'static/images/samsung/tablets/samsung_galaxy_tab_s7.avif', 'Tablets', 'Samsung'),
    ('Samsung Galaxy Tab S6 Lite', 349, 'static/images/samsung/tablets/samsung_galaxy_tab_s6_lite.webp', 'Tablets', 'Samsung'),
    ('Samsung Galaxy Tab A7', 229, 'static/images/samsung/tablets/samsung_galaxy_tab_a7.avif', 'Tablets', 'Samsung'),
    ('Samsung Galaxy Tab Active3', 599, 'static/images/samsung/tablets/samsung_galaxy_tab_active3.webp', 'Tablets', 'Samsung'),
    ('Samsung Galaxy Tab Active Pro', 799, 'static/images/samsung/tablets/samsung_galaxy_tab_active_pro.png', 'Tablets', 'Samsung'),
    ('Samsung Galaxy Watch 4', 249, 'static/images/samsung/smartwatches/samsung_galaxy_watch_4.webp', 'Smartwatches', 'Samsung'),
    ('Samsung Galaxy Watch 4 Classic', 299, 'static/images/samsung/smartwatches/samsung_galaxy_watch_ultra.avif', 'Smartwatches', 'Samsung'),
    ('Samsung Galaxy Watch 3', 199, 'static/images/samsung/smartwatches/samsung_galaxy_watch_3.webp', 'Smartwatches', 'Samsung'),
    ('Samsung Galaxy Watch Active 2', 149, 'static/images/samsung/smartwatches/samsung_galaxy_watch_active2.avif', 'Smartwatches', 'Samsung')
]

# Insert data for Xiaomi products
products += [
    ('Xiaomi Mi 11 Pro', 699, 'static/images/xiaomi/phones/xiaomi_mi_11_pro.webp', 'Phones', 'Xiaomi'),
    ('Xiaomi Mi 11', 599, 'static/images/xiaomi/phones/xiaomi_mi_11.avif', 'Phones', 'Xiaomi'),
    ('Xiaomi Mi 10 Pro', 599, 'static/images/xiaomi/phones/xiaomi_mi_10_pro.webp', 'Phones', 'Xiaomi'),
    ('Xiaomi Mi 10', 499, 'static/images/xiaomi/phones/xiaomi_mi_10.jpg', 'Phones', 'Xiaomi'),
    ('Xiaomi Redmi Note 10 Pro', 299, 'static/images/xiaomi/phones/xiaomi_redmi_note_10_pro.webp', 'Phones', 'Xiaomi'),
    ('Xiaomi Redmi Note 10', 249, 'static/images/xiaomi/phones/xiaomi_redmi_note_10.webp', 'Phones', 'Xiaomi'),
    ('Xiaomi Poco X3', 199, 'static/images/xiaomi/phones/xiaomi_poco_x3.webp', 'Phones', 'Xiaomi'),
    ('Xiaomi Mi True Wireless Earbuds Pro', 69, 'static/images/xiaomi/headphones/xiaomi_mi_true_wireless_earbuds_pro.webp', 'Headphones', 'Xiaomi'),
    ('Xiaomi Mi True Wireless Earbuds 2', 49, 'static/images/xiaomi/headphones/xiaomi_mi_true_wireless_earbuds_2.webp', 'Headphones', 'Xiaomi'),
    ('Xiaomi Mi Wireless Earbuds', 39, 'static/images/xiaomi/headphones/xiaomi_mi_wireless_earbuds.jpeg', 'Headphones', 'Xiaomi'),
    ('Xiaomi Redmi SonicBass Wireless Earphones', 29, 'static/images/xiaomi/headphones/xiaomi_redmi_sonicbass_wireless_earphones.jpg', 'Headphones', 'Xiaomi'),
    ('Xiaomi Mi Laptop Pro 15.6', 899, 'static/images/xiaomi/computers/xiaomi_mi_laptop_pro_15_6.webp', 'Computers', 'Xiaomi'),
    ('Xiaomi RedmiBook 14', 549, 'static/images/xiaomi/computers/xiaomi_redmibook_14.jpg', 'Computers', 'Xiaomi'),
    ('Xiaomi Mi Gaming Laptop', 1299, 'static/images/xiaomi/computers/xiaomi_mi_gaming_laptop.jpg', 'Computers', 'Xiaomi'),
    ('Xiaomi Mi Notebook 15.6', 499, 'static/images/xiaomi/computers/xiaomi_mi_notebook_pro_15_6.webp', 'Computers', 'Xiaomi'),
    ('Xiaomi Mi Pad 5', 299, 'static/images/xiaomi/tablets/xiaomi_mi_pad_5.webp', 'Tablets', 'Xiaomi'),
    ('Xiaomi Mi Pad 4 Plus', 349, 'static/images/xiaomi/tablets/xiaomi_mi_pad_4_plus.avif', 'Tablets', 'Xiaomi'),
    ('Xiaomi Mi Pad 4', 249, 'static/images/xiaomi/tablets/xiaomi_mi_pad_4.webp', 'Tablets', 'Xiaomi'),
    ('Xiaomi Mi Pad 3', 199, 'static/images/xiaomi/tablets/xiaomi_mi_pad_3.avif', 'Tablets', 'Xiaomi'),
    ('Xiaomi Mi Pad 2', 149, 'static/images/xiaomi/tablets/xiaomi_mi_pad_2.avif', 'Tablets', 'Xiaomi'),
    ('Xiaomi Mi Watch Revolve', 129, 'static/images/xiaomi/smartwatches/xiaomi_mi_watch_revolve.jpg', 'Smartwatches', 'Xiaomi'),
    ('Xiaomi Mi Watch Lite', 79, 'static/images/xiaomi/smartwatches/xiaomi_mi_watch_lite.webp', 'Smartwatches', 'Xiaomi'),
    ('Xiaomi Amazfit Bip U Pro', 59, 'static/images/xiaomi/smartwatches/xiaomi_amazfit_bip_u_pro.avif', 'Smartwatches', 'Xiaomi'),
    ('Xiaomi Amazfit GTS 2', 149, 'static/images/xiaomi/smartwatches/xiaomi_amazfit_gts_2.webp', 'Smartwatches', 'Xiaomi')
]

# Insert the products into the products table
cursor.executemany('''
INSERT INTO products (product_name, product_price, image_url, category, brand)
VALUES (?, ?, ?, ?, ?)
''', products)

# Commit changes and close the connection
connection.commit()
connection.close()
