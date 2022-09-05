from flask.templating import render_template
from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify
import os
import subprocess
#import timer_test
import time
from models import db, User, Download
from datetime import datetime


bp = Blueprint('index', __name__, url_prefix='/OTA')

@bp.route("/main_page", methods=["GET", "POST"])  # 로그인 후 메인화면
def mainPage():
    
    return render_template("test.html")


@bp.route("/login_page", methods=["GET", "POST"])   # 로그인 화면
def loginPage():
    
    return render_template("login.html")

    
@bp.route("/login", methods=["GET", "POST"])   # 로그인 체크
def login():

    id = request.form['id']
    pw = request.form['pw']

    user_list = User.query.filter(User.id == id).first()

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


@bp.route("/signup", methods=["GET", "POST"])  # 회원가입
def signup():
    id = request.form['id']
    pw = request.form['pw']

    user_ck = User.query.filter(User.id == id).first()

    if user_ck:
        return jsonify({
                "result" : False
            })
    else:
        db.session.add(User(id=id, pw=pw))
        db.session.commit()
        return jsonify({
                "result" : True
            })

    return ""


@bp.route("/getdata", methods=["GET", "POST"])  # DB 리스트
def getdata():
    updatelist = Download.query.all()

    #db.session.add(Download(Version="fw1.2", File=b'12', Level=2, Val="xdfs"))
#bin(19)
    for i in updatelist:
        print(f'{i.Version} | {i.Level} | {i.Datetime}')
    # if user_ck:
    #     return jsonify({
    #             "result" : False
    #         })
    # else:
    #     db.session.add(User(id=id, pw=pw))
    #     db.session.commit()
    #     return jsonify({
    #             "result" : True
    #         })

    return ""


@bp.route("/test")
def test():

    # test = User.query.filter(User.id == "admin").first()
    # test1 = User.query.all()

    # if test:
    #     db.session.delete(test)

    # for i in test1:
    #     print(f'{i.Num} | {i.id}')

    # print(test.Num)

    # db.session.add(User(id="admin", pw="admin"))
    # db.session.commit()

    return render_template("download.html")
