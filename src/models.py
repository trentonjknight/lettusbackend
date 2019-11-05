from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    email = db.Column(db.String(60), unique=True)
    phone = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(30))
    registration_time = db.Column(db.Integer)
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

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(60), unique= True)
    days_to_maturity = db.Column(db.Integer)
    precip_min = db.Column(db.Integer)
    precip_max = db.Column(db.Integer)
    temp_min = db.Column(db.Integer)
    temp_max = db.Column(db.Integer)
    humid_min = db.Column(db.Integer)
    humid_max = db.Column(db.Integer)
    ph_min = db.Column(db.Integer)
    ph_max = db.Column(db.Integer)
    mat_height = db.Column(db.Integer)
    edible = db.Column(db.String(20))
    description = db.Column(db.String(120))
    pairings = db.Column(db.String(120))

    def __repr__(self):
        return '<Plant %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "days_to_maturity": self.days_to_maturity,
            "precip_min": self.precip_min,
            "precip_max": self.precip_max,
            "temp_min": self.temp_min,
            "temp_max": self.temp_max,
            "humid_min": self.humid_min,
            "humid_max": self.humid_max,
            "ph_min": self.ph_min,
            "ph_max": self.ph_max,
            "mat_height": self.mat_height,
            "edible": self.edible,
            "description": self.description,
            "pairings": self.pairings

        }

