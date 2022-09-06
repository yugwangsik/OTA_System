from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import BigInteger, Boolean
from sqlalchemy.dialects.mysql import DATETIME, BIGINT, LONGBLOB
from datetime import datetime, timedelta

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "user_info"

    Num = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id = db.Column(db.String, nullable=False)
    pw = db.Column(db.String, nullable=False)

class Download(db.Model):

    __tablename__ = "download"

    Num = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Version = db.Column(db.String, nullable=False)
    Datetime = db.Column(db.Date, nullable=False)
    Level = db.Column(db.Integer, nullable=False)
    Val = db.Column(db.String, nullable=False)