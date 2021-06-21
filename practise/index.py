from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def index():
    html = '<h1>Hello world</h1>\n' \
                     '<h3>welcome</h3>\n'
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
