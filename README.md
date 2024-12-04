# TECHTROVE

### Description
**TECHTROVE** is a dynamic e-commerce platform offering a seamless shopping experience for tech enthusiasts. Developed with a responsive front-end using **HTML**, **CSS**, and **JavaScript**, and a secure back-end powered by **Flask** and **SQLite**.

Key features include:
- **User Authentication**: Secure registration and login processes.
- **Shopping Cart**: Users can add, update, and remove items in their shopping cart.
- **Wishlist**: Users can save products to their wishlist for easy access later.
- **Product Management**: Categorized product displays with improved browsing and navigation.
- **Data Management**: SQLite database is used for user information, products, carts, wishlists, and purchase history.

### Main Components

- **Python Files**:
  - **`app.py`**: The main application file managing routes, authentication, cart operations, wishlist, and other functionalities.
  - **`helpers.py`**: Contains helper functions for various tasks such as hashing passwords, session management, and utilities.
  - **`db.py`**: The python script to setup the database.
  - **`database.db`**: The SQLite database used to store user, product, wishlist, shopping cart, and purchase information.

- **HTML Templates**:
  - **Authentication Pages**:
    - **`login.html`**: User login page.
    - **`register.html`**: User registration page.
  - **Product Pages**:
    - **`index.html`**: Homepage showcasing available products, promotions, and categories.
    - **`apple.html`**, **`samsung.html`**, **`xiaomi.html`**: Brand-specific pages for browsing and purchasing products.
    - **`cart.html`**: Shopping cart page, displaying items users have added, allowing modifications.
    - **`wishlist.html`**: Wishlist page, showing saved products with options to add to the cart or remove.
  
- **JavaScript**:
  - **`main.js`**: Handles client-side interactions, such as adding/removing items from the cart and wishlist, and providing notifications.

- **CSS Styles**:
  - **`styles.css`**: Provides custom styles for a visually consistent user interface, including buttons, navigation, and product displays.

- **Database Schema (SQLite)**:
  - **`schema.sql`**: Defines the structure of the database:
    - **`users`**: Stores user credentials and information.
    - **`products`**: Stores all product details including brand, category, and image URLs.
    - **`shopping_cart`**: Tracks user shopping cart items.
    - **`wishlist`**: Manages items that users add to their wishlist.
    - **`purchases`**: Records user purchases after checkout.

### Running the Project
To run **TECHTROVE** locally, follow these steps:

#### Prerequisites
- **Python 3.6+** installed
- **SQLite** installed
- **Flask** framework
- A virtual environment to manage project dependencies

#### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd techtrove
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Run the Application**:
   ```bash
   flask run
- Navigate to **http://127.0.0.1:5000** in your browser.

