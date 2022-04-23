# Flask クラス を import する
from flask import Flask, render_template, url_for, redirect

# Flask クラス を インスタンス 化 する
app = Flask(__name__)

# Endpointを表示する


# URL と 実行 する 関数 をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.get("/hello")
def hello():
    return "Hello World!"


@app.get("/setname/<name>")
def setname(name):
    return f"Hello, {name}!"


@app.route("/name/<name>")
def showname(name):
    return render_template("index.html", name=name)


@app.get("/redirectfrom")
def redirectfrom():
    return redirect(url_for("redirectto", msg="redirect complete"))


@app.get("/redirectto/<string:msg>")
def redirectto(msg):
    return msg


@app.get("/contact")
def contact():
    return render_template("contact.html")


@app.post("/contact/complete")
def contact_complete():
    return render_template("contact_complete.html")


with app.test_request_context():
    print(url_for("index"))
