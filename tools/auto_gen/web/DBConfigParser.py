from DBConfig import Column, Table, DB

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
            for json_column in json_columns:
                column = Column()
                column.setName(json_column['name'])
                column.setTitle(json_column['title'])
                if 'enum' in json_column.keys():
                    column.setEnum(json_column['enum'])
                table.addColum(column)
            db.addTable(table)
        return db

        


        
