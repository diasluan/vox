import os
# import RPi.GPIO as io

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'whatever'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False


  # io.setmode(io.BCM)
  # io.setup(16, io.OUT)
  # io.setup(19, io.OUT)
  # io.setup(20, io.OUT)
  # io.setup(21, io.OUT)
