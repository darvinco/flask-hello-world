from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from -- Darvin Contreras -- in 3308!'
