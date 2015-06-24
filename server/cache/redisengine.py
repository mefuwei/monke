#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:F.W
import redis

from server.utils import xpickle, xmd5


class RedisEngine(object):
    """
    Redis 集群类,
    """
    def __init__(self,servers=[],expire=7200):
        '''
        servers=[(host,port)]
        '''
        self.pools = []
        for redis_host,redis_port in servers:

            pool = redis.StrictRedis(host=redis_host,port=redis_port)
            self.pools.append(pool)
        self.node_num = len(servers)
        self.expire = expire

    def _connection(self,hash_key):
        "hash 分配到redis事例"
        index = int(xmd5.md5(hash_key)[:2],16) % self.node_num
        return self.pools[index]

    def get_data(self,hash_key,key):
        """

        :param hashkey: 主机名或IP
        :param key: model 对象主键
        :data: model object dictionary
        """
        val = self._connection(hash_key).get(key)
        if val is None:
            return None

        return val
    def get_pk_data(self,hash_key,key):
        """

        :param hashkey: 主机名或IP
        :param key: model 对象主键
        :data: model object dictionary
        """
        val = self._connection(hash_key).get(key)
        if val is None:
            return None
        data = xpickle.loads(val)
        return data

    def put_pk_data(self,hash_key,key,data):
        """

        :param hash_key: 主机唯一标识
        :param key: redis 主键
        :param data: 对象字典
        :return: 数据存入Redis 一个序列化数据

        """
        val = xpickle.dumps(data)
        return self._connection(hash_key).set(key,val)

    def put_data(self,hash_key,key,data):
        """

        :param hash_key: 主机唯一标识
        :param key: redis 主键
        :param data: 对象字典
        :return: 数据存入Redis

        """

        return self._connection(hash_key).set(key,data)


    def delete(self,hash_key,key):
        """

        :param hash_key: 主机唯一标识
        :param key: redis 主键
        :return 删除对应key 的 value ,返回true,false

        """
        return self._connection(hash_key).delete(key)







