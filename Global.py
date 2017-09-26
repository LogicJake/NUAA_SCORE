# -*- coding: utf-8 -*-

def _init():#初始化
    global _global_dict
    _global_dict = {}
    file = open("1.ini")
    lines = file.readlines()
    _global_dict['usr'] = lines[0].replace('\n', '').strip()
    _global_dict['pwd'] = lines[1].replace('\n', '').strip()
    _global_dict['mail'] = lines[2].replace('\n', '').strip()
    _global_dict['qq'] = lines[3].replace('\n', '').strip()
    _global_dict['mailpwd'] = lines[4].replace('\n', '').strip()
    _global_dict['path'] = lines[5].replace('\n', '').strip()


def set_value(key,value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue