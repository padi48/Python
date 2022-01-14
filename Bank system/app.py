from functools import wraps
from flask import Flask, render_template, request, session, redirect
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

database = sqlite3.connect("system.db", check_same_thread=False)
db = database.cursor()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

"""A funny meme page for errors"""
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

@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    if "username" in session:
        return render_template("index.html")
    else:
        return render_template("login.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get('username'):
            return apology("Must provide username!", 404)
        if not request.form.get('password'):
            return apology("Must provide password!", 404)
        
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get('username'))
        if len(rows) != 1 or rows[0]["password"] != request.form.get('password'):
            return apology("Invalid username or password", 404)

        session["username"] = rows[0]["username"]
        return redirect("/")

    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        if not request.form.get('username'):
            return apology("Must provide username!", 404)
        if not request.form.get('password'):
            return apology("Must provide password!", 404)
        if request.form.get('password') != request.form.get("password1"):
            return apology("Passwords must match!", 500)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get('username'))
        if len(rows) != 1:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", request.form.get('username'), request.form.get('password'))
            return redirect("login")
        return apology("username not available", 404)

    return render_template("register.html")
