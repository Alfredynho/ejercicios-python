
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'un hola mundo xD!'

if __name__ == '__main__':
    app.run()