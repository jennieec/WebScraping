from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola TIN701 Bases de Datos!</h1>"

@app.route("/g")
def grafica():
    return render_template("grafica.html")

if __name__ == "__main__":
    app.run()