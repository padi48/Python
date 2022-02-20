from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)
database = sqlite3.connect("feedback.db", check_same_thread=False)
db = database.cursor()

@app.route("/error")
def error(message):
    message.upper()
    return render_template("error.html", message=message)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        username = request.form.get("username")
        opinion = request.form.get("opinion")
        rating = request.form.get("ratings")
        feedback_display = request.form.get("display_fb")

        if not username:
            error("must provide username!")
        db.execute("INSERT INTO feedbacks VALUES (?, ?, ?, ?)", username, opinion, rating, feedback_display)        
        database.commit()

    return render_template("feedback.html")
