from dotenv import load_dotenv
import os
from cs50 import SQL
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import redirect, render_template, session
from functools import wraps

# Load environment variables
load_dotenv()

# Email configuration
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")
db = SQL(DATABASE_URL)


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def get_time():
    # Get the current timestamp as a string
    current_time = datetime.datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S')


def get_cart_count(user_id):
    """Get the total number of items in a user's cart."""
    cart_items = db.execute("SELECT SUM(quantity) AS total_items FROM shopping_cart WHERE user_id = ?", user_id)
    return cart_items[0]["total_items"] if cart_items[0]["total_items"] else 0


def get_wishlist_count(user_id):
    """Get the total number of items in a user's wishlist."""
    wishlist_items = db.execute("SELECT COUNT(*) AS total_items FROM wishlist WHERE user_id = ?", user_id)
    return wishlist_items[0]["total_items"] if wishlist_items[0]["total_items"] else 0


def send_email(recipient_email, subject, body):
    try:
        smtp_server = os.getenv("EMAIL_HOST")
        smtp_port = int(os.getenv("EMAIL_PORT"))
        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASSWORD")

        # Set up the MIME email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

    except Exception as e:
        raise Exception(f"Failed to send email: {e}")
    