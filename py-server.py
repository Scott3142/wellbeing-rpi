from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import json
import random
from gpiozero import LED,Button
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

    led1 = LED(3)
    button1 = Button(27)
    led2 = LED(21)
    button2 = Button(13)
    led3 = LED(10)
    button3 = Button(7)
    led4 = LED(15)
    button4 = Button(5)
    led5 = LED(4)
    button5 = Button(2)
    my_list = ['led1', 'led2', 'led3', 'led4', 'led5']
    
    reaction_times = []
    a = 100
    b = 75
    c = 50
    d = 25
    e = 10
    
    score = 0
    number_of_hits = 10
    
#   while True:
#       
#       led1.on()
#       button1.wait_for_press()
#       led1.off()
    
    for index in range(0,number_of_hits):
        
        sleep(random.randint(1,5))
    
        start_time = time()
    
        choice = random.choice (my_list)
    
        if choice == 'led1':
            led1.on()
            button1.wait_for_press()
            led1.off()
    
        elif choice == 'led2':
            led2.on()
            button2.wait_for_press()
            led2.off()
            
        elif choice == 'led3':
            led3.on()
            button3.wait_for_press()
            led3.off()
            
        elif choice == 'led4':
            led4.on()
            button4.wait_for_press()
            led4.off()
            
        elif choice == 'led5':
            led5.on()
            button5.wait_for_press()
            led5.off()
            
        reaction_time = time() - start_time
    
        if reaction_time <2:
            score += a
        if reaction_time >2 and reaction_time <2.5:
            score += b
        if reaction_time >2.5 and reaction_time <2.9:
            score += c
        if reaction_time >3 and reaction_time <5:
            score += d
        if reaction_time >5:
            score += e
    
#    print(score)
#    sleep (5)
#    score = 0

    current_score = score

    ### End code ###

    return jsonify(scores=current_score)

@app.route("/score/<scoreValue>")
def score(scoreValue):
    return render_template('score.html',scoreValue=scoreValue)

if __name__ == "__main__":
    app.run(debug=True)
