from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get('https://api.npoint.io/111dd683d74ef9d3a630').json()
    return render_template("index.html",posts=posts)

@app.route('/post/<num>')
def get_post(num):
    number = int(num)
    posts = requests.get('https://api.npoint.io/111dd683d74ef9d3a630').json()
    return render_template("post.html", posts=posts, num=number)

if __name__ == "__main__":
    app.run(debug=False)
