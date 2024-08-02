from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def hello():
    return "<p>Fine, you say hello!!</p>"

@app.route("/param")
def get_param():
    return request.args

if __name__ == "__main__":
    app.run(debug=True)