# Flask クラス を import する
from flask import Flask

# Flask クラス を インスタンス 化 する
app = Flask(__name__)


# URL と 実行 する 関数 をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!"


@app.get("/hello")
def hello():
    return "Hello World!"


@app.get("/helloppl/<name>")
def helloppl(name):
    return f"Hello, {name}!"
