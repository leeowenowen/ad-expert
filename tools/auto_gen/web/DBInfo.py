class Column:
    def __init__(self):
        self.__name = ''
        self.__data_type = ''
        self.__column_type = []
        self.__column_key = ''
        self.__extra = ''

    def setName(self, name):
        self.__name = name
    def name(self):
        return self.__name
    
    def setDataType(self, data_type):
        self.__data_type = data_type
    def dataType(self):
        return self.__data_type
    def setColumnType(self, column_type):
        self.__column_type = column_type
    def columnType(self):
        return self.__column_type
    def setColumnKey(self, column_key):
        self.__column_key = column_key
    def columnKey(self):
        return self.column_key
    def setExtra(self, extra):
        self.__extra = extra
    def extra(self):
        return self.__extra
    
    def isAutoIncrement(self):
        return self.__extra.lower().find("auto_increment") >= 0
    
    def isPrimaryKey(self):
        return self.__column_key.upper().find("PRI") >= 0
class Table:
    def __init__(self):
        self.__name = ''
        self.__columns = []
        self.__pk_columns = []
        self.__autoinc_columns = []
        
    def setName(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def addColum(self, column):
        self.__columns.append(column)

    def columns(self):
        return self.__columns
    
    def check(self):
        for col in self.__columns:
            if col.isPrimaryKey():
                self.__pk_columns.append(col)
            if col.isAutoIncrement():
                self.__autoinc_columns.append(col)
    def primaryKeys(self):
        return self.__pk_columns
    def autoIncrement(self):
        return self.__autoinc_columns
    
class DB:
    
    def __init__(self):
        self.__name = ''
        self.__tables = []
    
    def setName(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def addTable(self, table):
        self.__tables.append(table)

    def tables(self):
        return self.__tables


