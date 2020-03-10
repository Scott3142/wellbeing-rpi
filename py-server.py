from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import json
import random
#from gpiozero import LED,Button
from time import time,sleep

app = Flask(__name__)

@app.route("/")
def splash():
    return render_template('splash.html')

@app.route("/holding/")
def inprogress():
    return render_template('holding.html')

@app.route("/playing/")
def game_playing():
    
    ### Put code here ###

    current_score = str(random.randint(0,11))
    sleep(5)

    ### End code ###

    return jsonify(scores=current_score)

@app.route("/score/<scoreValue>")
def score(scoreValue):
    return render_template('score.html',scoreValue=scoreValue)

if __name__ == "__main__":
    app.run(debug=True)
