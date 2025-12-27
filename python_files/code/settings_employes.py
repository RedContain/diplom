import sqlite3
import sys
from contextlib import contextmanager
from typing import List, Dict, Any
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit

from python_files.code_ui.ui_setting_employes import Ui_Form

class Ui_Form(QMainWindow, Ui_Form):                                                                      #Инициализация формы
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Кнопки, отвечающие за действия в блоке сотрудники(сам элемент + привязка к методу)

        self.pushButton_3.clicked.connect(self.save_employees)

    def save_employees(self): #сам метод(обращение к БД)
        name = self.lineEdit.text()
        job_title = self.lineEdit_2.text()
        date = self.dateEdit.text()
        try:
            db_manager = DatabaseManager()
            employees = db_manager.add_item(
                name_id = name,
                job_title = job_title,
                date_of_work = date

            )
            print(f"Сотрудник добавлен! ID: {employees}")

        except Exception as e:
            print(f"Ошибка: {e}")

class DatabaseManager:
    def __init__(self,db_path = r"C:\Users\lowar\PycharmProjects\diplom\python_files\database\company.db"):
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
            cursor.execute("SELECT * FROM employees ORDER BY worker_id DESC")
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

    def add_item(self, name_id: str,job_title: str,report_count: int = 0,date_of_work: str = None) -> List[Dict]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (name_id, job_title, report_count, date_of_work) VALUES (?, ?, ?, ?)",
                (name_id, job_title, report_count, "2024-01-01")  # date_of_work нужно как-то получить
            )
            return cursor.lastrowid

    def get_all_items(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees ORDER BY worker_id DESC")
            return [dict(row) for row in cursor.fetchall()]

    def delete_item(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                cursor.execute("DELETE * FROM employees WHERE worker_id = ?", (None,))
            )
    def update_item(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                cursor.execute("")
            )

if __name__ == "__main__":                                                                                               #Главный класс(точка входа в программу)
    app = QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())
