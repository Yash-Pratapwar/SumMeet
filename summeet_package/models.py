from sqlalchemy.orm import backref
from summeet_package import db
from flask_login import UserMixin 
from datetime import datetime
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType
class users(db.Model, UserMixin):   
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    fname = db.Column(db.String(150), nullable = True)
    lname = db.Column(db.String(150), nullable = True)
    user_email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    age = db.Column(db.Integer, nullable = True)
    gender = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    advts = db.relationship('uploaded_files', backref='owner') 

class uploaded_files(db.Model, UserMixin):
    __tablename__ = 'uploaded_files'
    id  = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_fname = db.Column(db.String(150))
    meeting_name = db.Column(db.String(150))
    mailing_list = db.Column(MutableList.as_mutable(PickleType),
                                    default=[])
    meeting_agenda = db.Column(db.String(1000))
    meeting_date = db.Column(db.DateTime)
    mimetype = db.Column(db.Text, nullable = False)
    file_name = db.Column(db.Text, nullable = False)
    date_uploaded = db.Column(db.DateTime, default = datetime.utcnow)

class summarised_text(db.Model, UserMixin):
    __tablename__ = 'summarised_text'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sum_text = db.Column(db.Text, nullable = True) 
    sum_file_name = db.Column(db.Text, nullable = True) 
    