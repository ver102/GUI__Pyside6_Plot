# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testTkUPQE.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1100, 700)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"")
        self.comBox = QComboBox(Dialog)
        self.comBox.setObjectName(u"comBox")
        self.comBox.setGeometry(QRect(60, 80, 150, 30))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.comBox.setFont(font1)
        self.comBox_2 = QComboBox(Dialog)
        self.comBox_2.setObjectName(u"comBox_2")
        self.comBox_2.setGeometry(QRect(240, 80, 150, 30))
        self.comBox_2.setFont(font1)
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(610, 50, 80, 30))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(610, 90, 80, 30))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.input_path = QLineEdit(Dialog)
        self.input_path.setObjectName(u"input_path")
        self.input_path.setGeometry(QRect(700, 50, 280, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.input_path.setFont(font2)
        self.save_path = QLineEdit(Dialog)
        self.save_path.setObjectName(u"save_path")
        self.save_path.setGeometry(QRect(700, 90, 280, 30))
        self.save_path.setFont(font2)
        self.input_find = QPushButton(Dialog)
        self.input_find.setObjectName(u"input_find")
        self.input_find.setGeometry(QRect(980, 50, 50, 30))
        self.input_find.setLayoutDirection(Qt.LeftToRight)
        self.input_find.setAutoFillBackground(False)
        self.input_find.setFlat(False)
        self.save_find = QPushButton(Dialog)
        self.save_find.setObjectName(u"save_find")
        self.save_find.setGeometry(QRect(980, 90, 50, 30))
        self.save_find.setAutoFillBackground(False)
        self.save_find.setFlat(False)
        self.move_lb = QLabel(Dialog)
        self.move_lb.setObjectName(u"move_lb")
        self.move_lb.setGeometry(QRect(300, 140, 100, 30))
        self.move_lb.setStyleSheet(u"")
        self.move_lb.setFrameShape(QFrame.NoFrame)
        self.move_lb.setFrameShadow(QFrame.Plain)
        self.move_lb.setAlignment(Qt.AlignCenter)
        self.Exe = QPushButton(Dialog)
        self.Exe.setObjectName(u"Exe")
        self.Exe.setGeometry(QRect(60, 140, 100, 30))
        self.Exe.setLayoutDirection(Qt.LeftToRight)
        self.Exe.setAutoFillBackground(False)
        self.Exe.setFlat(False)
        self.Stop = QPushButton(Dialog)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setGeometry(QRect(170, 140, 100, 30))
        self.Stop.setLayoutDirection(Qt.LeftToRight)
        self.Stop.setAutoFillBackground(False)
        self.Stop.setFlat(False)
        self.para1 = QLineEdit(Dialog)
        self.para1.setObjectName(u"para1")
        self.para1.setGeometry(QRect(970, 210, 90, 30))
        self.para1.setFont(font2)
        self.para2 = QLineEdit(Dialog)
        self.para2.setObjectName(u"para2")
        self.para2.setGeometry(QRect(969, 260, 91, 30))
        self.para2.setFont(font2)
        self.para4 = QLineEdit(Dialog)
        self.para4.setObjectName(u"para4")
        self.para4.setGeometry(QRect(969, 360, 91, 30))
        self.para4.setFont(font2)
        self.para3 = QLineEdit(Dialog)
        self.para3.setObjectName(u"para3")
        self.para3.setGeometry(QRect(969, 310, 91, 30))
        self.para3.setFont(font2)
        self.txt1 = QLabel(Dialog)
        self.txt1.setObjectName(u"txt1")
        self.txt1.setGeometry(QRect(900, 210, 80, 30))
        self.txt1.setFont(font)
        self.txt1.setAlignment(Qt.AlignCenter)
        self.txt2 = QLabel(Dialog)
        self.txt2.setObjectName(u"txt2")
        self.txt2.setGeometry(QRect(900, 260, 80, 30))
        self.txt2.setFont(font)
        self.txt2.setAlignment(Qt.AlignCenter)
        self.txt4 = QLabel(Dialog)
        self.txt4.setObjectName(u"txt4")
        self.txt4.setGeometry(QRect(900, 360, 80, 30))
        self.txt4.setFont(font)
        self.txt4.setAlignment(Qt.AlignCenter)
        self.txt3 = QLabel(Dialog)
        self.txt3.setObjectName(u"txt3")
        self.txt3.setGeometry(QRect(900, 310, 80, 30))
        self.txt3.setFont(font)
        self.txt3.setAlignment(Qt.AlignCenter)
        self.video_btn = QPushButton(Dialog)
        self.video_btn.setObjectName(u"video_btn")
        self.video_btn.setGeometry(QRect(950, 580, 0, 0))
        self.video_btn.setLayoutDirection(Qt.LeftToRight)
        self.video_btn.setAutoFillBackground(False)
        self.video_btn.setFlat(False)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 180, 861, 501))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.point_lb = QLabel(Dialog)
        self.point_lb.setObjectName(u"point_lb")
        self.point_lb.setGeometry(QRect(410, 140, 100, 30))
        self.point_lb.setStyleSheet(u"")
        self.point_lb.setFrameShape(QFrame.NoFrame)
        self.point_lb.setFrameShadow(QFrame.Plain)
        self.point_lb.setAlignment(Qt.AlignCenter)
        self.Pre_2 = QPushButton(Dialog)
        self.Pre_2.setObjectName(u"Pre_2")
        self.Pre_2.setGeometry(QRect(60, 20, 151, 30))
        self.Pre_2.setLayoutDirection(Qt.LeftToRight)
        self.Pre_2.setAutoFillBackground(False)
        self.Pre_2.setFlat(False)
        self.warn_lb = QLabel(Dialog)
        self.warn_lb.setObjectName(u"warn_lb")
        self.warn_lb.setGeometry(QRect(220, 20, 180, 30))
        self.warn_lb.setStyleSheet(u"")
        self.warn_lb.setFrameShape(QFrame.NoFrame)
        self.warn_lb.setFrameShadow(QFrame.Plain)
        self.warn_lb.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        self.input_find.setDefault(True)
        self.save_find.setDefault(True)
        self.Exe.setDefault(True)
        self.Stop.setDefault(True)
        self.video_btn.setDefault(True)
        self.Pre_2.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Input Path", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Save Path", None))
        self.input_path.setText(QCoreApplication.translate("Dialog", u"\ud3f4\ub354\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694", None))
        self.save_path.setText(QCoreApplication.translate("Dialog", u"\ud3f4\ub354\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694", None))
        self.input_find.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.save_find.setText(QCoreApplication.translate("Dialog", u"Open", None))
        self.move_lb.setText("")
        self.Exe.setText(QCoreApplication.translate("Dialog", u"View", None))
        self.Stop.setText(QCoreApplication.translate("Dialog", u"Stop", None))
        self.para1.setText("")
        self.para2.setText("")
        self.para4.setText("")
        self.para3.setText("")
        self.txt1.setText(QCoreApplication.translate("Dialog", u"para1", None))
        self.txt2.setText(QCoreApplication.translate("Dialog", u"para2", None))
        self.txt4.setText(QCoreApplication.translate("Dialog", u"para4", None))
        self.txt3.setText(QCoreApplication.translate("Dialog", u"para3", None))
        self.video_btn.setText(QCoreApplication.translate("Dialog", u"Play", None))
        self.point_lb.setText("")
        self.Pre_2.setText(QCoreApplication.translate("Dialog", u"Pre-process", None))
        self.warn_lb.setText("")
    # retranslateUi

