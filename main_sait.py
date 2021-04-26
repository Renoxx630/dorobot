from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.htm')


@app.route('/beze')
def beze():
    return render_template('beze.htm')


@app.route('/caramel')
def caramel():
    return render_template('caramel.htm')


@app.route('/choco')
def choco():
    return render_template('choco.htm')


@app.route('/gallery')
def gallery():
    return render_template('gallery.htm')


@app.route('/history')
def history():
    return render_template('history.htm')


@app.route('/marcipan')
def marcipan():
    return render_template('marcipan.htm')


@app.route('/marmelad')
def marmelad():
    return render_template('marmelad.htm')


@app.route('/muss')
def muss():
    return render_template('muss.htm')


@app.route('/pomadka')
def pomadka():
    return render_template('pomadka.htm')


@app.route('/science')
def science():
    return render_template('science.htm')


@app.route('/sufle')
def sufle():
    return render_template('sufle.htm')


@app.route('/vostoc')
def vostoc():
    return render_template('vostoc.htm')


@app.route('/wafly')
def wafly():
    return render_template('wafly.htm')


@app.route('/zefir')
def zefir():
    return render_template('zefir.htm')


if __name__ == "__main__":
    app.run()
