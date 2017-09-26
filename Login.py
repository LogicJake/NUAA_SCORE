# -*- coding: utf-8 -*-
import http.cookiejar
import urllib
from urllib.error import URLError

import os
import pytesseract
from PIL import Image, ImageEnhance
from bs4 import BeautifulSoup
import Global

def getValidCode():
    url = "http://ded.nuaa.edu.cn/mss/Account/Vcode/signinid"
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive',
               'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'}

    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)  # 自定义Opener对象
    try:
        request = urllib.request.Request(url,headers=headers)  # 构造包含headers的request
        response = opener.open(request)
        cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    except URLError as e:
        print(e)
    fhand = open('code.png','wb')
    while True:
        info = response.read(100000)
        if len(info) < 1: break
        fhand.write(info)
    return 1

def SaveCookie(usr,pwd):       #保存在cookie.txt
    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)  # 加载cookie
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    loginUrl = "http://ded.nuaa.edu.cn/mss/Account/SignIn"
    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive','Accept':'image/webp,image/apng,image/*,*/*;q=0.8'}

    #code = input("请输入验证码:")        #人工识别
    code = Distinguish()                   #tesseract识别
    data = urllib.parse.urlencode({'VCodeId': 'signinid', 'UserName':usr,'Password':pwd,'VaildCode':code,'RememberMe':'true'})
    data = data.encode('utf-8')
    try:
        request = urllib.request.Request(loginUrl,data=data,headers=headers)  # 构造包含headers的request
        response = opener.open(request)
        cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    except URLError as e:
        print(e)

def LoginWithCookie(usr):
    cookie_filename = 'cookie.txt'
    if os.path.exists(cookie_filename) == False:            #不存在cookie文件
        return 0
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)  # 加载cookie
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
    headers = {'User-Agent': user_agent,
               'Connection': 'keep-alive',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language':'zh - CN, zh;q = 0.8',
               'Cache-Control': 'max - age = 0',
               'Referer': 'http://ded.nuaa.edu.cn/netean/newpage/xsyh/deeptree.asp'}

    get_url = "http://ded.nuaa.edu.cn/mss/studentresults/show/"+usr

    try:
        get_request = urllib.request.Request(get_url, headers=headers)
        get_response = opener.open(get_request)
        # print(get_response.read().decode('utf-8'))
        return get_response
    except URLError as e:
        print(e)

def Distinguish():
    pytesseract.pytesseract.tesseract_cmd = Global.get_value('path')
    image = Image.open('code.png')
    imgry = image.convert('L')
    sharpness = ImageEnhance.Contrast(imgry)
    sharp_img = sharpness.enhance(2.0)
    text = pytesseract.image_to_string(sharp_img,lang='nuaa') #自己训练的语言字典 nuaa
    return text

def LoginMain(usr,pwd):
    num = 0
    html = LoginWithCookie(usr)
    if html == 0:
        len = 7
    else:
        soup = BeautifulSoup(html, "html.parser")
        len = soup.findAll('input').__len__()  # len大于1说明没有登陆成功，继续尝试
    if len > 1:
        while 1:
            if getValidCode() == 1:
                SaveCookie(usr, pwd)
                html = LoginWithCookie(usr)
                soup = BeautifulSoup(html, "html.parser")
                len = soup.findAll('input').__len__()  # len大于1说明没有登陆成功，继续尝试
                num += 1
                if len <= 1:
                    break
    else:
        return html


