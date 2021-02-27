# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class VisualizationWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        MainWindow.setToolTipDuration(4)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonDone = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDone.setGeometry(QtCore.QRect(460, 420, 113, 32))
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 291, 31))
        self.label.setObjectName("label")
        self.checkBoxDot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxDot.setGeometry(QtCore.QRect(70, 229, 163, 20))
        self.checkBoxDot.setToolTipDuration(0)
        self.checkBoxDot.setObjectName("checkBoxDot")
        self.checkBoxHeatmap = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxHeatmap.setGeometry(QtCore.QRect(70, 195, 125, 20))
        self.checkBoxHeatmap.setObjectName("checkBoxHeatmap")
        self.checkBoxLinear = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxLinear.setGeometry(QtCore.QRect(70, 263, 224, 20))
        self.checkBoxLinear.setObjectName("checkBoxLinear")
        self.checkBoxLog = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxLog.setGeometry(QtCore.QRect(70, 365, 278, 20))
        self.checkBoxLog.setObjectName("checkBoxLog")
        self.checkBoxCorr = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxCorr.setGeometry(QtCore.QRect(70, 161, 283, 20))
        self.checkBoxCorr.setObjectName("checkBoxCorr")
        self.checkBoxPie = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxPie.setGeometry(QtCore.QRect(70, 331, 175, 20))
        self.checkBoxPie.setObjectName("checkBoxPie")
        self.checkBoxBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxBox.setGeometry(QtCore.QRect(70, 297, 300, 20))
        self.checkBoxBox.setObjectName("checkBoxBox")
        self.checkBoxHist = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxHist.setGeometry(QtCore.QRect(70, 127, 300, 20))
        self.checkBoxHist.setObjectName("checkBoxHist")
        self.checkBoxScatter = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxScatter.setGeometry(QtCore.QRect(70, 93, 356, 20))
        self.checkBoxScatter.setObjectName("checkBoxScatter")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Визуализация"))
        self.pushButtonDone.setText(_translate("MainWindow", "Завершить"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Выбор графиков для реализации</span></p></body></html>"))
        self.checkBoxDot.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Это тул тип типочек молодой цыганенок я за тобой бегал месяц мразота</p></body></html>"))
        self.checkBoxDot.setText(_translate("MainWindow", "Точечная диаграмма "))
        self.checkBoxHeatmap.setText(_translate("MainWindow", "Тепловая карта"))
        self.checkBoxLinear.setText(_translate("MainWindow", "График линейной зависимости"))
        self.checkBoxLog.setText(_translate("MainWindow", "График логарифмической зависимости"))
        self.checkBoxCorr.setText(_translate("MainWindow", "матрица корреляций(в численном виде)"))
        self.checkBoxPie.setText(_translate("MainWindow", "Круговая диаграмма"))
        self.checkBoxBox.setText(_translate("MainWindow", "график ящик с усами(диаграмма размаха)"))
        self.checkBoxHist.setText(_translate("MainWindow", "гистограмма/столбцовая диаграмма"))
        self.checkBoxScatter.setText(_translate("MainWindow", "матрица корреляций(в виде диаграммы рассеяния)"))
