#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
import hashlib


def md5(s):
    """

    :param s:
    :return   返回个MD5字符串
    """
    return hashlib.new("md5",str(s)).hexdigest()