from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/Python-doc")
def python():
    return render_template("Python.html")


@app.route("/docker")
def docker():
    return redirect("https://docs.docker.com/")


@app.route("/aws-doc")
def aws():
    return render_template("aws_doc.html")


@app.route("/majin")
def majin():
    return render_template("majin_buu.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
