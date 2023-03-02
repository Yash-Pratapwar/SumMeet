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
    mailing_list = db.Column(MutableList.as_mutable(PickleType),
                                    default=[])
    meeting_agenda = db.Column(db.String(1000))
    meeting_date = db.Column(db.DateTime)
    mimetype = db.Column(db.Text, nullable = False)
    name = db.Column(db.Text, nullable = False)
    date_uploaded = db.Column(db.DateTime, default = datetime.utcnow)

# class advt_approval(db.Model, UserMixin):
#     __tablename__ = 'advt_approval'
#     id = db.Column(db.Integer, primary_key = True)
#     advt_id = db.Column(db.Integer, nullable = True)
#     advt_name = db.Column(db.Text, nullable = True)
#     advt_brand = db.Column(db.Text, nullable = True)
#     owner_id = db.Column(db.Integer, nullable = True)
#     owner_name = db.Column(db.Text, nullable = True)
#     infl_id = db.Column(db.Integer, nullable = True)
#     infl_fname = db.Column(db.Text, nullable = True)
#     infl_lname = db.Column(db.Text, nullable = True)
#     infl_smh = db.Column(db.Text, nullable = True)
#     infl_email = db.Column(db.Text, nullable = True)
#     approved = db.Column(db.Integer, nullable = True, default=0)
#     filter = db.Column(db.Text, nullable = True) 