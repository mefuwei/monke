#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# auther:keve
from server.core.getconfig import get_conf
import MySQLdb
import MySQLdb.cursors

DB_HOST=get_conf('db','DB_HOST').strip()
DB_PORT=int(get_conf('db','DB_PORT'))
DB_NAME=get_conf('db','DB_NAME')
DB_USER=get_conf('db','DB_USER')
DB_PAWD=get_conf('db','DB_PAWD')

class Pymysql:
    def __init__(self):
        self.conn = None
    def _connect(self):
        '''建立一个新的连接，从ｃonfig.ini 获取ｍｙsql信息'''
        try:
            self.conn=MySQLdb.connect(host=DB_HOST,port =DB_PORT,user =DB_USER,passwd=DB_PAWD,db=DB_NAME)
            return self.conn
        except MySQLdb.Error,err:
            print err[1]
            self.conn = None
            return self.conn
    def close_connect(self):
        """
        关闭连接
        """
        if (self.conn.open) == True:
            self.conn.close()
        else:
            pass


    def _cursor_db(self):
        self._connect()
        #return self.conn.cursor()
        return self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

    def findall(self, tables, what='*', where=None, val=None):
        curs = self._cursor_db()

        if where == None and val == None:
            sqltext = 'SELECT %s FROM %s' % (what,tables)
        elif where !=None and val != None:
            sqltext = 'SELECT %s FROM %s WHERE %s="%s"'% (what,tables,where,val)

        else:
            return None
        try:

            curs.execute(sqltext)
        except MySQLdb.Error:
            return None
        self.close_connect()
        return curs.fetchall()
    def find_join(self,tables,from_table, what='*', where=None, val=None):
        """
        从ｆrom_tables 查询　ｔables里的数据，

        """
        ids = self.findall(from_table,what,where,val)
        if ids != None:
            id = ids[0]["template_id"]
        else:
            return None

        curs = self._cursor_db()
        sqltext = "SELECT * FROM %s WHERE id='%s'" % (tables,id)
        try:
            curs.execute(sqltext)
        except MySQLdb.Error:
            return None
        self.close_connect()
        return curs.fetchone()
