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

    rows = []
    data = []
    updatelist = Download.query.all()
    
    for row in updatelist:
        rows.append(row.Version)
        rows.append(row.Val)
        data.append(rows)
        rows = []

    return jsonify({
        "data" : data
    })


@bp.route("/download_page")   # 다운로드 페이지
def download_page():

    return render_template("download.html")


@bp.route("/download")   # 다운로드 실행
def download():

    return ""


@bp.route("/test")   # 테스트 공간
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

    return ""

@bp.route("/test2")   
def test2():
    for i in range(5):
        db.session.add(Download(Version=f"fw{i}.2", Level=2, Val="xdfs"))

    return ""

