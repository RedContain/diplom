# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReportWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_reportWindow(object):
    def setupUi(self, reportWindow):
        if not reportWindow.objectName():
            reportWindow.setObjectName(u"reportWindow")
        reportWindow.resize(1909, 983)
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
        self.action_14 = QAction(reportWindow)
        self.action_14.setObjectName(u"action_14")
        self.action_15 = QAction(reportWindow)
        self.action_15.setObjectName(u"action_15")
        self.centralwidget = QWidget(reportWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 30, 1901, 911))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.groupBox_9 = QGroupBox(self.tab_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 0, 391, 111))
        self.gridLayoutWidget_25 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_25.setObjectName(u"gridLayoutWidget_25")
        self.gridLayoutWidget_25.setGeometry(QRect(10, 20, 71, 81))
        self.gridLayout_25 = QGridLayout(self.gridLayoutWidget_25)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.gridLayoutWidget_25)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_25.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_55 = QLabel(self.gridLayoutWidget_25)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_25.addWidget(self.label_55, 1, 0, 1, 1)

        self.gridLayoutWidget_26 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_26.setObjectName(u"gridLayoutWidget_26")
        self.gridLayoutWidget_26.setGeometry(QRect(80, 20, 301, 41))
        self.gridLayout_26 = QGridLayout(self.gridLayoutWidget_26)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.comboBox_13 = QComboBox(self.gridLayoutWidget_26)
        self.comboBox_13.setObjectName(u"comboBox_13")

        self.gridLayout_26.addWidget(self.comboBox_13, 1, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.tab_5)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 340, 391, 91))
        self.gridLayoutWidget_27 = QWidget(self.groupBox_12)
        self.gridLayoutWidget_27.setObjectName(u"gridLayoutWidget_27")
        self.gridLayoutWidget_27.setGeometry(QRect(10, 50, 371, 28))
        self.gridLayout_27 = QGridLayout(self.gridLayoutWidget_27)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.gridLayoutWidget_27)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(51, 22))
        self.label_56.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_56.setAutoFillBackground(False)

        self.gridLayout_27.addWidget(self.label_56, 0, 0, 1, 1)

        self.comboBox_14 = QComboBox(self.gridLayoutWidget_27)
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.gridLayout_27.addWidget(self.comboBox_14, 0, 1, 1, 1)

        self.gridLayoutWidget_29 = QWidget(self.groupBox_12)
        self.gridLayoutWidget_29.setObjectName(u"gridLayoutWidget_29")
        self.gridLayoutWidget_29.setGeometry(QRect(10, 20, 371, 28))
        self.gridLayout_29 = QGridLayout(self.gridLayoutWidget_29)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.gridLayoutWidget_29)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setEnabled(True)
        self.label_58.setMaximumSize(QSize(81, 22))
        self.label_58.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_29.addWidget(self.label_58, 0, 0, 1, 1)

        self.comboBox_15 = QComboBox(self.gridLayoutWidget_29)
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.gridLayout_29.addWidget(self.comboBox_15, 0, 1, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab_5)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(10, 120, 391, 221))
        self.gridLayoutWidget_30 = QWidget(self.groupBox_13)
        self.gridLayoutWidget_30.setObjectName(u"gridLayoutWidget_30")
        self.gridLayoutWidget_30.setGeometry(QRect(10, 20, 371, 41))
        self.gridLayout_30 = QGridLayout(self.gridLayoutWidget_30)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.gridLayoutWidget_30)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_30.addWidget(self.label_59, 0, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.gridLayoutWidget_30)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_30.addWidget(self.lineEdit_23, 0, 1, 1, 1)

        self.gridLayoutWidget_31 = QWidget(self.groupBox_13)
        self.gridLayoutWidget_31.setObjectName(u"gridLayoutWidget_31")
        self.gridLayoutWidget_31.setGeometry(QRect(10, 70, 371, 95))
        self.gridLayout_31 = QGridLayout(self.gridLayoutWidget_31)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.textEdit_5 = QTextEdit(self.gridLayoutWidget_31)
        self.textEdit_5.setObjectName(u"textEdit_5")

        self.gridLayout_31.addWidget(self.textEdit_5, 1, 0, 1, 1)

        self.label_60 = QLabel(self.gridLayoutWidget_31)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_31.addWidget(self.label_60, 0, 0, 1, 1)

        self.gridLayoutWidget_32 = QWidget(self.groupBox_13)
        self.gridLayoutWidget_32.setObjectName(u"gridLayoutWidget_32")
        self.gridLayoutWidget_32.setGeometry(QRect(10, 170, 371, 41))
        self.gridLayout_32 = QGridLayout(self.gridLayoutWidget_32)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.gridLayoutWidget_32)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_32.addWidget(self.label_61, 0, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.gridLayoutWidget_32)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_32.addWidget(self.lineEdit_24, 0, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_5)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(410, 0, 1471, 831))
        self.label_62 = QLabel(self.groupBox_14)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(10, 30, 81, 21))
        self.spinBox_6 = QSpinBox(self.groupBox_14)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(120, 30, 61, 21))
        self.label_63 = QLabel(self.groupBox_14)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(10, 60, 101, 21))
        self.line_2 = QFrame(self.groupBox_14)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(330, 20, 21, 801))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.comboBox_16 = QComboBox(self.groupBox_14)
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setGeometry(QRect(120, 60, 201, 21))
        self.tableView_2 = QTableView(self.groupBox_14)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(350, 20, 351, 801))
        self.label_64 = QLabel(self.groupBox_14)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(10, 90, 101, 21))
        self.gridLayoutWidget_33 = QWidget(self.groupBox_14)
        self.gridLayoutWidget_33.setObjectName(u"gridLayoutWidget_33")
        self.gridLayoutWidget_33.setGeometry(QRect(10, 120, 311, 161))
        self.gridLayout_33 = QGridLayout(self.gridLayoutWidget_33)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.comboBox_17 = QComboBox(self.gridLayoutWidget_33)
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.gridLayout_33.addWidget(self.comboBox_17, 0, 1, 1, 1)

        self.comboBox_18 = QComboBox(self.gridLayoutWidget_33)
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.gridLayout_33.addWidget(self.comboBox_18, 1, 1, 1, 1)

        self.label_65 = QLabel(self.gridLayoutWidget_33)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_33.addWidget(self.label_65, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_66 = QLabel(self.gridLayoutWidget_33)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_33.addWidget(self.label_66, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_67 = QLabel(self.gridLayoutWidget_33)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_33.addWidget(self.label_67, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_68 = QLabel(self.gridLayoutWidget_33)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_33.addWidget(self.label_68, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_69 = QLabel(self.gridLayoutWidget_33)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_33.addWidget(self.label_69, 4, 0, 1, 1)

        self.lineEdit_25 = QLineEdit(self.gridLayoutWidget_33)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_33.addWidget(self.lineEdit_25, 4, 1, 1, 1)

        self.lineEdit_26 = QLineEdit(self.gridLayoutWidget_33)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_33.addWidget(self.lineEdit_26, 3, 1, 1, 1)

        self.lineEdit_27 = QLineEdit(self.gridLayoutWidget_33)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_33.addWidget(self.lineEdit_27, 2, 1, 1, 1)

        self.groupBox_15 = QGroupBox(self.groupBox_14)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(710, 10, 511, 811))
        self.pushButton_4 = QPushButton(self.groupBox_14)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1230, 20, 231, 26))
        self.pushButton_6 = QPushButton(self.groupBox_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1230, 50, 231, 26))
        self.pushButton_7 = QPushButton(self.groupBox_14)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(1230, 80, 231, 26))
        self.pushButton_8 = QPushButton(self.tab_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(410, 840, 231, 26))
        self.pushButton_9 = QPushButton(self.tab_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(640, 840, 231, 26))
        self.pushButton_10 = QPushButton(self.tab_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(870, 840, 231, 26))
        self.tabWidget.addTab(self.tab_5, "")
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
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 350, 391, 91))
        self.gridLayoutWidget_11 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(10, 50, 371, 28))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(51, 22))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_6.setAutoFillBackground(False)

        self.gridLayout_12.addWidget(self.label_6, 0, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget_11)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_12.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.gridLayoutWidget_10 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 20, 371, 28))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setMaximumSize(QSize(81, 22))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget_10)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_5.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(420, 10, 1471, 821))
        self.label_19 = QLabel(self.groupBox_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 30, 81, 21))
        self.spinBox_3 = QSpinBox(self.groupBox_6)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(120, 30, 61, 21))
        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 60, 101, 21))
        self.line = QFrame(self.groupBox_6)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(310, 20, 41, 781))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.comboBox_7 = QComboBox(self.groupBox_6)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(120, 60, 201, 21))
        self.tableView = QTableView(self.groupBox_6)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(340, 20, 1121, 791))
        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 90, 101, 21))
        self.gridLayoutWidget_24 = QWidget(self.groupBox_6)
        self.gridLayoutWidget_24.setObjectName(u"gridLayoutWidget_24")
        self.gridLayoutWidget_24.setGeometry(QRect(10, 120, 311, 161))
        self.gridLayout_24 = QGridLayout(self.gridLayoutWidget_24)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.comboBox_12 = QComboBox(self.gridLayoutWidget_24)
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout_24.addWidget(self.comboBox_12, 0, 1, 1, 1)

        self.comboBox_11 = QComboBox(self.gridLayoutWidget_24)
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_24.addWidget(self.comboBox_11, 1, 1, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget_24)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_24.addWidget(self.label_52, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_50 = QLabel(self.gridLayoutWidget_24)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_24.addWidget(self.label_50, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_51 = QLabel(self.gridLayoutWidget_24)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_24.addWidget(self.label_51, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_54 = QLabel(self.gridLayoutWidget_24)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_24.addWidget(self.label_54, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_53 = QLabel(self.gridLayoutWidget_24)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_24.addWidget(self.label_53, 4, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.gridLayoutWidget_24)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_24.addWidget(self.lineEdit_22, 4, 1, 1, 1)

        self.lineEdit_21 = QLineEdit(self.gridLayoutWidget_24)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_24.addWidget(self.lineEdit_21, 3, 1, 1, 1)

        self.lineEdit_20 = QLineEdit(self.gridLayoutWidget_24)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_24.addWidget(self.lineEdit_20, 2, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.tab)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(420, 840, 231, 26))
        self.pushButton_12 = QPushButton(self.tab)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(650, 840, 231, 26))
        self.pushButton_13 = QPushButton(self.tab)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(880, 840, 231, 26))
        self.pushButton_14 = QPushButton(self.tab)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(1110, 840, 231, 26))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 40, 451, 221))
        self.gridLayoutWidget_13 = QWidget(self.groupBox_7)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(10, 20, 431, 41))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_13)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_14.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_13)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_14.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.gridLayoutWidget_14 = QWidget(self.groupBox_7)
        self.gridLayoutWidget_14.setObjectName(u"gridLayoutWidget_14")
        self.gridLayoutWidget_14.setGeometry(QRect(10, 70, 431, 95))
        self.gridLayout_15 = QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.textEdit_4 = QTextEdit(self.gridLayoutWidget_14)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.gridLayout_15.addWidget(self.textEdit_4, 1, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_14)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_15.addWidget(self.label_14, 0, 0, 1, 1)

        self.gridLayoutWidget_15 = QWidget(self.groupBox_7)
        self.gridLayoutWidget_15.setObjectName(u"gridLayoutWidget_15")
        self.gridLayoutWidget_15.setGeometry(QRect(10, 170, 431, 41))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_15)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.gridLayoutWidget_15)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_16.addWidget(self.label_15, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_15)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_16.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(10, 260, 451, 91))
        self.gridLayoutWidget_16 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_16.setObjectName(u"gridLayoutWidget_16")
        self.gridLayoutWidget_16.setGeometry(QRect(10, 50, 431, 28))
        self.gridLayout_17 = QGridLayout(self.gridLayoutWidget_16)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.gridLayoutWidget_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(51, 22))
        self.label_16.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_16.setAutoFillBackground(False)

        self.gridLayout_17.addWidget(self.label_16, 0, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget_16)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_17.addWidget(self.comboBox_5, 0, 1, 1, 1)

        self.gridLayoutWidget_18 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_18.setObjectName(u"gridLayoutWidget_18")
        self.gridLayoutWidget_18.setGeometry(QRect(10, 20, 431, 28))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_18)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.gridLayoutWidget_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(True)
        self.label_18.setMaximumSize(QSize(81, 22))
        self.label_18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.gridLayoutWidget_18)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_6.addWidget(self.comboBox_6, 0, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 350, 451, 481))
        self.gridLayoutWidget_17 = QWidget(self.groupBox_10)
        self.gridLayoutWidget_17.setObjectName(u"gridLayoutWidget_17")
        self.gridLayoutWidget_17.setGeometry(QRect(10, 20, 431, 431))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_17)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.gridLayoutWidget_17)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_18.addWidget(self.label_33, 10, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_30 = QLabel(self.gridLayoutWidget_17)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_18.addWidget(self.label_30, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_31 = QLabel(self.gridLayoutWidget_17)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_18.addWidget(self.label_31, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_26 = QLabel(self.gridLayoutWidget_17)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_18.addWidget(self.label_26, 5, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_21 = QLabel(self.gridLayoutWidget_17)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_18.addWidget(self.label_21, 6, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_29 = QLabel(self.gridLayoutWidget_17)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_18.addWidget(self.label_29, 3, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_23 = QLabel(self.gridLayoutWidget_17)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_18.addWidget(self.label_23, 7, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_24 = QLabel(self.gridLayoutWidget_17)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_18.addWidget(self.label_24, 8, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_25 = QLabel(self.gridLayoutWidget_17)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_18.addWidget(self.label_25, 9, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_17 = QLabel(self.gridLayoutWidget_17)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_18.addWidget(self.label_17, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_22 = QLabel(self.gridLayoutWidget_17)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_18.addWidget(self.label_22, 4, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_18.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_18.addWidget(self.lineEdit_8, 3, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_18.addWidget(self.lineEdit_9, 4, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_18.addWidget(self.lineEdit_10, 5, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_18.addWidget(self.lineEdit_11, 6, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_18.addWidget(self.lineEdit_12, 7, 1, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.gridLayoutWidget_17)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout_18.addWidget(self.dateTimeEdit, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_18.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget_17)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_18.addWidget(self.lineEdit_13, 8, 1, 1, 1)

        self.comboBox_8 = QComboBox(self.gridLayoutWidget_17)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_18.addWidget(self.comboBox_8, 9, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.gridLayoutWidget_17)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_18.addWidget(self.plainTextEdit, 10, 1, 1, 1)

        self.groupBox_11 = QGroupBox(self.tab_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(470, 40, 421, 791))
        self.label_32 = QLabel(self.groupBox_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 60, 121, 20))
        self.lineEdit_14 = QLineEdit(self.groupBox_11)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(130, 60, 281, 21))
        self.gridLayoutWidget_19 = QWidget(self.groupBox_11)
        self.gridLayoutWidget_19.setObjectName(u"gridLayoutWidget_19")
        self.gridLayoutWidget_19.setGeometry(QRect(40, 90, 371, 161))
        self.gridLayout_19 = QGridLayout(self.gridLayoutWidget_19)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.gridLayoutWidget_19)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_19.addWidget(self.label_28, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_27 = QLabel(self.gridLayoutWidget_19)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_19.addWidget(self.label_27, 3, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_36 = QLabel(self.gridLayoutWidget_19)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_19.addWidget(self.label_36, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_37 = QLabel(self.gridLayoutWidget_19)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_19.addWidget(self.label_37, 4, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_35 = QLabel(self.gridLayoutWidget_19)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_19.addWidget(self.label_35, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.comboBox_10 = QComboBox(self.gridLayoutWidget_19)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.gridLayout_19.addWidget(self.comboBox_10, 1, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget_19)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_19.addWidget(self.lineEdit_15, 2, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.gridLayoutWidget_19)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_19.addWidget(self.lineEdit_16, 3, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.gridLayoutWidget_19)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_19.addWidget(self.lineEdit_17, 4, 1, 1, 1)

        self.comboBox_9 = QComboBox(self.gridLayoutWidget_19)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout_19.addWidget(self.comboBox_9, 0, 1, 1, 1)

        self.gridLayoutWidget_20 = QWidget(self.groupBox_11)
        self.gridLayoutWidget_20.setObjectName(u"gridLayoutWidget_20")
        self.gridLayoutWidget_20.setGeometry(QRect(10, 259, 401, 60))
        self.gridLayout_20 = QGridLayout(self.gridLayoutWidget_20)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.gridLayoutWidget_20)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_20.addWidget(self.label_40, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_39 = QLabel(self.gridLayoutWidget_20)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_20.addWidget(self.label_39, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_18 = QLineEdit(self.gridLayoutWidget_20)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_20.addWidget(self.lineEdit_18, 0, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.gridLayoutWidget_20)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_20.addWidget(self.lineEdit_19, 1, 1, 1, 1)

        self.gridLayoutWidget_21 = QWidget(self.groupBox_11)
        self.gridLayoutWidget_21.setObjectName(u"gridLayoutWidget_21")
        self.gridLayoutWidget_21.setGeometry(QRect(10, 321, 241, 92))
        self.gridLayout_21 = QGridLayout(self.gridLayoutWidget_21)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.gridLayoutWidget_21)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_21.addWidget(self.label_43, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_41 = QLabel(self.gridLayoutWidget_21)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_21.addWidget(self.label_41, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_42 = QLabel(self.gridLayoutWidget_21)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_21.addWidget(self.label_42, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.spinBox_2 = QSpinBox(self.gridLayoutWidget_21)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_21.addWidget(self.spinBox_2, 0, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.gridLayoutWidget_21)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_21.addWidget(self.doubleSpinBox, 1, 1, 1, 1)

        self.spinBox_4 = QSpinBox(self.gridLayoutWidget_21)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_21.addWidget(self.spinBox_4, 2, 1, 1, 1)

        self.gridLayoutWidget_22 = QWidget(self.groupBox_11)
        self.gridLayoutWidget_22.setObjectName(u"gridLayoutWidget_22")
        self.gridLayoutWidget_22.setGeometry(QRect(12, 418, 241, 60))
        self.gridLayout_22 = QGridLayout(self.gridLayoutWidget_22)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.gridLayoutWidget_22)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_22.addWidget(self.label_45, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_46 = QLabel(self.gridLayoutWidget_22)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_22.addWidget(self.label_46, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.dateEdit = QDateEdit(self.gridLayoutWidget_22)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_22.addWidget(self.dateEdit, 0, 1, 1, 1)

        self.dateEdit_2 = QDateEdit(self.gridLayoutWidget_22)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.gridLayout_22.addWidget(self.dateEdit_2, 1, 1, 1, 1)

        self.gridLayoutWidget_23 = QWidget(self.groupBox_11)
        self.gridLayoutWidget_23.setObjectName(u"gridLayoutWidget_23")
        self.gridLayoutWidget_23.setGeometry(QRect(10, 485, 401, 281))
        self.gridLayout_23 = QGridLayout(self.gridLayoutWidget_23)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_4 = QPlainTextEdit(self.gridLayoutWidget_23)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.gridLayout_23.addWidget(self.plainTextEdit_4, 1, 1, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_23)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_23.addWidget(self.label_47, 1, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.gridLayoutWidget_23)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout_23.addWidget(self.plainTextEdit_3, 0, 1, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget_23)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_23.addWidget(self.label_48, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(1360, 50, 531, 771))
        self.label_34 = QLabel(self.tab_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 10, 271, 31))
        self.label_34.setStyleSheet(u"font: 28pt \"Segoe UI\";")
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(900, 800, 451, 26))
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(900, 770, 211, 26))
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(900, 80, 231, 26))
        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(900, 50, 231, 26))
        self.label_38 = QLabel(self.tab_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(1360, 10, 351, 31))
        self.label_38.setStyleSheet(u"font: 28pt \"Segoe UI\";")
        self.tabWidget.addTab(self.tab_2, "")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 0, 1891, 31))
        self.progressBar.setValue(24)
        reportWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(reportWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1909, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        reportWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menu.addSeparator()
        self.menu.addSeparator()
        self.menu.addSeparator()
        self.menu.addAction(self.action_14)
        self.menu.addAction(self.action_15)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu.addSeparator()
        self.menu_2.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menu_4.addAction(self.action_9)
        self.menu_4.addAction(self.action_10)
        self.menu_5.addAction(self.action_11)

        self.retranslateUi(reportWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(reportWindow)
    # setupUi

    def retranslateUi(self, reportWindow):
        reportWindow.setWindowTitle(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.action.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.action_2.setText(QCoreApplication.translate("reportWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.action_3.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.action_4.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.action_5.setText(QCoreApplication.translate("reportWindow", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u043e\u0442\u0447\u0435\u0442\u043e\u0432", None))
        self.action_6.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.action_7.setText(QCoreApplication.translate("reportWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.action_8.setText(QCoreApplication.translate("reportWindow", u"\u0422\u0435\u043c\u0430", None))
        self.action_9.setText(QCoreApplication.translate("reportWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f", None))
        self.action_10.setText(QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0435", None))
        self.action_11.setText(QCoreApplication.translate("reportWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0447\u0435\u0435 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u0435", None))
        self.action_12.setText(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.action_13.setText(QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.action_14.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u0432\u0430\u044f \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.action_15.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u0432\u043e\u0435 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("reportWindow", u"<html><head/><body><p>\u0432</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_9.setTitle(QCoreApplication.translate("reportWindow", u"\u041b\u0438\u0446\u043e, \u0437\u0430\u043f\u043e\u043b\u043d\u044f\u044e\u0449\u0438\u0435\u0435 \u043e\u0442\u0447\u0435\u0442:", None))
        self.label_49.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0418\u041e:", None))
        self.label_55.setText(QCoreApplication.translate("reportWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u044f:", None))
        self.label_56.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0438\u043b\u0438\u0430\u043b:", None))
        self.label_58.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0435:", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("reportWindow", u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_59.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 :", None))
        self.label_60.setText(QCoreApplication.translate("reportWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.label_61.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0440\u0438\u043a\u0430\u0437\u0430:*", None))
        self.lineEdit_24.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("reportWindow", u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0434\u0435\u043d\u0438\u0435", None))
        self.label_62.setText(QCoreApplication.translate("reportWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u044d\u0442\u0430\u0436:", None))
        self.label_63.setText(QCoreApplication.translate("reportWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043e\u043c\u043d\u0430\u0442\u0443:", None))
        self.label_64.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b:", None))
        self.label_65.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_66.setText(QCoreApplication.translate("reportWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.label_67.setText(QCoreApplication.translate("reportWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c:", None))
        self.label_68.setText(QCoreApplication.translate("reportWindow", u"\u0422\u0438\u043f:", None))
        self.label_69.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043c\u0435\u0441\u0442\u0430:", None))
        self.pushButton_4.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("reportWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043a\u043e\u043c\u0430\u043d\u0442\u0443", None))
        self.pushButton_7.setText(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c:", None))
        self.pushButton_8.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u0441\u0451", None))
        self.pushButton_9.setText(QCoreApplication.translate("reportWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0441\u0451", None))
        self.pushButton_10.setText(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u0443\u044e \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("reportWindow", u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
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
        self.lineEdit_4.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u0430\u0438\u0446\u0438\u044f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("reportWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u044f:", None))
        self.label_6.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0438\u043b\u0438\u0430\u043b:", None))
        self.label_5.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0435:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("reportWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None))
        self.label_19.setText(QCoreApplication.translate("reportWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u044d\u0442\u0430\u0436:", None))
        self.label_20.setText(QCoreApplication.translate("reportWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043e\u043c\u043d\u0430\u0442\u0443:", None))
        self.label_44.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u044b:", None))
        self.label_52.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_50.setText(QCoreApplication.translate("reportWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.label_51.setText(QCoreApplication.translate("reportWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c:", None))
        self.label_54.setText(QCoreApplication.translate("reportWindow", u"\u0422\u0438\u043f:", None))
        self.label_53.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.pushButton_11.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438 \u043f\u043e \u043a\u043e\u043c\u043d\u0430\u0442\u0435", None))
        self.pushButton_12.setText(QCoreApplication.translate("reportWindow", u".txt", None))
        self.pushButton_13.setText(QCoreApplication.translate("reportWindow", u".pdf", None))
        self.pushButton_14.setText(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u043f\u043e\u043b\u043d\u043e\u0439 \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0432\u0435\u043d\u0442\u0430\u0440\u0438\u0437\u0430\u0438\u0446\u0438\u044f", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_13.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.lineEdit_5.setText(QCoreApplication.translate("reportWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435 \u2116 ", None))
        self.label_14.setText(QCoreApplication.translate("reportWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u0430:", None))
        self.label_15.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0440\u0438\u043a\u0430\u0437\u0430:*", None))
        self.lineEdit_6.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u044f:", None))
        self.label_16.setText(QCoreApplication.translate("reportWindow", u"\u0424\u0438\u043b\u0438\u0430\u043b:", None))
        self.label_18.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0435:", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("reportWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434", None))
        self.label_33.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u044f:", None))
        self.label_30.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u043a\u043b\u0430\u0434\u043d\u043e\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430:", None))
        self.label_31.setText(QCoreApplication.translate("reportWindow", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_26.setText(QCoreApplication.translate("reportWindow", u"Email \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430:", None))
        self.label_21.setText(QCoreApplication.translate("reportWindow", u"\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_29.setText(QCoreApplication.translate("reportWindow", u"\u0418\u041d\u041d \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430:", None))
        self.label_23.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u043e\u0432\u0430\u0440\u043d\u043e\u0439 \u043d\u0430\u043a\u043b\u0430\u0434\u043d\u043e\u0439:", None))
        self.label_24.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430:", None))
        self.label_25.setText(QCoreApplication.translate("reportWindow", u"\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c(\u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a):", None))
        self.label_17.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430:", None))
        self.label_22.setText(QCoreApplication.translate("reportWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430:", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("reportWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435 :", None))
        self.label_32.setText(QCoreApplication.translate("reportWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_28.setText(QCoreApplication.translate("reportWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.label_27.setText(QCoreApplication.translate("reportWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c:", None))
        self.label_36.setText(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_37.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.label_35.setText(QCoreApplication.translate("reportWindow", u"\u0422\u0438\u043f:", None))
        self.label_40.setText(QCoreApplication.translate("reportWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440:", None))
        self.label_39.setText(QCoreApplication.translate("reportWindow", u"\u0418\u043d\u0432\u0435\u043d\u0442\u0440\u0430\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440:", None))
        self.label_43.setText(QCoreApplication.translate("reportWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.label_41.setText(QCoreApplication.translate("reportWindow", u"\u0413\u0430\u0440\u0430\u0440\u0430\u043d\u0442\u0438\u044f:", None))
        self.label_42.setText(QCoreApplication.translate("reportWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u0435\u0434\u0435\u043d\u0438\u0446\u0443:", None))
        self.label_45.setText(QCoreApplication.translate("reportWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0438\u0437\u043e\u0432\u0434\u0441\u0442\u0432\u0430:", None))
        self.label_46.setText(QCoreApplication.translate("reportWindow", u"\u0421\u0440\u043e\u043a \u0433\u043e\u0434\u043d\u043e\u0441\u0442\u0438:", None))
        self.label_47.setText(QCoreApplication.translate("reportWindow", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435:", None))
        self.label_48.setText(QCoreApplication.translate("reportWindow", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438:", None))
        self.label_34.setText(QCoreApplication.translate("reportWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u041d\u041e\u0412\u041e\u0415 \u041f\u041e\u0421\u0422\u0423\u041f\u041b\u0415\u041d\u0418\u042f :</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("reportWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("reportWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 .txt", None))
        self.pushButton_5.setText(QCoreApplication.translate("reportWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 .pdf", None))
        self.label_38.setText(QCoreApplication.translate("reportWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u0411\u0410\u0417\u0410 \u0414\u0410\u041d\u041d\u042b\u0425 \u041f\u041e\u0421\u0422\u0423\u041f\u041b\u0415\u041d\u0418\u042f:</span></p><p><span style=\" font-size:18pt;\"><br/></span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("reportWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.menu.setTitle(QCoreApplication.translate("reportWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_4.setTitle(QCoreApplication.translate("reportWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu_5.setTitle(QCoreApplication.translate("reportWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u044f", None))
        self.menu_6.setTitle(QCoreApplication.translate("reportWindow", u"\u041e\u0422\u041a\u0420\u042b\u0422\u042c \u0421\u0425\u0415\u041c\u0423", None))
    # retranslateUi

