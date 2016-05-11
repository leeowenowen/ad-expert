import os
import sys
import json
from DBConfigParser import DBConfigParser
from MySQLGenClient import MySQLGenClient
from FileUtil import FileUtil
from WebBuilder import WebBuilder
from DBInfo import DB, Table, Column

def ParseDBConfig(path):
    with open(path, 'r') as config_json:
        config = json.load(config_json)
        db = DBConfigParser.fromJson(config)
        return db


db_config = ParseDBConfig('config.json')
mgc = MySQLGenClient(db_config)

mgc.open()

table_sets = mgc.fetchTableInfo()
db_info = DB()
for table_set in table_sets:
    WebBuilder.buildTab(table_set)
    for table in table_set:
        print '%s----------------' % table
        table_info = Table()
        table_info.setName(table)
        column_sets = mgc.fetchColumnInfo(table)
        WebBuilder.buildTable(table, column_sets)
        for column_set in column_sets:
            column_info = Column()
            column_list = list(column_set)
            name = column_list[0]
            data_type = column_list[1]
            column_type = column_list[2]
            column_key = column_list[3]
            extra = column_list[4]
            column_info.setName(name)
            column_info.setDataType(data_type)
            column_info.setColumnType(column_type)
            column_info.setColumnKey(column_key)
            column_info.setExtra(extra)
            table_info.addColum(column_info)
            print '%s, %s, %s, %s, %s' % (name, data_type, column_type, column_key, extra)
        db_info.addTable(table_info)
mgc.close()


