from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home(name=None):
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
