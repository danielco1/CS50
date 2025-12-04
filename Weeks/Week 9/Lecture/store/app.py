import os
import sqlite3
import secrets
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "store.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
    return render_template("books.html", books=books)


@app.route("/cart", methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []

    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(int(book_id))
        return redirect("/cart")

    with get_db_connection() as conn:
        cursor = conn.cursor()
        if session["cart"]:
            placeholders = ",".join("?" * len(session["cart"]))
            query = f"SELECT * FROM books WHERE id IN ({placeholders})"
            cursor.execute(query, session["cart"])
            books = cursor.fetchall()
        else:
            books = []

    return render_template("cart.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)
