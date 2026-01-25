from flask import Flask, flash, render_template

app = Flask(__name__)

app.secret_key = 'supersecretkey'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out.", "info")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)