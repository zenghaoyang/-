# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '摄像头实时.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"QWidget {\n"
"border-image:url(C:/Users/123/Desktop/ruangong/MaskDetect-YOLOv4-PyTorch-master/pyqt5/背景.jpeg);\n"
"}\n"
"\n"
"#下面的防止背景干扰其他控件\n"
"QTextBrowser {\n"
"border-image:url();\n"
"}\n"
"QLineEdit {\n"
"border-image:url();\n"
"}\n"
"QComboBox {\n"
"border-image:url();\n"
"}\n"
"QLabel {\n"
"border-image:url();\n"
"}\n"
"QPushButton {\n"
"border-image:url();\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labresult2 = QtWidgets.QLabel(self.centralwidget)
        self.labresult2.setText("")
        self.labresult2.setObjectName("labresult2")
        self.verticalLayout.addWidget(self.labresult2)
        self.btnopencamera2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnopencamera2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:blue;\n"
"color:#ffffff\n"
"font:75 13pt \"宋体\"\n"
"}")
        self.btnopencamera2.setObjectName("btnopencamera2")
        self.verticalLayout.addWidget(self.btnopencamera2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")

        self.retranslateUi(MainWindow)
        self.btnopencamera2.clicked.connect(MainWindow.btnopencamera2_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "16小组口罩识别系统"))
        self.btnopencamera2.setText(_translate("MainWindow", "打 开 摄 像 头"))
        self.action1.setText(_translate("MainWindow", "摄像头实时检测"))
        self.action2.setText(_translate("MainWindow", "摄像头拍照检测"))
        self.action3.setText(_translate("MainWindow", "本地照片检测"))
        self.action_4.setText(_translate("MainWindow", "本地视频检测"))