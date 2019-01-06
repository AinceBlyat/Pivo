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
        MainWindow.resize(552, 380)
        MainWindow.setMinimumSize(QtCore.QSize(552, 380))
        MainWindow.setMaximumSize(QtCore.QSize(552, 380))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Enter = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(30, 30, 491, 171))
        self.Enter.setObjectName("Enter")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(340, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(340, 320, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.clean = QtWidgets.QPushButton(self.centralwidget)
        self.clean.setGeometry(QtCore.QRect(30, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.clean.setFont(font)
        self.clean.setObjectName("clean")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(340, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pause.setFont(font)
        self.pause.setObjectName("pause")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 280, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.first = QtWidgets.QRadioButton(self.groupBox)
        self.first.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.first.setChecked(True)
        self.first.setObjectName("first")
        self.second = QtWidgets.QRadioButton(self.groupBox)
        self.second.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.second.setObjectName("second")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 220, 151, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/data/Pivasss.jpg"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пиво"))
        self.Enter.setPlainText(_translate("MainWindow", "Тут ваша строка|end|x1;0.5;"))
        self.start.setText(_translate("MainWindow", "Старт"))
        self.stop.setText(_translate("MainWindow", "Стоп"))
        self.clean.setText(_translate("MainWindow", "Очистка"))
        self.pause.setText(_translate("MainWindow", "Пауза"))
        self.groupBox.setTitle(_translate("MainWindow", "Режимы"))
        self.first.setText(_translate("MainWindow", "Ввод"))
        self.second.setText(_translate("MainWindow", "Тренажёр"))

import resurs_rc
