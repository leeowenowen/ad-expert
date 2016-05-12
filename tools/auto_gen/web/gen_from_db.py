import os
import sys
import json
from DBConfigParser import DBConfigParser
from MySQLGenClient import MySQLGenClient
from FileUtil import FileUtil
from WebBuilder import WebBuilder
from DBInfo import DB, Table, Column
from TableHtmlBuilder import TableHtmlBuilder
from string import Template

def getTableConfigByName(table_configs, name):
    for table_config in table_configs:
        if table_config.name() == name:
            return table_config

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
        name = table_info.name()
        table_config = getTableConfigByName(db_config.tables(), name)
        tableHtmlBuilder = TableHtmlBuilder(table_config, table_info)
        tableHtmlBuilder.buildx()
        with open('web_template/table.template.html', 'r') as input:
            content = input.read()
            content_template = Template(content)
            content = content_template.substitute({'SERVER_PREFIX', tableHtmlBuilder.serverPrefxi(),
                                        'TABLE_HEADER', tableHtmlBuilder.tableHeader(),
                                        'TABLE_COLUMN', tableHtmlBuilder.tableColumn(),
#                                         'EDIT_OLD', tableHtmlBuilder.editOld(),
#                                         'EDIT_NEW', tableHtmlBuilder.editNew()
                                        })
            with open('web_template/' + name + ".html", 'w') as output:
                output.write(content)
mgc.close()

# declare variables






