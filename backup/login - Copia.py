# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 446)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 531, 411))
        self.widget.setStyleSheet("background-color: rgb(29, 92, 132);\n"
"border-radius:20px;")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 260, 311, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(62, 62, 62);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 155, 255);\n"
"padding-bottom:7px")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 220, 311, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(62, 62, 62);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 155, 255);\n"
"padding-bottom:7px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(110, 300, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(66, 199, 255, 100), stop:1 rgba(255, 255, 255, 100));\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(220, 100, 151, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: 0")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Digite a senha"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Usuario"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "???"))
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())