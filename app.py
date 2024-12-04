import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, get_time

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("Username cannot be blank.", 400)
        usernamecheck = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(usernamecheck) > 0:
            return apology("Username already exists. Please choose a different one.", 400)

        if not request.form.get("password") or request.form.get("password") != request.form.get("confirmation"):
            return apology("The invalid password was provided. Try again", 400)

        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username,
                   generate_password_hash(request.form.get("password"), method='pbkdf2', salt_length=16))

        return redirect("/")
    else:
        return render_template("register.html")


def get_cart_count(user_id):
    cart_items = db.execute("SELECT SUM(quantity) AS total_items FROM shopping_cart WHERE user_id = ?", user_id)
    return cart_items[0]["total_items"] if cart_items[0]["total_items"] else 0

@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    cart_count = get_cart_count(user_id)
    return render_template("index.html", cart_count=cart_count)


@app.route("/cart/add", methods=["POST"])
@login_required
def add_to_cart():
    """Add an item to the shopping cart (AJAX request)"""
    user_id = session["user_id"]
    data = request.get_json()  # Get the JSON data from the request

    if not data:
        return jsonify({"error": "No data provided"}), 400

    product_name = data.get("product_name")
    product_quantity = data.get("quantity", 1)

    # Get product price from the database
    product_price_result = db.execute("SELECT item_price FROM products WHERE item_name = ?", product_name)
    if not product_price_result:
        return jsonify({"error": "Product not found"}), 404

    product_price = float(product_price_result[0]["item_price"])

    # Check if the item is already in the cart
    existing_item = db.execute(
        "SELECT * FROM shopping_cart WHERE user_id = ? AND product_name = ?",
        user_id, product_name
    )

    if existing_item:
        # Update the quantity if the item already exists
        db.execute(
            "UPDATE shopping_cart SET quantity = quantity + ? WHERE user_id = ? AND product_name = ?",
            product_quantity, user_id, product_name
        )
    else:
        # Insert a new item into the cart
        db.execute(
            "INSERT INTO shopping_cart (user_id, product_name, product_price, quantity) VALUES (?, ?, ?, ?)",
            user_id, product_name, product_price, product_quantity
        )

    # Calculate the total items in the shopping cart for the user
    total_items = get_cart_count(user_id)

    # Return JSON response with updated cart count
    return jsonify({"message": "Item added to cart", "total_items": total_items})



@app.route("/cart/remove", methods=["POST"])
@login_required
def remove_from_cart():
    """Remove an item from the shopping cart"""
    user_id = session["user_id"]
    product_name = request.json.get("product_name")

    # Remove the item from the cart
    db.execute("DELETE FROM shopping_cart WHERE user_id = ? AND product_name = ?", user_id, product_name)

    # Calculate the total items in the shopping cart for the user
    cart_items = db.execute("SELECT SUM(quantity) AS total_items FROM shopping_cart WHERE user_id = ?", user_id)
    total_items = cart_items[0]["total_items"] if cart_items[0]["total_items"] else 0

    # Calculate the updated total price for the user
    cart_items = db.execute("SELECT product_price, quantity FROM shopping_cart WHERE user_id = ?", user_id)
    total_price = sum(float(item["product_price"]) * int(item["quantity"]) for item in cart_items)

    # Return JSON response with updated cart count and total price (ensure total_price is 0 if cart is empty)
    return jsonify({
        "message": "Item removed from cart",
        "total_items": total_items,
        "total_price": float(total_price) if total_price else 0.00
    })





@app.route("/cart")
@login_required
def view_cart():
    user_id = session["user_id"]
    cart_items = db.execute(
        "SELECT product_name, product_price, quantity FROM shopping_cart WHERE user_id = ?", user_id
    )
    
    total_price = sum(float(item["product_price"]) * int(item["quantity"]) for item in cart_items)

    return render_template("cart.html", cart_items=cart_items, total_price=total_price)


@app.route("/checkout")
@login_required
def view_checkout():
    user_id = session["user_id"]
    db.execute("DELETE FROM shopping_cart WHERE user_id = ?", user_id)
    return render_template("checkout.html")


@app.route("/apple")
@login_required
def view_apple():
    """Render the Apple products page"""
    user_id = session["user_id"]
    cart_count = get_cart_count(user_id)
    return render_template("apple.html", cart_count=cart_count)


@app.route("/samsung")
@login_required
def view_samsung():
    """Render the Samsung products page"""
    return render_template("samsung.html")


@app.route("/xiaomi")
@login_required
def view_xiaomi():
    """Render the Xiaomi products page"""
    return render_template("xiaomi.html")