from flask import Flask, render_template
app = Flask("__name__")


@app.route("/")
def index():
    headline = "Hello Sosio"
    return render_template("index.html", headline=headline)


@app.route("/bye")
def bye():
    headline = "Bye Sosio"
    return render_template("index.html", headline=headline)

    return render_template("")
if __name__ == '__main__':
    app.run()
