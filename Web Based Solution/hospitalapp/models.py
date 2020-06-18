# encoding:utf-8
from hospitalapp import db
import datetime


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staffname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Staff {}>'.format(self.staffname)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Customer {}>'.format(self.name)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    type = db.Column(db.String(64))
    petname = db.Column(db.String(64))
    age = db.Column(db.Integer)
    breed = db.Column(db.String(64))

    def __repr__(self):
        return '<Pet {}>'.format(self.petname)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    subject = db.Column(db.String(64))
    content = db.Column(db.String(160))
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    date = db.Column(db.Integer)

    def __repr__(self):
        return '<Message {}>'.format(self.id)


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer)
    staff_id = db.Column(db.Integer)
    content = db.Column(db.String(160))
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    date = db.Column(db.Integer)

    def __repr__(self):
        return '<Reply {}>'.format(self.id)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    pet_id = db.Column(db.Integer)
    symptom = db.Column(db.String(160))
    status = db.Column(db.String(64))
    city = db.Column(db.String(64))
    apptime=db.Column(db.DateTime,default=datetime.datetime.now())
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    date = db.Column(db.Integer)
    state = db.Column(db.String(160))
    state_two_description = db.Column(db.String(160))
    state_two_year = db.Column(db.Integer)
    state_two_month = db.Column(db.Integer)
    state_two_date = db.Column(db.Integer)
    state_three_description = db.Column(db.String(160))
    state_three_year = db.Column(db.Integer)
    state_three_month = db.Column(db.Integer)
    state_three_date = db.Column(db.Integer)

    def __repr__(self):
        return '<Appointment {}>'.format(self.id)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer)
    url = db.Column(db.String(160))
