from flask import Flask, render_template, jsonify

app = Flask(__name__)

marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}
values = [marks[name] for name in marks]

@app.route("/")
def index():
    return jsonify(marks)

@app.route("/values")
def get_values():
    return jsonify(values)

if __name__ == "__main__":
    app.run(debug=True)