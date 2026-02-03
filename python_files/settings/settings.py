import sqlite3
import sys
from contextlib import contextmanager
from typing import List, Dict
from datetime import datetime

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QListWidget, QListWidgetItem
)
from PySide6.QtCore import QDate
from python_files.settings.ui_view import Ui_MainWindow


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # Сначала инициализируем UI
        self.setupUi(self)

        # Затем создаем менеджер БД
        self.db_manager = DatabaseManager()

        # Настраиваем виджеты
        self.spinBox.setValue(0)

        # Подключаем сигналы
        self.setup_connections()

        # Загружаем данные при старте
        self.load_from_database()

    def setup_connections(self):
        """Подключение сигналов к слотам"""
        # Предположим, что у вас есть кнопка с именем addButton
        if hasattr(self, 'addButton'):
            self.addButton.clicked.connect(self.add_to_database)

        # Предположим, что у вас есть кнопка с именем loadButton
        if hasattr(self, 'loadButton'):
            self.loadButton.clicked.connect(self.load_from_database)

    def spinBox_value(self, new_value):
        current = self.spinBox.value() or 0
        new_value = current + 1
        self.spinBox.setValue(new_value)

    def add_to_database(self):
        """Добавление данных из интерфейса в БД"""
        # Предположим, что у вас есть lineEdit для ввода имени
        if hasattr(self, 'nameEdit'):
            name = self.nameEdit.text().strip()
        else:
            name = ""

        if not name:
            QMessageBox.warning(self, "Ошибка", "Заполните поле с именем!")
            return

        try:
            # Используем менеджер БД
            with self.db_manager.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO braches_id (name_id) VALUES (?)",
                    (name,)
                )

            # Очищаем поле
            if hasattr(self, 'nameEdit'):
                self.nameEdit.clear()

            print(f"Добавлено: {name}")

            # Обновляем список
            self.load_from_database()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Ошибка БД", str(e))

    def load_from_database(self):
        """Загрузка данных из БД в виджет"""
        try:
            # Используем менеджер БД
            with self.db_manager.get_connection() as conn:
                cursor = conn.cursor()

                # Проверяем, какая таблица существует
                try:
                    cursor.execute(
                        "SELECT name FROM sqlite_master WHERE type='table' AND name IN ('branches', 'braches_id')")
                    tables = cursor.fetchall()
                    print(f"Найденные таблицы: {tables}")

                    # Выбираем подходящую таблицу
                    if tables:
                        table_name = tables[0][0]
                        cursor.execute(f"SELECT name_id FROM {table_name}")
                    else:
                        print("Таблицы не найдены")
                        return

                except sqlite3.Error as e:
                    print(f"Ошибка при проверке таблиц: {e}")
                    return

                rows = cursor.fetchall()

            # Очищаем listWidget (предполагаем, что он есть в UI)
            if hasattr(self, 'listWidget'):
                self.listWidget.clear()

                # Добавляем данные
                for row in rows:
                    item = QListWidgetItem(str(row['name_id']))
                    self.listWidget.addItem(item)

                print(f"Загружено {len(rows)} записей")
            else:
                print("listWidget не найден в интерфейсе")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Ошибка загрузки", str(e))
            print(f"Ошибка SQL: {e}")


class DatabaseManager:
    def __init__(self, db_path: str = r"C:\Users\lowar\PycharmProjects\diplom\python_files\database\company.db"):
        self.db_path = db_path
        print(f"Путь к БД: {self.db_path}")

        if not self.test_connection():
            print("Не удалось подключиться к БД")

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def test_connection(self) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                return True
        except Exception as e:
            print(f"Ошибка подключения к БД: {e}")
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())