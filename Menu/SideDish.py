# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SideDish.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SideDish(object):
    def SideDishUi(self, SideDish):
        SideDish.setObjectName("SideDish")
        SideDish.resize(623, 280)
        self.centralwidget = QtWidgets.QWidget(SideDish)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 60, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SideDish.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SideDish)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName("menubar")
        SideDish.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SideDish)
        self.statusbar.setObjectName("statusbar")
        SideDish.setStatusBar(self.statusbar)

        self.retranslateUi(SideDish)
        QtCore.QMetaObject.connectSlotsByName(SideDish)

    def retranslateUi(self, SideDish):
        _translate = QtCore.QCoreApplication.translate
        SideDish.setWindowTitle(_translate("SideDish", "MainWindow"))
        self.label.setText(_translate("SideDish", "Side Dish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SideDish = QtWidgets.QMainWindow()
    ui = Ui_SideDish()
    ui.setupUi(SideDish)
    SideDish.show()
    sys.exit(app.exec_())

