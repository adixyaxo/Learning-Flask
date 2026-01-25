from flask import Flask, render_template, request

app = Flask(__name__)

# In the url route we want to pass the variables like 
# http://127.0.0.1:5000/?name=jack&tokens=89#/
# for this we use the request.args.get('variable_name')

@app.route("/")
def index():
    name = "Aditya"
    tokens = '1000'
    print(request.args)
    if 'name' in request.args.keys():
        name = request.args['name']
    if 'tokens' in request.args.keys():
        tokens = request.args['tokens']
    return render_template("index.html", name=name, tokens=tokens)

if __name__ == "__main__":
    app.run(debug=True)