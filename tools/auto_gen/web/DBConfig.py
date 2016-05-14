class Column:
    
    def __init__(self):
        self.__name = ''
        self.__title = ''
        self.__enum = {}

    def setEnum(self, kv):
        self.__kv = kv
    
    def enum(self, k):
        return self.__kv[k]
    def enums(self):
        return self.__kv

    def setName(self, name):
        self.__name = name
    def name(self):
        return self.__name
    def setTitle(self, title):
        self.__title = title
    def title(self):
        return self.__title

class Table:
    def __init__(self):
        self.__name = ''
        self.__title = ''
        self.__columns = []
        
    def setName(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def setTitle(self, title):
        self.__title = title

    def title(self):
        return self.__title
    
    def addColum(self, column):
        self.__columns.append(column)

    def columns(self):
        return self.__columns
    
    def column(self, name):
        for column in self.__columns:
            if column.name() == name:
                return column

class DB:
    
    def __init__(self):
        self.__host = ''
        self.__port = ''
        self.__username = ''
        self.__password = ''
        self.__name = ''
        self.__charset = ''
        self.__tables = []
    
    def setHost(self, host):
        self.__host = host

    def host(self):
        return self.__host
    
    def setPort(self, port):
        self.__port = port

    def port(self):
        return self.__port

    def setName(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def setUser(self, user):
        self.__username = user

    def user(self):
        return self.__username

    def setPassword(self, password):
        self.__password = password

    def password(self):
        return self.__password

    def setCharset(self, charset):
        self.__charset = charset

    def charset(self):
        return self.__charset
 
    def addTable(self, table):
        self.__tables.append(table)

    def tables(self):
        return self.__tables

    def getTable(self, name):
        for table in self.__tables:
            if table.name() == name:
                return table
