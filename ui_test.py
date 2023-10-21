# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testKvBKoo.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 700)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 210, 661, 401))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.comBox = QComboBox(Dialog)
        self.comBox.setObjectName(u"comBox")
        self.comBox.setGeometry(QRect(60, 60, 120, 30))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.comBox.setFont(font1)
        self.comBox_2 = QComboBox(Dialog)
        self.comBox_2.setObjectName(u"comBox_2")
        self.comBox_2.setGeometry(QRect(200, 60, 120, 30))
        self.comBox_2.setFont(font1)
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(350, 50, 80, 30))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 90, 80, 30))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.input_path = QLineEdit(Dialog)
        self.input_path.setObjectName(u"input_path")
        self.input_path.setGeometry(QRect(440, 50, 280, 30))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.input_path.setFont(font2)
        self.save_path = QLineEdit(Dialog)
        self.save_path.setObjectName(u"save_path")
        self.save_path.setGeometry(QRect(440, 90, 280, 30))
        self.save_path.setFont(font2)
        self.input_find = QPushButton(Dialog)
        self.input_find.setObjectName(u"input_find")
        self.input_find.setGeometry(QRect(720, 50, 50, 30))
        self.input_find.setLayoutDirection(Qt.LeftToRight)
        self.input_find.setAutoFillBackground(False)
        self.input_find.setFlat(False)
        self.save_find = QPushButton(Dialog)
        self.save_find.setObjectName(u"save_find")
        self.save_find.setGeometry(QRect(720, 90, 50, 30))
        self.save_find.setAutoFillBackground(False)
        self.save_find.setFlat(False)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 650, 50, 30))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 650, 140, 30))
        self.label.setStyleSheet(u"")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 650, 120, 30))
        self.label_2.setStyleSheet(u"")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.Exe = QPushButton(Dialog)
        self.Exe.setObjectName(u"Exe")
        self.Exe.setGeometry(QRect(60, 140, 80, 30))
        self.Exe.setLayoutDirection(Qt.LeftToRight)
        self.Exe.setAutoFillBackground(False)
        self.Exe.setFlat(False)
        self.Stop = QPushButton(Dialog)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setGeometry(QRect(150, 140, 80, 30))
        self.Stop.setLayoutDirection(Qt.LeftToRight)
        self.Stop.setAutoFillBackground(False)
        self.Stop.setFlat(False)

        self.retranslateUi(Dialog)

        self.input_find.setDefault(True)
        self.save_find.setDefault(True)
        self.Exe.setDefault(True)
        self.Stop.setDefault(True)


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
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.label.setText("")
        self.label_2.setText("")
        self.Exe.setText(QCoreApplication.translate("Dialog", u"Execute", None))
        self.Stop.setText(QCoreApplication.translate("Dialog", u"Stop", None))
    # retranslateUi

