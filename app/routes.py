from app import app
from flask import (render_template, redirect, url_for)
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

light_status = {16:True, 19:True, 20:True, 21:True}
scene_status = {0:True}

@app.route("/")
def index():
    return render_template('room.html', light_status=light_status)

@app.route("/lights/<status>/<int:id>")
def lights(status, id):
    if status == "on":
        light_status[id] = True
        for i in light_status:
            GPIO.output(i, light_status[i])
        time.sleep(0.1)
    elif status == "off":
        light_status[id] = False
        for i in light_status:
            GPIO.output(i, light_status[i])
        time.sleep(0.1)
    return redirect(url_for('index'))

@app.route("/scene/status/<int:id>")
def scene(status, id=0):
    if status == "on":
        scene_status[id] = True
        for i in light_status:
            light_status[i] = True
            GPIO.output(i, light_status[i])
    elif status == "off":
        scene_status[id] = False
        for i in light_status:
            light_status[i] = False
            GPIO.output(i, light_status[i])
    return redirect(url_for('index'))



def reset_lights():
    for i in light_status:
        GPIO.output(i, light_status[i])


scheduler = BackgroundScheduler()
scheduler.add_job(func=reset_lights, trigger="interval", seconds=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())