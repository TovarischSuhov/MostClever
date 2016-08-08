#!/usr/bin/env python

from flask import render_template
from flask import request
from app import app
from app import questions

@app.route('/')
@app.route('/index')
def index():
    return render_template("showbase.html", opts = questions)

@app.route('/showall')
def showall():
    return render_template("showall.html", opts = questions)

@app.route('/showmsg')
def showmsg():
    num = request.args.get('id');
    questions[int(num)]['opened'] = True;
    return render_template("showmsg.html", opts = questions[int(num)])


