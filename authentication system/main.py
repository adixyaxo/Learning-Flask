from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_dict = request.form
        print(user_dict)
        email = user_dict["email"]
        password = user_dict["password"]
        try:
            for index,row in pd.read_csv(f"accounts\\{email}.csv").itertuples():
                    if row["email"] == email and row["password"] == password:
                        return render_template("login.html",message="Login Successful")
                    else:
                        return render_template("login.html",message="Incorrect Password")
        except FileNotFoundError:
            return render_template("login.html",message="User not found. Please register.")
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        user_dict = request.form
        password = user_dict["password"]
        email = user_dict["email"]
        username = user_dict["username"]
        print(user_dict)
        user_df = pd.DataFrame({"username":username,"email":email,"password":password},index=[0])
        user_df.to_csv(f"accounts\\{email}.csv",mode="a",header=False,index=False)
        return redirect(url_for("login")) # Redirect to login after registration
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)