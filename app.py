from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
from sqlalchemy import Column, ForeignKey, Integer, Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy_imageattach.context import store_context


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nyjifrotlfgwbj:4d427557ea3920e6669a7fa76c058f7ab853c5e1559c430a45330ad0a17f479c@ec2-34-192-173-173.compute-1.amazonaws.com:5432/d9eg2abehv5ppe"

db = SQLAlchemy(app)
ma = Marshmallow(app)
Base = declarative_base()

heroku = Heroku(app)
CORS(app)

class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)
    picture = image_attachment('UserFoodPicture')

class UserFoodPicture(Base, Image):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship('User')
    __tablename__ = 'user_picture'


##insert code here

def __init__(self, )







if __name__ == "__main__":
    app.run(debug=True)