# coding: utf-8

import datetime
import time
import re
from collections import Counter
import uuid


def _find(li, a):
    """
    二分法查找list中小于等于a的最大值的索引
    """
    l, r = 0, len(li)
    while l < r:
        m = (l + r) >> 1
        if a < li[m][0]:
            r = m
        else:
            l = m + 1
    return l - 1


def _string2intip(s):
    """
    把一个字符串形式的ip地址转化为一个int值
    """
    ss = s.split('.')
    # return sum([int(j) << (24 - int(i) * 8) for i, j in enumerate(ss)])
    return (int(ss[0]) << 24) + (int(ss[1]) << 16) + (int(ss[2]) << 8) + int(ss[3])


def _intip2string(ip):
    """
    把一个int值形式的ip地址转化为一个字符串
    """
    a = (ip & 0xff000000) >> 24
    b = (ip & 0x00ff0000) >> 16
    c = (ip & 0x0000ff00) >> 8
    d = ip & 0x000000ff
    return "%d.%d.%d.%d" % (a, b, c, d)


def fmtip(ip):
    """
    将ip地址格式化
    """
    m = re.match(".*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*", ip)
    return list(m.groups())[0] if m else "0.0.0.0"

def fmttime(t):                                                                    
    """
    把时间变成标准化时间格式字符串                                                 
    """
    if not t or not isinstance(t, datetime.datetime):                              
        return ''
    return t.strftime("%Y-%m-%d %H:%M:%S")  

def a_fmttime(t):                                                                    
    """
    把时间变成标准化时间格式字符串                                                 
    """
    if not t or not isinstance(t, datetime.datetime):                              
        return ''
    return t.strftime("%Y-%m-%d %H:%M")  

def to_datetime(t, default_time=None):
    """
    数据库中取出的时间字符串，变成datetime对象
    """
    if not t:
        return default_time
    elif not isinstance(t, datetime.datetime):
        return datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    else:
        return t

def datetime_to_timestamp(d):
    """
    将datetime转换成时间戳
    """
    if not isinstance(d, datetime.datetime):
        return 
    t = d.timetuple()  
    timeStamp = int(time.mktime(t)*1000)  
    return timeStamp  

def one_day_two_minutes(t):
    """
    根据时间字符串t(2018-01-16)拿到一天每隔2分钟的时间列表
    """
    t_datetime = datetime.datetime.strptime(t, "%Y-%m-%d")
    t_list = [a_fmttime(t_datetime)]
    for i in range(48):
        t_datetime += datetime.timedelta(minutes=30)
        t_list.append(t_datetime)

    return t_list

def one_day_duration(t):
    """
    根据时间字符串t(2018-01-16)拿到一天开始和结束datetime
    """
    s_datetime = datetime.datetime.strptime(t, "%Y-%m-%d")
    e_datetime = s_datetime + datetime.timedelta(hours=24)
    return s_datetime, e_datetime
# 记录一个列表中各种元素的数量
count_numbers_dict = lambda lst: dict(Counter(lst).items())

def create_uuid_key():
    """
    利用uuid获取一个唯一标识
    """
    or_key = uuid.uuid1()
    try:
        public_key = or_key.get_hex()
    except AttributeError:
        public_key = or_key.hex
    return public_key[:16]
