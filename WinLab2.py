# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lab2(object):
    def setupUi(self, Lab2):
        Lab2.setObjectName("Lab2")
        Lab2.resize(366, 0)
        self.label = QtWidgets.QLabel(Lab2)
        self.label.setGeometry(QtCore.QRect(20, 20, 64, 36))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.radioButton = QtWidgets.QRadioButton(Lab2)
        self.radioButton.setGeometry(QtCore.QRect(20, 70, 100, 25))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(Lab2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 90, 100, 25))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(Lab2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 110, 125, 25))
        self.radioButton_3.setObjectName("radioButton_3")
        
        self.radioButton_4 = QtWidgets.QRadioButton(Lab2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 130, 125, 25))
        self.radioButton_4.setObjectName("radioButton_4")

        self.retranslateUi(Lab2)
        QtCore.QMetaObject.connectSlotsByName(Lab2)

    def retranslateUi(self, Lab2):
        _translate = QtCore.QCoreApplication.translate
        Lab2.setWindowTitle(_translate("Lab2", "Form"))
        self.label.setText(_translate("Lab2", "Lab2"))
        self.radioButton.setText(_translate("Lab2", "CezarCipher"))
        self.radioButton_2.setText(_translate("Lab2", "AphineCipher"))
        self.radioButton_3.setText(_translate("Lab2", "Cezar with keyword"))
        self.radioButton_4.setText(_translate("Lab2", "Tricemus"))
