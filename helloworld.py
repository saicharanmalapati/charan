from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/charan")
def charan():
    return "<h1>Hello Charan!</h1>"

if __name__ == '__main__':
    app.run()
