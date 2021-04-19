# -*- coding: utf-8 -*-
# @Date    : 2021-01-17 18:31:46
# @Author  : leeyiding (admin@lyd.im)
# @Link    : https://www.leeyiding,com/
# @Version : Python3.8.6

import sys
import os
import time
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel
from ui_mainWindow import Ui_MWin
from ui_imageWindow import Ui_ImageWin
from ui_sqlWindow import Ui_SqlWin
from CommonHelper import CommonHelper
from MyQLabel import MyQLabel

# 创建主窗口类
class MainWindow(QWidget,Ui_MWin):
    def __init__(self):
        super(MainWindow,self).__init__()
        # 初始化主窗口UI
        self.setupUi(self)
        # 初始化槽函数
        self.connectSlots()
        # 创建子窗口类
        self.imageWin = ImageWindow()
        styleFile = './style.qss'
        qssStyle = CommonHelper.readQSS(styleFile)
        self.imageWin.setStyleSheet(qssStyle)

    def connectSlots(self):
        '''为按钮连接槽函数/设置快捷键'''
        self.imageBtn.clicked.connect(self.openImage)
        self.imageBtn.setShortcut('CTRL+I')
        self.sqlBtn.clicked.connect(self.openSql)
        self.sqlBtn.setShortcut('CTRL+S')

    def openImage(self):
        '''检测图片按钮点击事件'''
        # 弹出文件对话框
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        
        # 判断文件名不为空，弹出子窗口
        if imgName:
            self.imageWin.show()
            self.imageWin.imgName = imgName
            CommonHelper.displayImg(imgName,self.imageWin)
        return imgName

    def openSql(self):
        # 初始化窗口
        self.sqlWin = SqlWindow()
        self.sqlWin.setStyleSheet(qssStyle)
        self.sqlWin.show()

# 创建子窗口类
class ImageWindow(QWidget,Ui_ImageWin):
    def __init__(self):
        super(ImageWindow,self).__init__()
        self.setupUi(self)
        self.imgName = ''
        self.connectSlots()
        
    def connectSlots(self):
        self.btnOK.clicked.connect(self.close)
        self.btnSaveSql.clicked.connect(self.saveSQL)
        self.beforeImgContainer.connectCustomizedSlot(lambda:CommonHelper.openImage("./sql/before",os.path.basename(self.imgName)))
        self.afterImgContainer.connectCustomizedSlot(lambda:CommonHelper.openImage("./sql/after",os.path.basename(self.imgName)))
    
    def saveSQL(self):
        fileName = os.path.basename(self.imgName)
        tempFile = './sql/temp/{}'.format(fileName)
        beforeImg = './sql/before/{}'.format(fileName)
        afterImg = './sql/after/{}'.format(fileName)
        shutil.copyfile(self.imgName,beforeImg)
        shutil.move(tempFile,afterImg)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 连接数据库
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./sql/sql.db')
        db.open()
        query = QSqlQuery()
        # 数据库查重
        sqlCode = 'select * from testing'
        query.exec_(sqlCode)
        while query.next():
            if fileName == query.value(0):
                QMessageBox.warning(self,"警告","同名文件已存在数据库\n请重命名图片或选择其它图片",QMessageBox.Yes|QMessageBox.Yes)
                break
            else:
                # 数据入库
                sqlCode = "insert into testing values ('{}','{}','{}','{}')".format(fileName,date,beforeImg,afterImg)
                if query.exec_(sqlCode):
                    print("insert data")
                    QMessageBox.information(self,"提示","存入数据库成功",QMessageBox.Yes|QMessageBox.Yes)
                db.close()
        

class SqlWindow(QWidget,Ui_SqlWin):
    def __init__(self):
        super(SqlWindow,self).__init__()
        self.setupUi(self)
        self.getData()

    def getData(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./sql/sql.db')
        db.open()

        query = QSqlQuery()
        sqlCode = 'select * from testing'
        query.exec_(sqlCode)
        row = 0
        while query.next():
            fileName = query.value(0)
            date = query.value(1)
            beforeImg = query.value(2)
            afterImg = query.value(3)

            item1 = QTableWidgetItem(fileName)
            item1.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(row,0,item1)
            item2 = QTableWidgetItem(date)
            item2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(row,1,item2)

            # 显示图片
            beforeImgLabel = MyQLabel(QLabel(self))
            beforeImgLabel.setAlignment(Qt.AlignCenter) 
            beforeImgLabel.setPixmap(QPixmap(beforeImg).scaled(50,50))
            self.tableWidget.setCellWidget(row,2,beforeImgLabel)
            # 点击查看图片
            beforeImgLabel.connectCustomizedSlot(lambda:CommonHelper.openImage("./sql/before",self.tableWidget.item(self.tableWidget.currentRow(),0).text()))
            afterImgLable = MyQLabel(QLabel(self))
            afterImgLable.setAlignment(Qt.AlignCenter)
            afterImgLable.setPixmap(QPixmap(afterImg).scaled(50,50))
            self.tableWidget.setCellWidget(row,3,afterImgLable)
            # 点击查看图片
            afterImgLable.connectCustomizedSlot(lambda:CommonHelper.openImage("./sql/after",self.tableWidget.item(self.tableWidget.currentRow(),0).text()))
            
            # 添加按钮
            delBtn = QPushButton()
            delBtn.setObjectName('delBtn')
            delBtn.setText('删除')
            delBtn.setToolTip('删除此条数据')
            delBtn.clicked.connect(lambda:self.delData(self.tableWidget.currentRow()))
            self.tableWidget.setCellWidget(row,4,delBtn)

            row += 1
        self.rowCount = row
        
        db.close()
    
    def delData(self,row):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./sql/sql.db')
        db.open()
        fileName = self.tableWidget.item(row,0).text()
        self.tableWidget.removeRow(row)
        query = QSqlQuery()
        sqlCode = "delete from testing where fileName = '{}'".format(fileName)
        query.exec_(sqlCode)
        db.close
        os.remove('./sql/before/{}'.format(fileName))
        os.remove('./sql/after/{}'.format(fileName))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置窗口图标
    app.setWindowIcon(QIcon('./resources/image/logo.jpg'))
    win = MainWindow()
    # 主窗口装载QSS
    styleFile = './style.qss'
    qssStyle = CommonHelper.readQSS(styleFile)
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())