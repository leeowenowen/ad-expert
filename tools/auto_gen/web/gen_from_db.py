import os
import sys
import json
from DBConfigParser import DBConfigParser
from MySQLGenClient import MySQLGenClient

def ParseDBConfig(path):
    with open(path, 'r') as config_json:
        config = json.load(config_json)
        db = DBConfigParser.fromJson(config)
        return db


db_config = ParseDBConfig('config.json')
mgc = MySQLGenClient(db_config)

mgc.open()

table_sets = mgc.fetchTableInfo()
for table_set in table_sets:
    for table in table_set:
        print '%s----------------' % table
        column_sets = mgc.fetchColumnInfo('user')
        for column_set in column_sets:
            column_list = list(column_set)
            name = column_list[0]
            data_type = column_list[1]
            column_type = column_list[2]
            print '%s, %s, %s' % (name, data_type, column_type)
        
mgc.close()


