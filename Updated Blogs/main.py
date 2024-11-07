from flask import Flask, render_template
import requests

app = Flask(__name__)
api = 'https://api.npoint.io/50f86650998e1f10dddb'

@app.route("/")
def home():
    data = requests.get(api).json()
    return render_template('index.html', posts=data)

@app.route("/about")
def get_about():
    return render_template('about.html')

@app.route("/contact")
def get_contact():
    return render_template('contact.html')

@app.route("/post/<int:id>")
def get_post(id):
    data = requests.get(api).json()
    post = next((item for item in data if item["id"] == id), None)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)
