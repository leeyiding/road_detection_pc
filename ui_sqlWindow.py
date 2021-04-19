from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel

class Ui_SqlWin(object):
    def setupUi(self, SqlWin):
        self.setObjectName('SqlWin')
        self.setWindowTitle('查询历史')
        self.resize(800,450)
        self.setMinimumSize(QSize(800,450))

        # 获取数据库行数
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./sql/sql.db')
        db.open()
        queryModel =QSqlQueryModel()
        queryModel.setQuery('select * from testing')
        self.rowCount = queryModel.rowCount()
        db.close()

        # 添加表格控件
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.rowCount)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['名称','检测时间','检测图片','检测结果','操作'])
        # 禁止编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选择
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 自动调节
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()
        # 扩展整行
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 调整表格宽高
        for i in range(self.rowCount):
            self.tableWidget.setRowHeight(i,50)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
