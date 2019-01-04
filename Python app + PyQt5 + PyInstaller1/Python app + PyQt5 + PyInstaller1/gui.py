# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setMinimumSize(QtCore.QSize(700, 400))
        MainWindow.setMaximumSize(QtCore.QSize(700, 400))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Enter = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(30, 30, 411, 151))
        self.Enter.setObjectName("Enter")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 340, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 340, 181, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 80, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 200, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пиво"))
        self.pushButton.setText(_translate("MainWindow", "старт"))
        self.pushButton_2.setText(_translate("MainWindow", "стоп"))
        self.pushButton_3.setText(_translate("MainWindow", "очистка"))
        self.pushButton_4.setText(_translate("MainWindow", "пауза"))
        self.groupBox.setTitle(_translate("MainWindow", "Режимы"))
        self.radioButton_2.setText(_translate("MainWindow", "Ввод"))
        self.radioButton.setText(_translate("MainWindow", "Тренажёр"))

