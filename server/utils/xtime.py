#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
import time
import datetime
def timestamp():
    """
    Get the server timestamp
    获取服务器时间戳!
    """
    return int(time.time())

def mstimestamp():
    """
    Get time stamp and accurate to millisecond
    获取时间戳并精确到毫秒

    """
    return int(time.time() * 1000)

def strdate():
    """
    Get the current date.
    @return YYYYmmdd
    获取当前日期.
    @20150501
    """
    return time.strftime("%Y%m%d",time.localtime(time.time()))

def strtime():
    """
    Get the current time.
    @return HHMMSS
    获取当前日期.
    @101057
    """
    return time.strftime("%H%M%S",time.localtime(time.time()))

def strdatetime(sign=False):
    """
    Get the current date and time.
    @return YYYY-mm-dd HH:MM:SS
    but sign is true
    @ return "%Y%m%d%H%M%S"
    获取当前日期.
    @ 2015-05-01 00:00:00
    当有值传入时返回
    @ 2015051219:08:23'
    """
    pattern = "%Y-%m-%d %H:%M:%S"
    if sign:
        pattern = "%Y%m%d%H%M%S"

    return time.strftime(pattern,time.localtime(time.time()))

def strdatetimefromats(stamp):
    """
    The timestamp format output
    :param stamp:
    :return: %Y-%m-%d %H:%M:%S
    传递个时间戳转格式化成人类可读的模式 年-月-日 时:分:秒
    """
    return (datetime.datetime.fromtimestamp(stamp)).strftime("%Y-%m-%d %H:%M:%S")

def strdatefromats(stamp):
    """
    The timestamp format output
    :param stamp:
    :return: %Y%m%d
    传递个时间戳转格式化成人类可读的模式 年月日
    """
    return (datetime.datetime.fromtimestamp(stamp)).strftime("%Y%m%d")

def today_time_stamp():
    """
    get the day start date time stamp
    :return:
    获取当天00:00:00的日时间戳
    """
    s= datetime.date.today()
    return int(time.mktime(s.timetuple()))

def tomorrow_time_stamp():
    """
    get tomorrow start date time stamp
    :return:
    获取明天00:00:00的日时间戳
    """
    return today_time_stamp() + 86400

def now_hour():
    """
    get the current time for hour
    :return: int type hour
    获取当前24小时时间,保留小时
    """
    return int(datetime.datetime.now().hour)
