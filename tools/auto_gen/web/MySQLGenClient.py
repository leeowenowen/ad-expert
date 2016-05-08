import os
import sys
import json
import MySQLdb

class MySQLGenClient:
    __db = None
    __conn = None
    __cursor = None
    
    def __init__(self, db):
        self.__db = db

    def __safeCall(self, func):
        try:
            return func()
        except Exception, e:
            print Exception, ":", e

    def open(self): 
        def openImpl():
            self.__conn = MySQLdb.connect(host=self.__db.host(), user=self.__db.user(), passwd=self.__db.password(), db=self.__db.name(), port=self.__db.port(), charset=self.__db.charset())

            self.__cursor = self.__conn.cursor()
            self.__conn.select_db(self.__db.name())
        return self.__safeCall(openImpl)

    def close(self):
        def closeImpl():
            self.__cursor.close()
            self.__conn.close()
        return self.__safeCall(closeImpl) 

    def execute(self, sql):
        def executeImpl():
            count = self.__cursor.execute(sql)
            results = self.__cursor.fetchall()
            return results
        return self.__safeCall(executeImpl)
