from flask import Flask ,render_template, requests

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)