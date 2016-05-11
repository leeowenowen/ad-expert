import os
import sys
import json
import MySQLdb

class MySQLGenClient:
    
    def __init__(self, db):
        self.db = db
        self.conn = None
        self.cursor = None

    def safeCall(self, func):
        try:
            return func()
        except Exception, e:
            print Exception, ":", e

    def open(self): 
        def openImpl():
            self.conn = MySQLdb.connect(host=self.db.host(), user=self.db.user(), passwd=self.db.password(), db=self.db.name(), port=self.db.port(), charset=self.db.charset())

            self.cursor = self.conn.cursor()
            return self.conn.select_db(self.db.name())
        return self.safeCall(openImpl)

    def close(self):
        def closeImpl():
            self.cursor.close()
            return self.conn.close()
        return self.safeCall(closeImpl) 

    def execute(self, sql):
        def executeImpl():
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        return self.safeCall(executeImpl)
    def fetchDBInfo(self):
        pass
    def fetchTableInfo(self):
        sql = "show tables"
        return self.execute(sql)
    
    def fetchColumnInfo(self, table):
        sql = "select column_name,data_type, column_type, column_key, extra from information_schema.columns where table_name = '%s' and table_schema='%s'" % (table, self.db.name())
        return self.execute(sql)