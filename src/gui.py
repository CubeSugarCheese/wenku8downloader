# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(791, 596)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Books = QtWidgets.QFrame(self.centralwidget)
        self.Books.setGeometry(QtCore.QRect(10, 10, 201, 551))
        self.Books.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Books.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Books.setObjectName("Books")
        self.BookList = QtWidgets.QListView(self.Books)
        self.BookList.setGeometry(QtCore.QRect(10, 10, 181, 381))
        self.BookList.setObjectName("BookList")
        self.BookID = QtWidgets.QLineEdit(self.Books)
        self.BookID.setGeometry(QtCore.QRect(10, 410, 91, 21))
        self.BookID.setObjectName("BookID")
        self.BookAdd = QtWidgets.QPushButton(self.Books)
        self.BookAdd.setGeometry(QtCore.QRect(110, 410, 71, 28))
        self.BookAdd.setObjectName("BookAdd")
        self.Bookcase = QtWidgets.QComboBox(self.Books)
        self.Bookcase.setGeometry(QtCore.QRect(10, 450, 91, 22))
        self.Bookcase.setObjectName("Bookcase")
        self.Bookcase.addItem("")
        self.Bookcase.addItem("")
        self.Bookcase.addItem("")
        self.Bookcase.addItem("")
        self.Bookcase.addItem("")
        self.Bookcase.addItem("")
        self.BookAddFromBookcase = QtWidgets.QPushButton(self.Books)
        self.BookAddFromBookcase.setGeometry(QtCore.QRect(110, 450, 71, 28))
        self.BookAddFromBookcase.setObjectName("BookAddFromBookcase")
        self.Download = QtWidgets.QPushButton(self.Books)
        self.Download.setGeometry(QtCore.QRect(110, 490, 71, 41))
        self.Download.setObjectName("Download")
        self.IsResize = QtWidgets.QCheckBox(self.Books)
        self.IsResize.setGeometry(QtCore.QRect(10, 500, 91, 19))
        self.IsResize.setObjectName("IsResize")
        self.Book = QtWidgets.QFrame(self.centralwidget)
        self.Book.setGeometry(QtCore.QRect(210, 10, 571, 401))
        self.Book.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Book.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Book.setObjectName("Book")
        self.BookInfo = QtWidgets.QFrame(self.Book)
        self.BookInfo.setGeometry(QtCore.QRect(10, 10, 551, 241))
        self.BookInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BookInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BookInfo.setObjectName("BookInfo")
        self.BookCover = QtWidgets.QLabel(self.BookInfo)
        self.BookCover.setGeometry(QtCore.QRect(20, 10, 141, 211))
        self.BookCover.setText("")
        self.BookCover.setObjectName("BookCover")
        self.BookTextInfo = QtWidgets.QTextBrowser(self.BookInfo)
        self.BookTextInfo.setEnabled(False)
        self.BookTextInfo.setGeometry(QtCore.QRect(180, 10, 361, 211))
        self.BookTextInfo.setObjectName("BookTextInfo")
        self.BookTools = QtWidgets.QFrame(self.Book)
        self.BookTools.setGeometry(QtCore.QRect(10, 260, 561, 131))
        self.BookTools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BookTools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BookTools.setObjectName("BookTools")
        self.DeleteFromList = QtWidgets.QPushButton(self.BookTools)
        self.DeleteFromList.setGeometry(QtCore.QRect(20, 20, 151, 28))
        self.DeleteFromList.setObjectName("DeleteFromList")
        self.DownloadAll = QtWidgets.QPushButton(self.BookTools)
        self.DownloadAll.setGeometry(QtCore.QRect(20, 70, 151, 28))
        self.DownloadAll.setObjectName("DownloadAll")
        self.DownloadVolumes = QtWidgets.QPushButton(self.BookTools)
        self.DownloadVolumes.setGeometry(QtCore.QRect(200, 20, 151, 28))
        self.DownloadVolumes.setObjectName("DownloadVolumes")
        self.DownloadCover = QtWidgets.QPushButton(self.BookTools)
        self.DownloadCover.setGeometry(QtCore.QRect(380, 20, 141, 28))
        self.DownloadCover.setObjectName("DownloadCover")
        self.DownloadVolume = QtWidgets.QFrame(self.BookTools)
        self.DownloadVolume.setGeometry(QtCore.QRect(190, 60, 351, 51))
        self.DownloadVolume.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DownloadVolume.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DownloadVolume.setObjectName("DownloadVolume")
        self.DownloadSingleVolume = QtWidgets.QPushButton(self.DownloadVolume)
        self.DownloadSingleVolume.setGeometry(QtCore.QRect(190, 10, 141, 28))
        self.DownloadSingleVolume.setObjectName("DownloadSingleVolume")
        self.Volumes = QtWidgets.QComboBox(self.DownloadVolume)
        self.Volumes.setGeometry(QtCore.QRect(10, 10, 151, 22))
        self.Volumes.setObjectName("Volumes")
        self.Log = QtWidgets.QFrame(self.centralwidget)
        self.Log.setGeometry(QtCore.QRect(210, 410, 571, 151))
        self.Log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Log.setObjectName("Log")
        self.Logs = QtWidgets.QTextBrowser(self.Log)
        self.Logs.setEnabled(False)
        self.Logs.setGeometry(QtCore.QRect(0, 0, 571, 151))
        self.Logs.setObjectName("Logs")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Wenku8Downloader"))
        self.BookAdd.setText(_translate("mainWindow", "添加"))
        self.Bookcase.setItemText(0, _translate("mainWindow", "默认书架"))
        self.Bookcase.setItemText(1, _translate("mainWindow", "第一组书架"))
        self.Bookcase.setItemText(2, _translate("mainWindow", "第二组书架"))
        self.Bookcase.setItemText(3, _translate("mainWindow", "第三组书架"))
        self.Bookcase.setItemText(4, _translate("mainWindow", "第四组书架"))
        self.Bookcase.setItemText(5, _translate("mainWindow", "第五组书架"))
        self.BookAddFromBookcase.setText(_translate("mainWindow", "导入"))
        self.Download.setText(_translate("mainWindow", "下载"))
        self.IsResize.setText(_translate("mainWindow", "图片缩放"))
        self.BookTextInfo.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.DeleteFromList.setText(_translate("mainWindow", "从下载列表中删除"))
        self.DownloadAll.setText(_translate("mainWindow", "下载全本"))
        self.DownloadVolumes.setText(_translate("mainWindow", "下载分卷"))
        self.DownloadCover.setText(_translate("mainWindow", "下载封面"))
        self.DownloadSingleVolume.setText(_translate("mainWindow", "下载单卷"))
