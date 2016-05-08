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


db = ParseDBConfig('config.json')
mgc = MySQLGenClient(db)
mgc.open()
mgc.close()

