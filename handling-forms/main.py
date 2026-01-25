from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #handle the form data
        with open("submissions.txt", "a") as f:
            f.write(f"Name: {request.form['name']}, Email: {request.form['email']}, Message: {request.form['message']}\n")
        return render_template("contact.html")
    else:
        return render_template("contact.html")
        
    
    

if __name__ == "__main__":
    app.run(debug=True)