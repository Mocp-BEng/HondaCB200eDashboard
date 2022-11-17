# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(800, 800)
        SplashScreen.setMinimumSize(QSize(800, 800))
        SplashScreen.setMaximumSize(QSize(800, 800))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.container)
        self.circle_bg.setObjectName(u"circle_bg")
        self.circle_bg.setStyleSheet(u"QFrame{\n"
"	background-color:#282a36;\n"
"	color:#f8f8f2;\n"
"	border-radius: 360px;\n"
"}")
        self.circle_bg.setFrameShape(QFrame.NoFrame)
        self.circle_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.texts = QFrame(self.circle_bg)
        self.texts.setObjectName(u"texts")
        self.texts.setMaximumSize(QSize(16777215, 500))
        self.texts.setStyleSheet(u"QFrame{\n"
"	background-color:none;\n"
"	color:#f8f8f2;\n"
"	border-radius: 0px;\n"
"}")
        self.texts.setFrameShape(QFrame.StyledPanel)
        self.texts.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.texts)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(310, 320, 91, 101))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.label_6 = QLabel(self.texts)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 230, 49, 16))
        self.label_7 = QLabel(self.texts)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(510, 230, 49, 16))
        self.label_8 = QLabel(self.texts)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 110, 91, 16))

        self.verticalLayout_2.addWidget(self.texts)


        self.horizontalLayout.addWidget(self.circle_bg)


        self.verticalLayout.addWidget(self.container)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashScreen", u"Motor", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"100\u00b0C", None))
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"Batterie", None))
        self.label_5.setText(QCoreApplication.translate("SplashScreen", u"100\u00b0C", None))
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"Temperatur", None))
        self.label_6.setText(QCoreApplication.translate("SplashScreen", u"A", None))
        self.label_7.setText(QCoreApplication.translate("SplashScreen", u"rpm", None))
        self.label_8.setText(QCoreApplication.translate("SplashScreen", u"Honda CB200e", None))
    # retranslateUi

