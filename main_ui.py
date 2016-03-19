# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\1\1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(720, 600)
        # Create main menu
        # Form.menuBar()
        # mainMenu = Form.menuBar()
        # fileMenu = mainMenu.addMenu('&exit')
        # Add exit button
        ext_ac = QtGui.QAction("info", self)
        ext_ac.setShortcut('Ctrl+Q')
        ext_ac.setStatusTip('Exit application')

        # mainmenu = self.menubar()
        # infomenu = mainmenu.addmenu('&info')
        #ext_ac.triggered.connect(self.)
        #fileMenu.addAction(exitButton)



        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 180, 500, 260))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        #self.pushButton = QtGui.QPushButton(Form)
        #self.pushButton.setGeometry(QtCore.QRect(470, 750, 100, 25))
        #self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #self.pushButton.setIcon(QtGui.QIcon('ok.png'))

        self.msg = QtGui.QMessageBox(Form)
        self.msg.resize(800, 800)

        #self.infoButton = QtGui.QPushButton(Form)
        #self.infoButton.setGeometry(QtCore.QRect(350, 20, 100, 50))
        #self.infoButton.setObjectName(_fromUtf8("infoButton"))
        #self.infoButton.setIcon(QtGui.QIcon('info.png'))
        #self.infoButton.setText('Автор')

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 110, 120, 13))
        self.label.setObjectName(_fromUtf8("label"))





        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        #self.pushButton.setText(_translate("Form", "PushButton", None))
        self.label.setText(_translate("Form", "TextLabel", None))


