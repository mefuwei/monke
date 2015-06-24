#coding:utf-8
#auther:F.W
import cPickle

def dumps(o):
    """
    :param o: Serialized objects
    :return: cpickle dumps
    """
    return cPickle.dumps(o,cPickle.HIGHEST_PROTOCOL)

def loads(s):
    return cPickle.loads(s)