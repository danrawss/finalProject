import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
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
db = SQL("sqlite:///finance.db")

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

    # Forget any user_id
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

    # Forget any user_id
    session.clear()

    # Redirect user to login form
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


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]

    return render_template("index.html")


@app.route("/apple", methods=["GET", "POST"])
@login_required
def view_apple():
    if request.method == "POST":
        user_id = session["user_id"]

        product_name = request.form.get("product_name")
        product_price = db.execute("SELECT item_price FROM products WHERE item_name = ?", product_name)
        product_price = float(product_price[0]["item_price"])
        product_quantity = int(request.form.get("quantity"))

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
        db.execute("INSERT INTO purchases(user_id, product_name, product_price, quantity, date) VALUES (?, ?, ?, ?, ?)",
                user_id, product_name, product_price, product_quantity, get_time()) 

        return redirect("/apple")

    return render_template("apple.html")


@app.route("/samsung", methods=["GET", "POST"])
@login_required
def view_samsung():
    if request.method == "POST":
        user_id = session["user_id"]

        product_name = request.form.get("product_name")
        product_price = db.execute("SELECT item_price FROM products WHERE item_name = ?", product_name)
        product_price = float(product_price[0]["item_price"])
        product_quantity = int(request.form.get("quantity"))

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

        db.execute("INSERT INTO purchases(user_id, product_name, product_price, quantity, date) VALUES (?, ?, ?, ?, ?)",
            user_id, product_name, product_price, product_quantity, get_time()) 

        return redirect("/samsung")

    return render_template("samsung.html")


@app.route("/xiaomi", methods=["GET", "POST"])
@login_required
def view_xiaomi():
    if request.method == "POST":
        user_id = session["user_id"]

        product_name = request.form.get("product_name")
        product_price = db.execute("SELECT item_price FROM products WHERE item_name = ?", product_name)
        product_price = float(product_price[0]["item_price"])
        product_quantity = int(request.form.get("quantity"))

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

        db.execute("INSERT INTO purchases(user_id, product_name, product_price, quantity, date) VALUES (?, ?, ?, ?, ?)",
             user_id, product_name, product_price, product_quantity, get_time()) 
        
        return redirect("/xiaomi")

    return render_template("xiaomi.html")
    

@app.route("/cart")
def view_cart():
    user_id = session["user_id"]
    cart_items = db.execute(
        "SELECT product_name, product_price, quantity FROM shopping_cart WHERE user_id = ?",
        user_id
    )
    
    total_price = 0
    for item in cart_items:
        price = float(item["product_price"])
        quantity = int(item["quantity"])
        total_price += price * quantity

    return render_template("cart.html", cart_items=cart_items, total_price=total_price)

@app.route("/checkout")
def view_checkout():
    user_id = session["user_id"]

    db.execute("DELETE FROM shopping_cart WHERE user_id = ?", user_id)
    return render_template("checkout.html")
