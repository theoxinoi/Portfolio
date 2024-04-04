from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    return render_template("index.html")

@app.route("/dev")
def sobre_mim():
    return render_template("Sobremim.html")

app.run(debug = True, port = 4999)


