import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow  # Исправлено: QApplicagittion -> QApplication
from python_files.LoadingWindow.ui_main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):  # Исправлено: используем прямое имя класса
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.counter = 0
        QTimer.singleShot(100, self.start_progress)

    def start_progress(self):
        self.counter = 0
        self.progressBar.setValue(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(30)

    def update_progress(self):
        self.counter += 1
        self.progressBar.setValue(self.counter)

        if self.counter >= 100:
            self.timer.stop()
            self.progressBar.setValue(0)
            self.close()  # Исправлено: закрываем окно вместо sys.exit

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())