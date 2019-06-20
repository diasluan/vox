from app import app
from flask import (render_template, redirect, url_for)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

light_status = {16:True, 19:True, 20:True, 21:True}

@app.route("/")
def index():
    return render_template('room.html', light_status=light_status)

@app.route("/lights/<status>/<int:id>")
def lights(status, id):
    if status == "on":
        GPIO.output(id, True)
        light_status[id] = True
    elif status == "off":
        GPIO.output(id, False)
        light_status[id] = False
    return redirect(url_for('index'))
