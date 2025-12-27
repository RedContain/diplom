import sqlite3
import sys
from contextlib import contextmanager
from typing import List, Dict
from datetime import datetime
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import Qt

from python_files.code_ui.ui_setting_employes import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Инициализация менеджера БД
        self.db_manager = DatabaseManager()

        # Находим tableWidget
        self.find_table_widget()

        # Загружаем данные при старте
        self.load_data_to_table()

        # Подключение кнопок
        self.pushButton_3.clicked.connect(self.save_employee)

    def find_table_widget(self):

        # Ищем все QTableWidget в форме
        table_widgets = []
        for widget in self.findChildren(QTableWidget):
            table_widgets.append(widget)
            print(f"Найден QTableWidget: {widget.objectName()}")

        # Сохраняем первый найденный tableWidget
        if table_widgets:
            self.tableWidget = table_widgets[0]
            print(f"Используем tableWidget: {self.tableWidget.objectName()}")
        else:
            print("⚠️ QTableWidget не найден в форме")
            self.tableWidget = None

    def save_employee(self):
        """Сохранение сотрудника в БД"""
        name = self.lineEdit.text().strip()
        job_title = self.lineEdit_2.text().strip()

        # Получаем дату из dateEdit (если он есть)
        if hasattr(self, 'dateEdit'):
            date = self.dateEdit.text()
        else:
            date = datetime.now().strftime("%Y-%m-%d")

        # Проверяем обязательные поля
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите имя сотрудника!")
            return

        if not job_title:
            QMessageBox.warning(self, "Ошибка", "Введите должность!")
            return

        try:
            employee_id = self.db_manager.add_item(
                name_id=name,
                job_title=job_title,
                date_of_work=date
            )

            QMessageBox.information(
                self,
                "Успех",
                f"Сотрудник добавлен!\nID: {employee_id}"
            )

            # Очищаем поля
            self.lineEdit.clear()
            self.lineEdit_2.clear()

            # Обновляем таблицу
            self.load_data_to_table()

            print(f"✅ Сотрудник добавлен! ID: {employee_id}")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {e}")
            print(f"Ошибка: {e}")

    def load_data_to_table(self):
        if not hasattr(self, 'tableWidget') or self.tableWidget is None:
            print("tableWidget не найден")
            return

        try:
            # 1. Получаем данные из БД
            employees = self.db_manager.get_all_items()

            # 2. Получаем ссылку на таблицу
            table = self.tableWidget

            # 3. Очищаем таблицу
            table.clear()
            table.setRowCount(0)

            # 4. Если нет данных
            if not employees:
                table.setRowCount(1)
                table.setColumnCount(1)
                table.setItem(0, 0, QTableWidgetItem("Нет данных"))
                return

            # 5. Настраиваем таблицу
            table.setColumnCount(5)  # 5 полей в таблице employees

            # Устанавливаем заголовки
            headers = ["ID", "ФИО", "Должность", "Отчетов", "Дата приема"]
            table.setHorizontalHeaderLabels(headers)

            # Устанавливаем количество строк
            table.setRowCount(len(employees))

            # 6. Заполняем таблицу
            for row, employee in enumerate(employees):
                # ID
                table.setItem(row, 0, QTableWidgetItem(str(employee.get('worker_id', ''))))

                # ФИО
                table.setItem(row, 1, QTableWidgetItem(employee.get('name_id', '')))

                # Должность
                table.setItem(row, 2, QTableWidgetItem(employee.get('job_title', '')))

                # Отчеты
                table.setItem(row, 3, QTableWidgetItem(str(employee.get('report_count', 0))))

                # Дата
                table.setItem(row, 4, QTableWidgetItem(employee.get('date_of_work', '')))

            # 7. Настраиваем отображение
            # Автоподбор ширины столбцов
            table.resizeColumnsToContents()

            # Растягиваем столбец с ФИО
            table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

            # Чередование цветов строк
            table.setAlternatingRowColors(True)

            # Включаем сортировку
            table.setSortingEnabled(True)

            print(f"✅ Загружено {len(employees)} записей в таблицу")

        except Exception as e:
            print(f"Ошибка загрузки данных в таблицу: {e}")


class DatabaseManager:
    def __init__(self, db_path: str = r"C:\Users\lowar\PycharmProjects\diplom\python_files\database\company.db"):
        self.db_path = db_path
        print(f"Путь к БД: {self.db_path}")

        # Проверяем подключение
        if not self.test_connection():
            QMessageBox.critical(None, "Ошибка БД", f"Не удалось подключиться к БД: {self.db_path}")

    @contextmanager
    def get_connection(self):
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

    def test_connection(self) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                return True
        except Exception as e:
            print(f"Ошибка подключения к БД: {e}")
            return False

    def add_item(self, name_id: str, job_title: str, date_of_work: str = None, report_count: int = 0) -> int:
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # Если дата не указана, используем текущую
            if date_of_work is None:
                date_of_work = datetime.now().strftime("%Y-%m-%d")

            cursor.execute(
                "INSERT INTO employees (name_id, job_title, report_count, date_of_work) VALUES (?, ?, ?, ?)",
                (name_id, job_title, report_count, date_of_work)
            )
            return cursor.lastrowid

    def get_all_items(self) -> List[Dict]:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM employees ORDER BY worker_id DESC")
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Ошибка получения данных: {e}")
            return []

    def delete_item(self, worker_id: int) -> bool:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE worker_id = ?", (worker_id,))
            return cursor.rowcount > 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Управление сотрудниками")
    window.show()
    sys.exit(app.exec())