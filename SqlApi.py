from PyQt5.QtSql import QSqlDatabase,QSqlQuery
import os

def createDB():
    if os.path.exists('./sql.sql.db') == False:
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./sql/sql.db')
        db.open()
        query = QSqlQuery()
        sql_code = 'create table testing (fileName varchar(255) primary key, date varchar(255), beforeImg varchar(255), afterImg varchar(255))'
        if query.exec_(sql_code):
            print('create a table')
        return True

if __name__ == '__main__':
    createDB()

