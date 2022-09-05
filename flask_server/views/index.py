from flask.templating import render_template
from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify
import os
import subprocess
#import timer_test
import time
from models import db, User

#dsdasdasda

bp = Blueprint('index', __name__, url_prefix='/OTA')

@bp.route("/main_page", methods=["GET", "POST"])  # 로그인 후 메인화면
#@logging_time
def mainPage():
    
    return render_template("test.html")


@bp.route("/login_page", methods=["GET", "POST"])   # 로그인 화면
#@logging_time
def loginPage():
    
    return render_template("login.html")

    
@bp.route("/login", methods=["GET", "POST"])   # 로그인 체크
#@logging_time
def login():

    id = request.form['id']
    pw = request.form['pw']

    user_list = User.query.filter(User.id == id).first()


    #print(f'{id} | {pw}')

    if user_list:
        if pw == user_list.pw:
            print("!")
            return jsonify({
                "result" : True
            })
        else:
            print("!!!")
            return jsonify({
                "result" : False
            })

    return " "


@bp.route("/test")
def test():

    test = User.query.filter(User.id == "admin").first()
    test1 = User.query.all()

    if test:
        db.session.delete(test)

    for i in test1:
        print(f'{i.Num} | {i.id}')

    # print(test.Num)

    # db.session.add(User(id="admin", pw="admin"))
    # db.session.commit()

    return ""
