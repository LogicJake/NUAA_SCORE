# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

def GetAllScore(html):
    soup = BeautifulSoup(html,"html.parser")
    res = {}
    res['name'] = soup.findAll('table')[0].findAll('tr')[0].findAll('td')[1].string.strip()                        #姓名
    res['pjjd'] = soup.findAll('table')[1].findAll('tbody')[0].findAll('td')[0].string.strip()   #平均绩点
    res['bxpjjd'] = soup.findAll('table')[1].findAll('tbody')[0].findAll('td')[1].string.strip() #必修平均绩点
    s= ''.join(soup.findAll('script')[3].string)
    pattern = re.compile(r"\[(.*?)\]")
    match = re.findall(pattern,s)
    match.remove(match[0])
    courseall = []
    for mm in match:
        course = []
        course.append(mm.split(',')[5].strip("'"))
        course.append(mm.split(',')[10].strip("'"))
        course.append(mm.split(',')[11].strip("'"))
        course.append(mm.split(',')[14].strip("'"))
        courseall.append(course)
    res['score'] = courseall
    res['title'] = "每日成绩汇报"
    return covert(res)

def covert(res):
    mcontent = {}
    mcontent['title'] = res['title']
    if res['title'] == "每日成绩汇报":
        content = res['name'] + '你好！\n' + '      你的每日成绩汇报如下\n\n   各科成绩：\n\n'
        for score in res['score']:
            content = content + score[0] + '   ' + score[1] + '   ' + score[2] + '   ' + score[3] + '\n'
        content = content + "\n   绩点统计\n\n平均绩点：" + res['pjjd'] + "      必修平均绩点" + res['bxpjjd'] + '\n'
        mcontent['content'] = content
    return mcontent