from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    email = db.Column(db.String(60), unique=True)
    phone = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(30))
    registration_time = db.Column(db.DateTime)
    profile_image = db.Column(db.String(120))

    def __repr__(self):
        return '<Person %r>' % self.fname

    def serialize(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "registration_time": self.registration_time,
            "profile_image": self.profile_image
        }