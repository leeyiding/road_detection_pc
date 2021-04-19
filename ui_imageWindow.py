from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MyQLabel import MyQLabel

class Ui_ImageWin(object):
    def setupUi(self, imageWin):
        self.setObjectName('imageWin')
        self.setWindowTitle('检测结果')
        self.resize(800,450)
        self.setMinimumSize(QSize(800,450))
        self.beforeTitle = QLabel(self)
        self.beforeTitle.setText("待检图片")
        self.beforeTitle.setAlignment(Qt.AlignCenter)
        self.beforeImgContainer = MyQLabel(QLabel(self))
        self.beforeImgContainer.setFixedSize(350,350)
        self.afterTitle = QLabel(self)
        self.afterTitle.setText("检测结果")
        self.afterTitle.setAlignment(Qt.AlignCenter)
        self.afterImgContainer = MyQLabel(QLabel(self))
        self.afterImgContainer.setFixedSize(350,350)
        self.btnOK = QPushButton()
        self.btnOK.setObjectName('btnOK')
        self.btnOK.setText('确定')
        self.btnOK.setToolTip('确定')
        self.btnOK.setObjectName('btnOK')
        self.btnSaveSql = QPushButton()
        self.btnSaveSql.setObjectName('btnSaveSql')
        self.btnSaveSql.setText('存入数据库')
        self.btnSaveSql.setToolTip('存入数据库')
        self.btnSaveSql.setObjectName('btnSaveSql')

        # 设置按钮尺寸策略
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.btnOK.setSizePolicy(sizePolicy)
        self.btnSaveSql.setSizePolicy(sizePolicy)

        # 设置按钮尺寸
        self.btnOK.setMinimumSize(QSize(200,30))
        self.btnSaveSql.setMinimumSize(QSize(200,30))

        # 添加布局
        mainLayout = QVBoxLayout(self)
        topLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        btnLayout = QHBoxLayout()

        #布局添加控件
        leftLayout.addWidget(self.beforeTitle)
        leftLayout.addWidget(self.beforeImgContainer)
        rightLayout.addWidget(self.afterTitle)
        rightLayout.addWidget(self.afterImgContainer)
        btnLayout.addWidget(self.btnOK)
        btnLayout.addWidget(self.btnSaveSql)

        topLayout.addLayout(leftLayout)
        topLayout.addLayout(rightLayout)
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(btnLayout)

        self.setLayout(mainLayout)