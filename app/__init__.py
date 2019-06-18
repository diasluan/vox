# -*- coding: utf-8 -*-
from flask import (Flask, g, render_template, flash, redirect, url_for, abort, jsonify, request, session)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

if __name__ == "__main__":
    app.run()
