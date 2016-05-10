import os
import sys
from string import Template

class WebBuilder:
    def __init(self):
        pass
    
    @staticmethod
    def buildTable(table, column_set):
        pass
    
    @staticmethod
    def buildTab(tables):
        lis = ''
        for table in tables:
            lis = lis + '<li>' + table + '</li>'
        with open('web_template/tables.template.html', 'r') as input:
            content = input.read()
            content = Template(content).substitute(TITLE="NO TITLE", LI=lis)
            with open('web_template/tables.html', 'w') as output:
                output.write(content)