from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_MWin(object):
    def setupUi(self, MWin):
        self.setObjectName('Mwin')
        # 设置主窗口的标题
        self.setWindowTitle('路面灾害检测系统')
        # 设置窗口的尺寸
        self.resize(1200,675)
        self.setMinimumSize(QSize(1200,675))

        # 设置按钮
        self.imageBtn = QPushButton()
        self.imageBtn.setObjectName('imageBtn')
        self.imageBtn.setText('检测图片')
        self.imageBtn.setToolTip('点击上传图片')
        self.imageBtn.setIcon(QIcon(QPixmap('./resources/image/image.png')))
        self.sqlBtn = QPushButton()
        self.sqlBtn.setText('查询数据库')
        self.sqlBtn.setObjectName('sqlBtn')
        self.sqlBtn.setToolTip('点击查询历史数据')
        self.sqlBtn.setIcon(QIcon(QPixmap('./resources/image/sql.png')))

        # 设置按钮尺寸策略
        sizePolicy = QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.imageBtn.setSizePolicy(sizePolicy)
        self.sqlBtn.setSizePolicy(sizePolicy)

        # 设置按钮尺寸
        self.imageBtn.setMinimumSize(QSize(240,120))
        self.sqlBtn.setMinimumSize(QSize(240,120))

        # 添加水平布局
        layout = QHBoxLayout()
        layout.setSpacing(40)
        layout.addWidget(self.imageBtn)
        layout.addWidget(self.sqlBtn)

        # 设置布局
        self.setLayout(layout)
