# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
def mmedian(a, l, r):
    n = r - l + 1
    n = (n + 1) // 2 - 1
    return (n + l)
def IQR(a,n):
    a.sort()
    mid_index = mmedian(a, 0, n)
    Q1 = a[mmedian(a, 0, mid_index)]
    Q3 = a[mmedian(a, mid_index + 1, n)]
    return (Q3 - Q1)
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import statistics
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 1315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 0, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(24)
        font.setItalic(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setLineWidth(18)
        self.label.setObjectName("label")
        self.combo_selectProblem = QtWidgets.QComboBox(self.centralwidget)
        self.combo_selectProblem.setGeometry(QtCore.QRect(150, 70, 111, 22))
        self.combo_selectProblem.setEditable(False)
        self.combo_selectProblem.setCurrentText("")
        self.combo_selectProblem.setObjectName("combo_selectProblem")
        self.combo_selectProblem.addItem("")
        self.combo_selectProblem.setItemText(0, "")
        self.combo_selectProblem.addItem("")
        self.combo_selectProblem.addItem("")
        self.combo_selectProblem.addItem("")
        self.combo_selectProblem.addItem("")
        self.combo_selectProblem.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 72, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget_pie_par = QtWidgets.QWidget(self.centralwidget)
        self.widget_pie_par.setGeometry(QtCore.QRect(0, 170, 821, 111))
        self.widget_pie_par.setObjectName("widget_pie_par")
        self.widget_pie_par.hide()
        self.txt_nameofdata = QtWidgets.QLineEdit(self.widget_pie_par)
        self.txt_nameofdata.setGeometry(QtCore.QRect(180, 20, 301, 20))
        self.txt_nameofdata.setObjectName("txt_nameofdata")
        self.btn_okpiepar = QtWidgets.QPushButton(self.widget_pie_par)
        self.btn_okpiepar.setGeometry(QtCore.QRect(610, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_okpiepar.setFont(font)
        self.btn_okpiepar.setObjectName("btn_okpiepar")
        self.label_4 = QtWidgets.QLabel(self.widget_pie_par)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comb_pie_par = QtWidgets.QComboBox(self.widget_pie_par)
        self.comb_pie_par.setGeometry(QtCore.QRect(680, 30, 131, 22))
        self.comb_pie_par.setObjectName("comb_pie_par")
        self.comb_pie_par.addItem("")
        self.comb_pie_par.setItemText(0, "")
        self.comb_pie_par.addItem("")
        self.comb_pie_par.addItem("")
        self.txt_amountofdatapie = QtWidgets.QLineEdit(self.widget_pie_par)
        self.txt_amountofdatapie.setGeometry(QtCore.QRect(180, 70, 301, 20))
        self.txt_amountofdatapie.setObjectName("txt_amountofdatapie")
        self.label_5 = QtWidgets.QLabel(self.widget_pie_par)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_pie_par)
        self.label_6.setGeometry(QtCore.QRect(500, 30, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.widget_iqr = QtWidgets.QWidget(self.centralwidget)
        self.widget_iqr.setGeometry(QtCore.QRect(0, 170, 821, 281))
        #self.btn_okiqr.hide()
        self.widget_iqr.setObjectName("widget_iqr")
        self.widget_iqr.hide()
        self.label_16 = QtWidgets.QLabel(self.widget_iqr)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.txt_nameofdataiqr = QtWidgets.QLineEdit(self.widget_iqr)
        self.txt_nameofdataiqr.setGeometry(QtCore.QRect(180, 20, 371, 20))
        self.txt_nameofdataiqr.setObjectName("txt_nameofdataiqr")
        self.btn_okiqr = QtWidgets.QPushButton(self.widget_iqr)
        self.btn_okiqr.setGeometry(QtCore.QRect(610, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_okiqr.setFont(font)
        self.btn_okiqr.setObjectName("btn_okiqr")
        self.label_17 = QtWidgets.QLabel(self.widget_iqr)
        self.label_17.setGeometry(QtCore.QRect(40, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lbl_mode_2 = QtWidgets.QLabel(self.widget_iqr)
        self.lbl_mode_2.setGeometry(QtCore.QRect(160, 90, 47, 13))
        self.lbl_mode_2.setText("")
        self.lbl_mode_2.setObjectName("lbl_mode_2")
        self.lbl_midean_2 = QtWidgets.QLabel(self.widget_iqr)
        self.lbl_midean_2.setGeometry(QtCore.QRect(160, 140, 47, 13))
        self.lbl_midean_2.setText("")
        self.lbl_midean_2.setObjectName("lbl_midean_2")
        self.lbl_mean_2 = QtWidgets.QLabel(self.widget_iqr)
        self.lbl_mean_2.setGeometry(QtCore.QRect(160, 190, 47, 13))
        self.lbl_mean_2.setText("")
        self.lbl_mean_2.setObjectName("lbl_mean_2")
        self.label_22 = QtWidgets.QLabel(self.widget_iqr)
        self.label_22.setGeometry(QtCore.QRect(40, 170, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_iqr)
        self.label_23.setGeometry(QtCore.QRect(40, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.widget_iqr)
        self.label_24.setGeometry(QtCore.QRect(40, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.lbl_iqr = QtWidgets.QLabel(self.widget_iqr)
        self.lbl_iqr.setGeometry(QtCore.QRect(100, 240, 47, 13))
        self.lbl_iqr.setText("")
        self.lbl_iqr.setObjectName("lbl_iqr")
        self.label_26 = QtWidgets.QLabel(self.widget_iqr)
        self.label_26.setGeometry(QtCore.QRect(20, 240, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.lbl_kindofiqr = QtWidgets.QLabel(self.widget_iqr)
        self.lbl_kindofiqr.setGeometry(QtCore.QRect(160, 260, 47, 13))
        self.lbl_kindofiqr.setText("")
        self.lbl_kindofiqr.setObjectName("lbl_kindofiqr")
        self.widget_mode = QtWidgets.QWidget(self.centralwidget)
        self.widget_mode.setGeometry(QtCore.QRect(0, 170, 821, 211))
        self.widget_mode.setObjectName("widget_mode")
        self.widget_mode.hide()

        self.label_14 = QtWidgets.QLabel(self.widget_mode)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.txt_nameofdatamode = QtWidgets.QLineEdit(self.widget_mode)
        self.txt_nameofdatamode.setGeometry(QtCore.QRect(180, 20, 371, 20))
        self.txt_nameofdatamode.setObjectName("txt_nameofdatamode")
        self.btn_okmode = QtWidgets.QPushButton(self.widget_mode)
        self.btn_okmode.setGeometry(QtCore.QRect(610, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_okmode.setFont(font)
        self.btn_okmode.setObjectName("btn_okmode")
        self.label_13 = QtWidgets.QLabel(self.widget_mode)
        self.label_13.setGeometry(QtCore.QRect(40, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lbl_mode = QtWidgets.QLabel(self.widget_mode)
        self.lbl_mode.setGeometry(QtCore.QRect(160, 90, 47, 13))
        self.lbl_mode.setText("")
        self.lbl_mode.setObjectName("lbl_mode")
        self.lbl_midean = QtWidgets.QLabel(self.widget_mode)
        self.lbl_midean.setGeometry(QtCore.QRect(160, 140, 47, 13))
        self.lbl_midean.setText("")
        self.lbl_midean.setObjectName("lbl_midean")
        self.lbl_mean = QtWidgets.QLabel(self.widget_mode)
        self.lbl_mean.setGeometry(QtCore.QRect(160, 190, 47, 13))
        self.lbl_mean.setText("")
        self.lbl_mean.setObjectName("lbl_mean")
        self.label_20 = QtWidgets.QLabel(self.widget_mode)
        self.label_20.setGeometry(QtCore.QRect(40, 170, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_mode)
        self.label_21.setGeometry(QtCore.QRect(40, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.widget_R = QtWidgets.QWidget(self.centralwidget)
        self.widget_R.setGeometry(QtCore.QRect(0, 170, 821, 450))
        self.widget_R.setObjectName("widget_R")
        self.widget_R.hide()

        self.tableWidget_r = QtWidgets.QTableWidget(self.widget_R)
        self.tableWidget_r.setGeometry(QtCore.QRect(300, 130, 501, 301))
        self.tableWidget_r.setObjectName("tableWidget_r")
        self.tableWidget_r.setColumnCount(0)
        self.tableWidget_r.setRowCount(0)
        self.label_25 = QtWidgets.QLabel(self.widget_R)
        self.label_25.setGeometry(QtCore.QRect(20, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_18 = QtWidgets.QLabel(self.widget_R)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.txt_nameofdatax = QtWidgets.QLineEdit(self.widget_R)
        self.txt_nameofdatax.setGeometry(QtCore.QRect(190, 20, 371, 20))
        self.txt_nameofdatax.setObjectName("txt_nameofdatax")
        self.btn_okr = QtWidgets.QPushButton(self.widget_R)
        self.btn_okr.setGeometry(QtCore.QRect(650, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_okr.setFont(font)
        self.btn_okr.setObjectName("btn_okr")
        self.txt_nameofdatay = QtWidgets.QLineEdit(self.widget_R)
        self.txt_nameofdatay.setGeometry(QtCore.QRect(190, 70, 371, 20))
        self.txt_nameofdatay.setObjectName("txt_nameofdatay")
        self.label_19 = QtWidgets.QLabel(self.widget_R)
        self.label_19.setGeometry(QtCore.QRect(20, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lb_r = QtWidgets.QLabel(self.widget_R)
        self.lb_r.setGeometry(QtCore.QRect(90, 150, 47, 13))
        self.lb_r.setText("")
        self.lb_r.setObjectName("lb_r")
        self.lb_kindofr = QtWidgets.QLabel(self.widget_R)
        self.lb_kindofr.setGeometry(QtCore.QRect(150, 190, 47, 13))
        self.lb_kindofr.setText("")
        self.lb_kindofr.setObjectName("lb_kindofr")
        self.label_27 = QtWidgets.QLabel(self.widget_R)
        self.label_27.setGeometry(QtCore.QRect(20, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.widget_hiostgram = QtWidgets.QWidget(self.centralwidget)
        self.widget_hiostgram.setGeometry(QtCore.QRect(0, 170, 831, 81))
        self.widget_hiostgram.setObjectName("widget_hiostgram")
        self.widget_hiostgram.hide()
        self.txt_nameofdatahistogram = QtWidgets.QLineEdit(self.widget_hiostgram)
        self.txt_nameofdatahistogram.setGeometry(QtCore.QRect(220, 20, 371, 20))
        self.txt_nameofdatahistogram.setObjectName("txt_nameofdatahistogram")
        self.label_15 = QtWidgets.QLabel(self.widget_hiostgram)
        self.label_15.setGeometry(QtCore.QRect(30, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btn_okhistogram = QtWidgets.QPushButton(self.widget_hiostgram)
        self.btn_okhistogram.setGeometry(QtCore.QRect(640, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_okhistogram.setFont(font)
        self.btn_okhistogram.setObjectName("btn_okhistogram")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Statistics Program"))
        self.combo_selectProblem.setItemText(1, _translate("MainWindow", "pie Chart & par Chart"))
        self.combo_selectProblem.setItemText(2, _translate("MainWindow", "Histogram"))
        self.combo_selectProblem.setItemText(3, _translate("MainWindow", "Measures of Central Tendency"))
        self.combo_selectProblem.setItemText(4, _translate("MainWindow", "Interquartile Range & Box Plot"))
        self.combo_selectProblem.currentTextChanged.connect(self.checkcombo)
        self.combo_selectProblem.setItemText(5, _translate("MainWindow", "Correlation"))
        self.label_2.setText(_translate("MainWindow", "Select Problem:"))
        self.btn_okpiepar.setText(_translate("MainWindow", "ok"))
        self.label_4.setText(_translate("MainWindow", "Enter your Data"))
        self.comb_pie_par.setItemText(1, _translate("MainWindow", "pie Chart"))
        self.comb_pie_par.setItemText(2, _translate("MainWindow", "par Chart"))
        self.label_5.setText(_translate("MainWindow", "Enter amount of Data"))
        self.label_6.setText(_translate("MainWindow", "Chosse Your Graph"))
        self.label_16.setText(_translate("MainWindow", "Enter amount of Data"))
        self.btn_okiqr.setText(_translate("MainWindow", "ok"))
        self.label_17.setText(_translate("MainWindow", "Mode:"))
        self.label_22.setText(_translate("MainWindow", "Mean:"))
        self.label_23.setText(_translate("MainWindow", "Midean:"))
        self.label_24.setText(_translate("MainWindow", "IQR:"))
        self.label_26.setText(_translate("MainWindow", "kind of IQR:"))
        self.label_14.setText(_translate("MainWindow", "Enter amount of Data"))
        self.btn_okmode.setText(_translate("MainWindow", "ok"))
        self.label_13.setText(_translate("MainWindow", "Mode:"))
        self.label_20.setText(_translate("MainWindow", "Mean:"))
        self.label_21.setText(_translate("MainWindow", "Midean:"))
        self.label_25.setText(_translate("MainWindow", "R:"))
        self.label_18.setText(_translate("MainWindow", "Enter amount of Data X"))
        self.btn_okr.setText(_translate("MainWindow", "ok"))
        self.label_19.setText(_translate("MainWindow", "Enter amount of Data Y"))
        self.label_27.setText(_translate("MainWindow", "Kind of R:"))
        self.label_15.setText(_translate("MainWindow", "Enter amount of Data"))
        self.btn_okhistogram.setText(_translate("MainWindow", "ok"))
        self.btn_okpiepar.clicked.connect(self.klick)
        self.btn_okhistogram.clicked.connect(self.klick_his)
        self.btn_okiqr.clicked.connect(self.klick_iqr)
    def checkcombo(self):
        if self.combo_selectProblem.currentText()=="pie Chart & par Chart":
            self.widget_pie_par.show()
            self.widget_hiostgram.hide()
            self.widget_mode.hide()
            self.widget_iqr.hide()
            self.widget_R.hide()

        elif self.combo_selectProblem.currentText()=="Histogram":
            self.widget_hiostgram.show()
            self.widget_pie_par.hide()
            self.widget_mode.hide()
            self.widget_iqr.hide()
            self.widget_R.hide()
        elif self.combo_selectProblem.currentText()=="Measures of Central Tendency":
            self.widget_mode.show()
            self.widget_pie_par.hide()
            self.widget_hiostgram.hide()
            self.widget_iqr.hide()
            self.widget_R.hide()
        elif self.combo_selectProblem.currentText()=="Interquartile Range & Box Plot":
            self.widget_iqr.show()
            self.widget_pie_par.hide()
            self.widget_hiostgram.hide()
            self.widget_mode.hide()
            self.widget_R.hide()
        elif self.combo_selectProblem.currentText()=="Correlation":
            self.widget_R.show()
            self.widget_pie_par.hide()
            self.widget_hiostgram.hide()
            self.widget_mode.hide()
            self.widget_iqr.hide()
    def klick(self):
        choice=self.comb_pie_par.currentText()
        txt1=self.txt_nameofdata.text()
        txt2=self.txt_amountofdatapie.text()
        word=txt1.split(",")
        amount=txt2.split(",")
        int_amout=[]
        for i in  range (0,len(amount)):
            int_amout.append(int(amount[i]))
        if(choice=="par Chart"):
            y_pos = np.arange(len(word))
            plt.bar(y_pos,int_amout, align='center', alpha=0.5)
            plt.xticks(y_pos,word)
            plt.ylabel('Usage')
            plt.title('Programming language usage')
            plt.show()
        if(choice=="pie Chart"):
            explode=[]
            for i in range (0,len(int_amout)):
                explode.append(0)
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','blue','yellow']
            plt.pie(int_amout, explode=explode, labels=word, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=140)
            plt.axis('equal')
            plt.show()
    def klick_his(self):
        choice=self.combo_selectProblem.currentText()
        amount = (self.txt_nameofdatahistogram.text()).split(",")
        int_amotnt = []
        for i in range(0, len(amount)):
            int_amotnt.append(int(amount[i]))
            num_bins = 5
            n, bins, patches = plt.hist(int_amotnt, num_bins, facecolor='blue', alpha=0.5)
            plt.show()
    def klick_iqr(self):
        amount = (self.txt_nameofdataiqr.text()).split(",")
        #print(amount[len(amount)-1])
        int_amotnt = []
        for i in range(0, len(amount)):
            int_amotnt.append(int(amount[i]))
        #mean1 = statistics.mean(int_amotnt)
        #self.lbl_mean_2.setText(str(mean1))
        #median1 = statistics.median(int_amotnt)
        #self.lbl_midean_2.setText(str(median1))
        #mode1 = statistics.mode(int_amotnt)
        #self.lbl_mode_2.setText(str(mode1))
        iqr=IQR(int_amotnt,len(int_amotnt))
        print(iqr)
        plt.boxplot(int_amotnt)
        plt.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

