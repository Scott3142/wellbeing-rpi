from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import random

app = Flask(__name__)

@app.route("/")
def splash():
    return render_template('splash.html')

@app.route("/play/")
def play():
    return render_template('play.html')

@app.route("/wait/")
def wait():
    from time import sleep
    sleep(15)
    return jsonify("We are waiting...")

@app.route("/score/")
def score():
        ### begin play funtion ###
        scores = str(random.randint(0,11))
        ### end play function
        
        return render_template('score.html',scoreValue=scores)

if __name__ == "__main__":
    app.run()
