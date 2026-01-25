from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/public', static_folder='assets')
# When setting static_url_path and static_folder,
# static files will be served from the specified folder and URL path.
# The static folder wont contain / at the start of its name but the static_url_path will contain / at the start of its name.

@app.route("/")
def index():
    return render_template("index.htm")


if __name__ == "__main__":
    app.run(debug=True) 