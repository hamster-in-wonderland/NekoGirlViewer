# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nekomfqZBf.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(609, 478)
        icon = QIcon()
        icon.addFile(u":/icon/ciallo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.ciallo = QAction(MainWindow)
        self.ciallo.setObjectName(u"ciallo")
        self.SavePath = QAction(MainWindow)
        self.SavePath.setObjectName(u"SavePath")
        self.About_Hamster_label = QAction(MainWindow)
        self.About_Hamster_label.setObjectName(u"About_Hamster_label")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.webViewer = QWebEngineView(self.centralwidget)
        self.webViewer.setObjectName(u"webViewer")
        self.webViewer.setGeometry(QRect(12, 0, 409, 433))
        self.webViewer.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.webViewer.setMouseTracking(False)
        self.webViewer.setUrl(QUrl(u"about:blank"))
        self.lnto = QLabel(self.centralwidget)
        self.lnto.setObjectName(u"lnto")
        self.lnto.setGeometry(QRect(432, 0, 161, 121))
        self.textOutputer = QTextBrowser(self.centralwidget)
        self.textOutputer.setObjectName(u"textOutputer")
        self.textOutputer.setGeometry(QRect(432, 130, 169, 192))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(432, 348, 174, 71))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.last = QPushButton(self.layoutWidget)
        self.last.setObjectName(u"last")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.last)

        self.next = QPushButton(self.layoutWidget)
        self.next.setObjectName(u"next")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.next)

        self.save = QPushButton(self.layoutWidget)
        self.save.setObjectName(u"save")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.save)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 609, 33))
        self.menuneko = QMenu(self.menubar)
        self.menuneko.setObjectName(u"menuneko")
        self.About = QMenu(self.menubar)
        self.About.setObjectName(u"About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuneko.menuAction())
        self.menubar.addAction(self.About.menuAction())
        self.menuneko.addAction(self.SavePath)
        self.menuneko.addSeparator()
        self.menuneko.addAction(self.ciallo)
        self.About.addAction(self.About_Hamster_label)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NekoViewer", None))
        self.ciallo.setText(QCoreApplication.translate("MainWindow", u"Hamster \u55b5~", None))
        self.SavePath.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4fdd\u5b58\u8def\u5f84", None))
        self.About_Hamster_label.setText(QCoreApplication.translate("MainWindow", u"About Hamster", None))
        self.lnto.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NekoViewer</p><p align=\"right\">By Hamster \u55b5~</p><p><br/></p><p>version 3.1.1</p><p><br/></p><p>2026.7.18</p></body></html>", None))
        self.last.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u56fe\u50cf", None))
        self.menuneko.setTitle(QCoreApplication.translate("MainWindow", u"Neko", None))
        self.About.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

