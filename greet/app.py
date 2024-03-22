from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    return "welcome"

@app.get('/welcome/home')
def home():
    return "welcome home"

@app.get("/welcome/back")
def back():
    return "welcome back"