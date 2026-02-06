from rich import print
import flask
from threading import Thread
flask.__builtins__["print"]=print
app=flask.Flask(__name__)
print(__debug__)
alternative={
    "main":1732
}
@app.route("/")
def main():
    return "main path"
@app.route("/add/<path>/logic/<logic>")
def add1(path,logic):
    @app.route(f"/user/{path}")
    def meta():
        exec(logic)
print("")
app.run(host="::",port=6123,debug=True)