from flask import Flask,render_template
import requests
from werkzeug.wrappers import request

app=Flask(__name__)

@app.route("/")
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b31c02048df346b0bd193d11c1d03762"
    req = requests.get(url).json()
    cases={
        'articles': req['articles'],
        
    }
    return render_template("index.html",case=cases)
