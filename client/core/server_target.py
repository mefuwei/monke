#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:keve

from conf import setting
from utils import xtime
import plugins_api
import config_handle
from threading import Thread
import Queue
m_queue = Queue.Queue()
def run(args):
    service_name,interval,plugin_name,hostname = args
    plugin_func = getattr(plugins_api,plugin_name)
    result = plugin_func()
    data = {"hostname":hostname,"service_name":service_name,"data":result}
    m_queue.put(data)

def get_data():
    conf_dict = config_handle.config()
    hostname = conf_dict["hostname"]
    for k,v in conf_dict.items():
        if k =="status":
            pass
        elif k == 'hostname':
            pass
        elif k == "port":
            pass
        else:
            service_name,interval,plugin_name,last_run_time = k,v[0],v[1],v[2]

            if xtime.timestamp() - last_run_time > interval:
                t = Thread(target=run,args=[(service_name,interval,plugin_name,hostname),])
                t.start()
                conf_dict[service_name][2] = xtime.timestamp()
                config_handle.save_conf(conf_dict)
                t.join()
                return m_queue
            else:
                next_run_time = interval -(xtime.timestamp() - last_run_time)
                #print "%s next run time %ss"% (service_name,next_run_time)





