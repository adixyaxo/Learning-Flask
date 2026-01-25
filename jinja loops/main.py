from flask import Flask ,render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 90,
        "Harry": 88
    }

    return render_template("index.html", marks=marks)

if __name__ == "__main__":
    app.run(debug=True)