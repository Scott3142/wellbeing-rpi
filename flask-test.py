from flask import Flask, flash, redirect, render_template, request, session, abort
import random

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/run_program">Click here to start the game!</a>'

@app.route("/run_program/<string:name>/")
def run_program(name):
    
    #insert function here
    score = random.randint(0,11)
    
    string_firstPart = "You scored " + str(score) + ".<br><br>"
    string_secondPart = '<a href="/">Click here to replay!</a>'
    string_full = string_firstPart + string_secondPart
    
    return render_template('main.html',name=name)

@app.route("/leaderboard")
def members():
    return "Members"

if __name__ == "__main__":
    app.run()