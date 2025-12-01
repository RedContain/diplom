import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication

from python_files.code_ui.ui_reportwindow import Ui_reportWindow

class report_window(QMainWindow, Ui_reportWindow):                                                                      #Инициализация формы
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":                                                                                               #Главный класс(точка входа в программу)
    app = QApplication(sys.argv)
    window = report_window()
    window.show()
    sys.exit(app.exec())
