import pyodbc
import sys

class Tibero:
    def __init__(self, dsn):
        self.dsn = dsn
        self.db = None
        self.cursor = None

    def get_window_db(self):
        self.db = pyodbc.connect(DSN=self.dsn)
        self.db.setdecoding(pyodbc.SQL_CHAR, encoding='cp949')
        self.db.setdecoding(pyodbc.SQL_WCHAR, encoding='cp949')
        self.db.setencoding(encoding='cp949')
        return self.db
        
    def get_linux_db(self):
        self.db = pyodbc.connect(DSN=self.dsn, CHARSET='UTF-8')
        self.db.setdecoding(pyodbc.SQL_CHAR, encoding='utf-32le')
        self.db.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-32le')
        self.db.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-32le')
        self.db.setencoding(encoding='utf-8')
        return self.db

    def get_cursor(self):
        if sys.platform == 'win32':
            self.cursor = self.get_window_db().cursor()
        elif sys.platform.startswith('linux'):
            self.cursor = self.get_linux_db().cursor()
        else:
            print(f'{sys.platform} not categorized')
        return self.cursor
    
    def connect(self):
        if self.cursor is None:
            try:
                self.get_cursor()
            except Exception as e:
                print(f'db connection failed {e}')
        else:
            print('cursor is already exist')

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.db:
            self.db.close()
            self.db = None
    
def main():
    cdb = Tibero('CDB')
    ndb = Tibero('RGOUTSIGHT')
    print(cdb.db, cdb.cursor)
    cdb.connect()
    print(cdb.db, cdb.cursor)
    cdb.disconnect()
    print(cdb.db, cdb.cursor)
    
if __name__ == '__main__':
    main()