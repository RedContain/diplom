import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox   # Шаблон полключения главного окна
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())