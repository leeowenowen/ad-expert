


class TableHtmlBuilder:
    def __init__(self, table_config, table_info):
        self.__table_config = table_config
        self.__table_info = table_info
        self.__server_prefix = ''
        self.__table_header = ''
        self.__table_column = ''
        self.__edit_old = ''
        self.__edit_new = ''
        
            
    
    def buildx(self):
        # build __server_prefix
        # build __table_header
        table_header = []
        for column in self.__table_info.columns():
            table_header.append(column.name())
        columns_config = self.__table_config.columns()
        for column_config in columns_config:
            name = column_config.name()
            title = column_config.title()
            for i in range(0, len(table_header)):
                # user title replace name
                if table_header[i] == name:
                    table_header[i] = title
        self.__table_header = self.listToString(table_header)
        # build __table_column
        self.__table_column = self.listToString(self.__table_info.columns())
        # build edit old
        self.__edit_old = self.buildEditOld(self.__table_column)
        # build edit new
        self.__edit_new = self.buildEditNew(self.__table_column)
        
    
    def serverPrefxi(self):
        return self.__server_prefix
    def tableHeader(self):
        return self.__table_header
    def tableColumn(self):
        return self.__table_column
    def editOld(self):
        return self.__edit_old
    def editNew(self):
        return self.__edit_new
    
    @staticmethod
    def listToString(l):
        ret = '['
        for i in range(0, len(l)):
            item = l[i]
            ret += ('\"%s\"') % (item)
            if i != (len(l) - 1):
                ret = ret + ','
        ret = ret + ']'
        return ret
    
    @staticmethod
    def buildEditOld(columns):
        ret = ''
        for i in range(0, len(columns)):
            column = columns[i]
            ret += ('var %s = row.cells[%d].innerHTML;' % (column, i))
            ret += ('document.getElementById("edit_%s").value = %s;') % (column, column)
        return ret
    
    @staticmethod
    def buildEditNew(columns):
        ret = ''
        condition = ''
        params = ''
        for i in range(0, len(columns)):
            column = columns[i]
            ret += 'var new_%s = document.getElementById("edit_%s").value;' % (column, column)
            condition += '%s != new_%s' % (column, column)
            if i != 0:
                params += '&'
            params += '%s=\" + %s' % (column, column)
        ret += 'if ( %s){ var url=%supdate?%s;' % (condition, 'SERVER_PREFIX', params)
        return ret

        
