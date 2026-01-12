# Here is a flask minimal app

from flask import Flask , render_template # pyright: ignore[reportMissingImports] , ren

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug = True) # DEBUG = TRUE ENABLES DEBUG MODE WITH MULTIPLE FEATURES LIKE AUTOMATIC RELOADING WHICH ARE BENIFICIAL WHILE DEVELOPING 