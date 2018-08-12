# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MainCourse import Ui_MainMenu
from SideDish import Ui_SideDish
from Dessert import Ui_Dessert
from Drinks import Ui_Drinks
class Ui_MainWin(object):

    def openMainCourse(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_MainMenu()
    	self.ui.setupUi(self.window)
    	self.window.show()
    def openSideDish(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_SideDish()
    	self.ui.SideDishUi(self.window)
    	self.window.show()
    def openDessert(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_Dessert()
    	self.ui.setupUi(self.window)
    	self.window.show()
    def openDrinks(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_Drinks()
    	self.ui.setupUi(self.window)
    	self.window.show()

    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(627, 282)
        self.centralwidget = QtWidgets.QWidget(MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Plantagenet Cherokee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openMainCourse)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 30, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Plantagenet Cherokee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openSideDish)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 30, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Plantagenet Cherokee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.openDessert)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 30, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Plantagenet Cherokee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.openDrinks)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 170, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Plantagenet Cherokee")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 21))
        self.menubar.setObjectName("menubar")
        MainWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWin)
        self.statusbar.setObjectName("statusbar")
        MainWin.setStatusBar(self.statusbar)

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "MainWindow"))
        self.pushButton.setText(_translate("MainWin", "Main Course"))
        self.pushButton_2.setText(_translate("MainWin", "Side Dish"))
        self.pushButton_3.setText(_translate("MainWin", "Dessert"))
        self.pushButton_4.setText(_translate("MainWin", "Drinks"))
        self.pushButton_5.setText(_translate("MainWin", "Order"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())

