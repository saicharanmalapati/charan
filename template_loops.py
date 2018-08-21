from flask import Flask, render_template
app = Flask("__name__")


@app.route("/")
def index():
    names = ["charan", "srinivas", "bharath"]
    return render_template("loops.html", names=names)

if __name__ == '__main__':
    app.run()
