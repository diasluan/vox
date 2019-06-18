# -*- coding: utf-8 -*-
from flask import (Flask, g, render_template, flash, redirect, url_for, abort, jsonify, request, session)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import RPi.GPIO as io
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

if __name__ == "__main__":
    io.setmode(io.BCM)
    io.setup(16, io.OUT)
    io.setup(19, io.OUT)
    io.setup(20, io.OUT)
    io.setup(21, io.OUT)
    app.run()
