


class TableHtmlBuilder:
    def __init__(self, table_config, table_info):
        self.__table_config = table_config
        self.__table_info = table_info
        self.__server_prefix = ''
        self.__table_header = ''
        self.__table_column = ''
        self.__edit_old = ''
        self.__edit_new = ''
        self.__delete = ''
        self.__add_hide_auto = ''
        self.__add = ''
        self.__form = ''
        
            
    
    def build(self):
        # build __server_prefix
        # build __table_header
        table_columns = []
        for column in self.__table_info.columns():
            table_columns.append(column.name())
        # build __table_column
        self.__table_column = self.listToString(table_columns)
        # build edit old
        self.__edit_old = self.buildEditOld(table_columns)
        # build edit new
        self.__edit_new = self.buildEditNew(table_columns)  
          
        columns_config = self.__table_config.columns()
        for column_config in columns_config:
            name = column_config.name()
            title = column_config.title()
            for i in range(len(table_columns)):
                # user title replace name
                if table_columns[i] == name:
                    table_columns[i] = title
        self.__table_header = self.listToString(table_columns)
        self.__delete = self.buildDelete();
        self.__add = self.buildAdd();
        self.__form = self.buildForm()
        
    
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
    def delete(self):
        return self.__delete
    def addHideAuto(self):
        return self.__add_hide_auto
    def add(self):
        return self.__add
    def form(self):
        return self.__form
    
    def getEnumFromColumnType(self, column_type):
        items = column_type.split(',')
        for i in range(len(items)):
            item = items[i]
            start = item.find('\'')
            end = item.find('\'', start + 1)
            if start >= 0 and end >= 0:
                items[i] = item[start:end]
        return items
    
    def buildForm(self):
        ret = ''
        for column in self.__table_info.columns():
            col_name = column.name()
            col_config = self.__table_config.column(col_name)
            if(column.isAutoIncrement()):
                ret += '<p id=\"p_edit_%s\">id: <input type=\"text\" id=\"edit_%s\" readonly style="width: 300px"/></p>' % (col_name, col_name)
            else:
                if(column.isEnum()):
                    start = '<p>%s: <select id=\"edit_%s\" style=\"width: 300px\">' % (col_name, col_name)
                    content = ''
                    end = '</select></p>'
                    col_type = column.columnType()
                    enums = self.getEnumFromColumnType(col_type)
                    for i in range(len(enums)):
                        e = enums[i]
                        if e in col_config.enums():
                            enums[i] = col_config.enums()[e]
                            content += '<option value="%s">%s</option>' % (e, enums[i])
                    ret += start
                    ret += content
                    ret += end
                else:
                    ret += '<p>%s: <input type="text" id="edit_%s" style="width: 300px"/></p>' % (col_name, col_name)
        return ret
            
        
        
    
    @staticmethod
    def buildAddHideAuto(table_info):
        ret = ''
        auto_increment_columns = table_info.autoIncrement()
        for col in auto_increment_columns:
            ret += 'document.getElementById(\"p_edit_%s\").style.display = \"none\";' % (col.name())
        return ret

    def buildAdd(self):
        ret = ''
        columns = []
        for col in self.__table_info.columns():
            if not col.isAutoIncrement():
                columns.append(col)
        condition = ''
        params = ''
        for i in range(len(columns)):
            column = columns[i]
            name = column.name()
            ret += 'var %s = document.getElementById(\"edit_%s\").value;' % (name, name)
            condition += '%s != null' % (name)
            if i != len(columns) - 1:
                condition += " &&"
            if i != 0:
                params += '+ \"&'
            params += '%s=\" + %s' % (name, name)
        ret += 'if ( %s){ var url=%sadd?%s;' % (condition, 'SERVER_PREFIX', params)
        return ret

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
        for i in range(len(columns)):
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
            if i != len(columns) - 1:
                condition += " || "
            if i != 0:
                params += '+ \"&'
            params += '%s=\" + %s' % (column, column)
        ret += 'if ( %s){ var url=%supdate?%s;' % (condition, 'SERVER_PREFIX', params)
        return ret

    def buildDelete(self):
        ret = ''
        primary_keys = self.__table_info.primaryKeys()
        if len(primary_keys) > 0:
            params = ''
            for i in range(len(primary_keys)):
                pk_pair = primary_keys[i]
                pk = pk_pair[0].name()
                pk_index = pk_pair[1]
                ret += 'var %s = row.cells[%s].innerHTML;' % (pk, pk_index)
                if i != 0:
                    params += '+ \"&'
                params += '%s=\" + %s' % (pk, pk)
            ret += 'var url=%sdelete?%s;' % ('SERVER_PREFIX', params)    
        else:
            print 'no primary key in table'
            pass
        return ret
        
        
