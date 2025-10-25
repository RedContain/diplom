# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReportWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QSizePolicy,
    QTabWidget, QTextEdit, QWidget)

class Ui_reportWindow(object):
    def setupUi(self, reportWindow):
        if not reportWindow.objectName():
            reportWindow.setObjectName(u"reportWindow")
        reportWindow.resize(1197, 699)
        self.action = QAction(reportWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(reportWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(reportWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(reportWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(reportWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(reportWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(reportWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(reportWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_9 = QAction(reportWindow)
        self.action_9.setObjectName(u"action_9")
        self.action_10 = QAction(reportWindow)
        self.action_10.setObjectName(u"action_10")
        self.action_11 = QAction(reportWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_12 = QAction(reportWindow)
        self.action_12.setObjectName(u"action_12")
        self.action_13 = QAction(reportWindow)
        self.action_13.setObjectName(u"action_13")
        self.centralwidget = QWidget(reportWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(10, 40, 681, 631))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 391, 111))
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 71, 81))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(80, 20, 301, 41))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 130, 401, 221))
        self.gridLayoutWidget_3 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 20, 381, 41))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 70, 381, 73))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.gridLayoutWidget_4)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_4.addWidget(self.textEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.groupBox_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setGeometry(QRect(-10, -160, 681, 631))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 10, 401, 111))
        self.gridLayoutWidget_5 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 20, 71, 81))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 1, 0, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(80, 20, 311, 41))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_8.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 130, 391, 221))
        self.gridLayoutWidget_7 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 20, 371, 41))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.gridLayoutWidget_7)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_9.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.gridLayoutWidget_8 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 70, 371, 95))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.textEdit_3 = QTextEdit(self.gridLayoutWidget_8)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.gridLayout_10.addWidget(self.textEdit_3, 1, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_8)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self.gridLayoutWidget_9 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 170, 371, 41))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.gridLayoutWidget_9)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_11.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 20, 1171, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 0, 1171, 23))
        self.progressBar.setValue(24)
        reportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(reportWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1197, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        reportWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menu_4.addAction(self.action_9)
        self.menu_4.addAction(self.action_10)
        self.menu_5.addAction(self.action_11)
        self.menu_5.addAction(self.action_12)
        self.menu_5.addAction(self.action_13)

        self.retranslateUi(reportWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(reportWindow)
    # setupUi

    def retranslateUi(self, reportWindow):
        reportWindow.setWindowTitle(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.action.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.action_2.setText(QCoreApplication.translate("reportWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.action_3.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.action_4.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.action_5.setText(QCoreApplication.translate("reportWindow", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u043e\u0447\u0442\u0435\u0442\u043e\u0432", None))
        self.action_6.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.action_7.setText(QCoreApplication.translate("reportWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.action_8.setText(QCoreApplication.translate("reportWindow", u"\u0422\u0435\u043c\u0430", None))
        self.action_9.setText(QCoreApplication.translate("reportWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f", None))
        self.action_10.setText(QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0435", None))
        self.action_11.setText(QCoreApplication.translate("reportWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0447\u0435\u0435 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u0435", None))
        self.action_12.setText(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.action_13.setText(QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("reportWindow", u"\u041b\u0438\u0446\u043e, \u0437\u0430\u043f\u043e\u043b\u043d\u044f\u044e\u0449\u0438\u0435\u0435 \u043e\u0442\u0447\u0435\u0442:", None))
        self.label.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0418\u041e:", None))
        self.label_2.setText(QCoreApplication.translate("reportWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438:", None))
        self.label_3.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430:", None))
        self.label_4.setText(QCoreApplication.translate("reportWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("reportWindow", u"\u041b\u0438\u0446\u043e, \u0437\u0430\u043f\u043e\u043b\u043d\u044f\u044e\u0449\u0438\u0435\u0435 \u043e\u0442\u0447\u0435\u0442:", None))
        self.label_7.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0418\u041e:", None))
        self.label_8.setText(QCoreApplication.translate("reportWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438:", None))
        self.label_9.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430:", None))
        self.label_10.setText(QCoreApplication.translate("reportWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430:", None))
        self.label_11.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0440\u0438\u043a\u0430\u0437\u0430:*", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u0430\u0438\u0446\u0438\u044f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("reportWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u0430\u0438\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("reportWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.menu.setTitle(QCoreApplication.translate("reportWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_4.setTitle(QCoreApplication.translate("reportWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu_5.setTitle(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u044f", None))
    # retranslateUi

