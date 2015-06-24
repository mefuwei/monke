#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
from client.conf.setting import rootDir
confFile = rootDir+"/conf/config.ini"
import ConfigParser

def get_conf(section,index):
    """

    :param section: 节点分割名称
    :param index: 节点子项
    :return: success return str ,failed return (None,reason)
    """
    cf = ConfigParser.ConfigParser()
    cf.read(confFile)
    try:
        val = cf.get(section,index)
        return val
    except (ConfigParser.NoOptionError,ConfigParser.NoSectionError) as reason:

        return (None,reason)
