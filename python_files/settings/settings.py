import sys
import sqlite3

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication
from python_files.settings.ui_view import Ui_MainWindow

class mainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.spinBox.setValue(0)
        self.Action = QAction(self)

    def spinBox_value(self,new_value):
        current = self.spinBox.value() or 0
        new_value = current + 1
        self.spinBox.setValue(new_value)

    def add_name_company(self):
        pass

    def redaction(self):
        pass

    def settings_access(self):
        pass

    def administator_form(self):
        pass


if __name__ == "__main__":                                                                                               #Главный класс(точка входа в программу)
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())