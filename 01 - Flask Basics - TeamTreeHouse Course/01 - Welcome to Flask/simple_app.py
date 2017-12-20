# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# @app.route('/<name>')
# def index(name="Michael"):
#     return f"Hello, {name}"
#
#
# @app.route("/add/<int:num1>/<int:num2>/")
# def add(num1, num2):
#     answer = num1 + num2
#     return f"{str(num1)} + {str(num2)} = {str(answer)}"
#
# app.run(debug=True, port = 8080, host= '0.0.0.0')

from flask import Flask
app = Flask(__name__)


@app.route("/multiply")
@app.route("/multiply/<num1>/<num2>/")
def multiply(num1 = 5, num2=5):
    answer = num1 * num2
    return str(answer)



