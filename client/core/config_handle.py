#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:keve

import cPickle

from conf.setting import rootDir
file_conf_pkl = rootDir + '/logs/config.pkl'


def save_conf(conf):
    if isinstance(conf,str):
        data = cPickle.loads(conf)
        f = file(file_conf_pkl,'wb')
        cPickle.dump(data,f)
    else:
        f = file(file_conf_pkl,'wb')
        cPickle.dump(conf,f)
    f.close()


def config():
    f = file(file_conf_pkl,'r')
    conf=cPickle.load(f)
    f.close()

    return conf

