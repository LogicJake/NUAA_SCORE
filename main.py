# -*- coding: utf-8 -*-
from Login import *
from score import *
from mail import *
import Global
import time, datetime

Global._init()

def DailyReport():
    html = LoginMain(Global.get_value('usr'),Global.get_value('pwd'))
    content = GetAllScore(html)
    SendEmail(content)

# startTime = datetime.datetime(2017, 9, 25, 20, 55, 0)
# print('Program not starting yet...')
# while datetime.datetime.now() < startTime:
#     time.sleep(60)
# print('Program now starts on %s' % datetime.datetime.now())
DailyReport()