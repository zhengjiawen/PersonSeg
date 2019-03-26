import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from segmentationPerson import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2 as cv
from humanseg import Humanseg as H
from PIL import Image,ImageTk






class segWindows(QWidget, Ui_Dialog):
    def __init__(self):
        super(segWindows, self).__init__()
        self.setupUi(self)
        self.imgName = 'img/xixi.jpg'

    def resizeImg(img):
        targetSize = 600
        maxSize = 800
        h = img.shape[0]
        w = img.shape[1]
        minDim = min(w, h)
        maxDim = max(w, h)

        scale = targetSize / minDim
        if scale * maxDim > maxSize:
            scale = maxSize / maxDim

        return scale


    def openImage(self):
        self.imgName = QFileDialog.getOpenFileName(self, 'Open Image',"", "*.jpg;;*.png;;All Files(*)" )[0]
        if len(self.imgName):
            img = cv.imread(self.imgName)
            # scale = resizeImg(img)
            # img = cv.resize(img, (round(img.shape[1]*scale),round(img.shape[0]*scale)))
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

            # print(img.shape)
            # cv.imwrite('resizeImg.jpg', img)
            # img = img.copy()
            x = img.shape[1]
            y = img.shape[0]
            frame = QImage(img, x,y,QImage.Format_RGB888)
            # img = cv.imread(self.imgName, -1)
            # # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            # x = img.shape[1]
            # y = img.shape[0]
            # frame = QImage(img, x,y,QImage.Format_ARGB32)

            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            # self.item.setScale(self.zoomscale)
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.originImg.setScene(self.scene)


    def segmentation(self):
        hs = H()

        output_path = '.'.join(self.imgName.split('.')[0:-1]) + '_seg.{}'.format(self.imgName.split('.')[-1])
        time = hs.seg(self.imgName, output_path)

        print('time used : %d sec' % time)
        print('output path:'+str(output_path))

        img = cv.imread(output_path, -1)
        # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        x = img.shape[1]
        y = img.shape[0]
        frame2 = QImage(img, x, y, QImage.Format_ARGB32)

        pix = QPixmap.fromImage(frame2)
        self.item2 = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.item.setScale(self.zoomscale)
        self.scene2 = QGraphicsScene()  # 创建场景
        self.scene2.addItem(self.item2)
        self.segImg.setScene(self.scene2)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = segWindows()
    w.choosePic.clicked.connect(w.openImage)
    w.segPic.clicked.connect(w.segmentation)
    w.show()
    sys.exit(app.exec_())
