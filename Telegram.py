from flask import Flask, render_template
from flask import render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    url = 'templates'
    res = requests.get(url)
    data = res.json()
    print(res)
    print(data["message"])

    return f'''<img src={data["message"]}>'''


app.run(host='0.0.0.0', port=81)