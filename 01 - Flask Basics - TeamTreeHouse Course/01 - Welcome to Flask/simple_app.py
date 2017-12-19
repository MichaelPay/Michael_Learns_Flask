from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Michael"):
    name = request.args.get('name', name)
    return f"Hello, {name}"

app.run(debug=True, port = 8080, host= '0.0.0.0')
