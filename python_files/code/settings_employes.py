import sqlite3
import sys
from contextlib import contextmanager
from typing import List, Dict, Any
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from python_files.code_ui.ui_setting_employes import Ui_Form

class Ui_Form(QMainWindow, Ui_Form):                                                                      #Инициализация формы
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class logic_window():
    def __init__(self):
        super().__init__()


class DatabaseManager:
    def __init__(self, db_path: str = "database/database/company.db"):
        self.db_path = db_path

    @contextmanager
    def get_connection(self):
        """Контекстный менеджер для работы с БД"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def get_table_structure(self, table_name: str = "employees") -> List[Dict]:
        """Получение структуры таблицы"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Используем параметризованный запрос для безопасности
            cursor.execute("PRAGMA table_info(?)", (table_name,))
            return [dict(row) for row in cursor.fetchall()]

    def test_connection(self) -> bool:
        """Проверка подключения к БД"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                return True
        except Exception as e:
            print(f"Ошибка подключения к БД: {e}")
            return False

    def item(self, name,description=""):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (worker_id,name_id, job_title) VALUES (?, ?)",
                (name, description)
            )
            return cursor.lastrowid

    def get_all_items(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employess ORDER BY id DESC")
            return [dict(row) for row in cursor.fetchall()]

if __name__ == "__main__":                                                                                               #Главный класс(точка входа в программу)
    app = QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())
