from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_dict = request.form
        print(user_dict)
        email = user_dict["email"]
        password = user_dict["password"]
        
        # Add authentication logic here
        return render_template("login.html",message="Login Successful")
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        user_dict = request.form
        password = user_dict["password"]
        email = user_dict["email"]
        
        # Add registration logic here
        return redirect(url_for("login"))
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)