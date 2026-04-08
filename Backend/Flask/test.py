# Normal Routing
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return 'Hello World'
#
# if __name__ == '__main__':
#     app.run(debug=True)

# URL Parameter Routing
from flask import Flask
app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return f"Welcome to Flask Practicing App"

# Dynamic Routing
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

# Dynamic Routing (integer)
@app.route('/age/<int:age>')
def age(age):
    return f"Hello, you are {age} years old!"

# Multiple Dynamic Values
@app.route('/profile/<name>/<int:age>')
def profile(name , age):
    return f"Hello, {name}! You are {age} years old!"

# Main Runner
if __name__ == '__main__':
    app.run(debug=True)