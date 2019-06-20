from app import app
from flask import (render_template, redirect, url_for)

import RPi.GPIO as GPIO

light_status = {16:True, 19:True, 20:True, 21:True}

@app.route("/")
def index():
    return render_template('room.html', light_status=light_status)

@app.route("/lights/<status>/<id>")
def lights(status, id):
    if status == "on":
        GPIO.output(id, True)
        light_status[id] = True
    elif status == "off":
        GPIO.output(id, False)
        light_status[id] = False
    return redirect(url_for('index'))
