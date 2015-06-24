#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W

import connect_db
from server.template import templates
from server.core import getconfig
from server.utils import xpickle
from server.cache import redisengine

redis_server = eval(getconfig.get_conf("redis",'all_redis'))
r = redisengine.RedisEngine(redis_server)
def get_status():

    status =r.get_data("1","status")
    return status


def get_host_config(address):
    """
    get monitor configuration info for host server
    :args address:
    :return: dict
    """

    db = connect_db.Pymysql()
    host_data = db.findall("host_ip",where="ip",val=address)
    if host_data:
        for i in host_data:
            port = i['port']
            hostname = i['hostname']
    tp_data = db.find_join("host_template","host_ip",where='ip',val=address)
    tp_name= tp_data['name']
    host_conf = eval("templates."+tp_name+"()")
    host_conf.hostname = hostname
    host_conf.port = port
    config_dict = {}

    config_dict['hostname'] = host_conf.hostname
    config_dict["port"] = host_conf.port
    config_dict["status"] = "on"
    for k,v in host_conf.services.items():
        config_dict[k]=[v.interval,v.plugin_name,0]

    return xpickle.dumps(config_dict)





def get_host_ip():
    db = connect_db.Pymysql()
    hosts_list = db.findall('host_ip',what="ip")
    config_dict = {}
    for host in hosts_list:
        ip = host['ip']
        cf = get_host_config(ip)
        config_dict[ip] = cf

    return config_dict





