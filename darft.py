
from flask import Flask


app = Flask(__name__)


@app.route('/')
def main_page():
    return "<p><strong>Миссия Колонизация Марса</strong></p>"


@app.route("/index")
def index():
    return "<p><strong>И на Марсе будут яблони цвести!</strong></p>"


@app.route("/promotion")
def promotion():
    return """
    <b>Человечество вырастает из детства.</b>
    <b>Человечеству мала одна планета.</b>
    <b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
    <b>И начнем с Марса!</b>
    <b>Присоединяйся!<
    """


app.run(port='8080', host='0.0.0.0', debug=True)