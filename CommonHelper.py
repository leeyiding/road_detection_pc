import cv2
import os
from PyQt5.QtGui import *

class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()

    def displayImg(imgName,imageWin):
        jpg = QPixmap(imgName).scaled(imageWin.beforeImgContainer.width(),imageWin.beforeImgContainer.height())
        imageWin.beforeImgContainer.setPixmap(jpg)
        image = QPixmap(CommonHelper.testingImg(imgName)).scaled(imageWin.afterImgContainer.width(),imageWin.afterImgContainer.height())
        imageWin.afterImgContainer.setPixmap(image)

    def openImage(path,imageName):
        cmd = "cd {} && {}".format(path,imageName)
        os.system(cmd)

    def testingImg(image):
        pbtxt_file = './resources/model/model.pbtxt'
        pb_file = './resources/model/model.pb'
        net = cv2.dnn.readNetFromTensorflow(pb_file, pbtxt_file)
        score_threshold = 0.5
        imgName = os.path.basename(image)
        imgTempPath = "./sql/temp/" + imgName
        image = cv2.imread(image)
        height, width, _ = image.shape
        net.setInput(cv2.dnn.blobFromImage(image,size=(300, 300),swapRB=True,crop=False))
        out = net.forward()
        for detection in out[0, 0, :,:]:
            score = float(detection[2])
            if score > score_threshold:
                left = detection[3] * width
                top = detection[4] * height
                right = detection[5] * width
                bottom = detection[6] * height
                cv2.putText(image, str(int(score * 100))+"%",(int(left),int(top)),1,1,(0,0,250),1 )
                cv2.rectangle(image,(int(left), int(top)),(int(right), int(bottom)),(23, 230, 210),thickness=2)
        cv2.imwrite(imgTempPath,image)
        return imgTempPath
