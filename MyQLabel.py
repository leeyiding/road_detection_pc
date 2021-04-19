# 重写QLabel，使其添加单击事件
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent
class MyQLabel(QLabel):
    buttonClickedSignal = pyqtSignal()

    def __init__(self,parent=None):
        super(MyQLabel,self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.buttonClickedSignal.emit()

    def connectCustomizedSlot(self,func):
        self.buttonClickedSignal.connect(func)