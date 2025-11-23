# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_employes.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(779, 261)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 431, 251))
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 20, 391, 221))
        self.verticalSlider = QSlider(self.groupBox)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(400, 20, 31, 221))
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QRect(450, 10, 321, 151))
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 301, 91))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(610, 230, 161, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 230, 161, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424.\u0418.\u041e", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0432\u0441\u0435", None))
    # retranslateUi

