class Columns:
    __kv = {}
    def __init__(self):
        pass

    def set(self, kv):
        self.__kv = kv
    
    def get(self, k):
        return self.__kv[k]
    
    def contains(self, k):
        return k in self.__kv

class Table:
    __name = ''
    __title = ''
    __columns = {}
    def setName(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def setTitle(self, title):
        self.__title = title

    def title(self):
        return self.__title
    
    def setColumns(self, columns):
        self.__columns = columns

    def columns(self):
        return self.__columns

class DB:
    __host = ''
    __port = ''
    __username = ''
    __password = ''
    __name = ''
    __charset = ''
    __tables = []
    
    def __init__(self):
        pass
    
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


