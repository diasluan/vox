from app import db

class Lights(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True)
  io_port = db.Column(db.Integer)
  room = db.Column(db.String(64))
  controller = db.Column(db.String(64))

  def __repr__(self):
    return "<Light {}>".format(self.name, self.room)
