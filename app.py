from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/hello3")
def hello_world3():
    return "<h1>Hello, World3!</h1>"

@app.route("/test_fun")
def test():
    a = 5 + 6
    return "This is my first program, of flask {}".format(a)

@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "this is my input from URL {}".format(data)
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
