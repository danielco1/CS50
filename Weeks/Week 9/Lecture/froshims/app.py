import sqlite3
from flask import Flask, render_template, request  # type: ignore

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Hockey",
]

def add_registrant(name, sport):
    with sqlite3.connect("froshims.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", (name, sport))
        conn.commit()

def get_registrants():
    with sqlite3.connect("froshims.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, sport FROM registrants")
        return cur.fetchall()


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return render_template("error.html", message="Missing name.")
    if not sport:
        return render_template("error.html", message="Missing sport.")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport.")

    
    add_registrant(name, sport)

    return render_template("success.html")

@app.route("/registrants")
def registrants():
    registrants = get_registrants()
    return render_template("registrants.html", registrants=registrants)


if __name__ == "__main__":
    app.run(debug=True)
