from flask import Flask, render_template, request  # type: ignore

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    # Use request.form for POST data
    name = request.form.get("name", "Guest")
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)