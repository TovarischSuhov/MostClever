#!/usr/bin/env pithon
# -*- coding: utf-8 -*-
from flask import Flask
import configparser
import random
app = Flask(__name__)

config = configparser.ConfigParser()
config.read('tmp/questions.conf')
questions = []
for j in config:
  for i in config[j]:
    tmp = {}
    tmp['color'] = j
    tmp['text'] = config[j][i]
    tmp['opened'] = False
    questions.append(tmp)

random.shuffle(questions)
num = 1
for i in questions:
  i['num'] = num
  num += 1

from app import views
