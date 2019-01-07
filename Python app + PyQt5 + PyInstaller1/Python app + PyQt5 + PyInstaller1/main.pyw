# -*- coding: utf-8 -*-
import win32api
import win32con
win32api.keybd_event(win32con.SHIFT_PRESSED, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
import sys,time, win32com.client  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets,QtCore
import gui as design

class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.clean.clicked.connect(self.Enter.clear) # clicked-ивент, clear-обработчик(слот)
        self.start.clicked.connect(self.moder)
        self.shell=win32com.client.Dispatch("WScript.Shell")
    def moder(self):
        text=self.Enter.toPlainText()
        if self.first.isChecked():
            self.INput(text) # Режим ввода
        else:
            self.TREINER(text) # Режим тренажёра
    def KeyPress(self,char_):
        self.shell.SendKeys(char_)

    def TREINER(self,text):
        print("Трейнер получил:",text)
    def INput(self,text):
        saver=[]
        storer=text.split("\n")
        for k in storer:
            k1=[]
            end=k.find("|end|")
            k1.append(k[0:end])
            k1.append(int(k[k.find("x",end)+1:k.find(";",end)]))
            k1.append(float(k[k.find(";",end)+1:k.rfind(";",end)]))
            saver.append(k1)
        for k in saver:
            repeat=k[1]
            forma=list(k[0])
            while repeat>0:
                for s in forma:
                    self.KeyPress(s)
                    time.sleep(k[2])
                repeat=repeat-1
            
             
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()