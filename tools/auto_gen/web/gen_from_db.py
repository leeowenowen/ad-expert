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
            #content_template = Template(content)
            table_header = tableHtmlBuilder.tableHeader()
            table_column = tableHtmlBuilder.tableColumn()
            edit_old = tableHtmlBuilder.editOld()
            edit_new = tableHtmlBuilder.editNew()
            print 'table_header:', table_header
            print 'table_column:', table_column
            print 'edit_old:', edit_old
            print 'edit_new:', edit_new
            print type(table_header)
            print type(table_column)
            print type(edit_old)
            print type(edit_new)
            content = content.replace('$SERVER_PREFIX',tableHtmlBuilder.serverPrefxi())
            content = content.replace('$TABLE_HEADER', table_header)
            content = content.replace('$TABLE_COLUMNS', table_column)
            content = content.replace('$EDIT_OLD', edit_old)
            content = content.replace('$EDIT_NEW', edit_new)
#             content = content.replace(ADD="ADD")
#             content = content.replace(ADD_HEADER_AUTO="ADD_HEADER_AUTO")
#             content = content.replace(QUERY_MAKE_TABLE="QUERY_MAKE_TABLE")
#             content = content.replace(QUERY="QUERY")
            with open('web_template/' + name + ".html", 'w') as output:
                output.write(content)
mgc.close()

# declare variables






