from DBConfig import Columns, Table, DB

class DBConfigParser:
    @staticmethod
    def fromJson(json):
        json_db = json['db']
        db = DB()
        db.setHost(json_db['host'])
        db.setPort(json_db['port'])
        db.setName(json_db['name'])
        db.setUser(json_db['username'])
        db.setPassword(json_db['password'])
        db.setCharset(json_db['charset'])
        json_tables = json_db['tables']
        for json_table in json_tables:
            table = Table()
            table.setName(json_table['name'])
            table.setTitle(json_table['title'])
            json_columns = json_table['columns']
            columns = Columns()
            columns.set(json_columns)
            table.setColumns(columns)
        return db

        


        
