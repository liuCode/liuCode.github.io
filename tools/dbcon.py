'''
Created on 2018-1-11

@author: corey
'''
import platform
import MySQLdb
class MynewcoderDB:
    def __init__(self):
        self.db_conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='liu',
        passwd='123456',
        db ='newcoder',
        charset='utf8',
        )
        self.db_cur = self.db_conn.cursor()
    def execute(self,sqlstr):
        self.db_cur.execute(sqlstr)
    def getInfo(self,sqlstr):
        sqlstr = sqlstr.decode("utf-8")
        self.execute(sqlstr)
        return self.db_cur.fetchall()
    def commit(self):
        self.db_conn.commit()
    def close(self):
        self.db_cur.close()
        self.db_conn.close()
        
