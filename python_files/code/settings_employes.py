import sqlite3
import sys
from contextlib import contextmanager
from typing import List, Dict
from datetime import datetime
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
)
from PySide6.QtCore import QDate
from python_files.code_ui.ui_setting_employes import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_manager = DatabaseManager()
        self.selected_employee_id = None
        self.is_editing = False
        self.find_table_widget()
        self.setup_table()
        self.load_data_to_table()
        self.pushButton_3.clicked.connect(self.save_employee)  # Кнопка "Сохранить/Добавить"
        self.pushButton_4.clicked.connect(self.delete_employee)  # Кнопка "Удалить"

        if hasattr(self, 'pushButton'):
            self.pushButton.clicked.connect(self.update_employee)  # Кнопка "Обновить"

    def find_table_widget(self):
        """Находит tableWidget в форме"""
        table_widgets = []
        for widget in self.findChildren(QTableWidget):
            table_widgets.append(widget)
            print(f"Найден QTableWidget: {widget.objectName()}")

        if table_widgets:
            self.tableWidget = table_widgets[0]
            print(f"Используем tableWidget: {self.tableWidget.objectName()}")
        else:
            print("⚠️ QTableWidget не найден в форме")
            self.tableWidget = None

    def setup_table(self):
        """Настраивает таблицу"""
        if not hasattr(self, 'tableWidget') or self.tableWidget is None:
            return

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.cellClicked.connect(self.on_row_selected)

    def on_row_selected(self, row, column):
        """Обработка выбора строки в таблице"""
        id_item = self.tableWidget.item(row, 0)

        if id_item and id_item.text():
            try:
                self.selected_employee_id = int(id_item.text())
                self.load_employee_to_form(self.selected_employee_id)
                self.set_edit_mode(True)
            except ValueError:
                print("❌ Неверный ID сотрудника")

    def load_employee_to_form(self, worker_id):
        """Загружает данные сотрудника в форму"""
        employee = self.db_manager.get_item_by_id(worker_id)

        if employee:
            # Проверяем существование полей
            if hasattr(self, 'lineEdit'):
                self.lineEdit.setText(employee.get('name_id', ''))

            if hasattr(self, 'lineEdit_2'):
                self.lineEdit_2.setText(employee.get('job_title', ''))

            # Загружаем дату если есть dateEdit
            if hasattr(self, 'dateEdit') and employee.get('date_of_work'):
                date_str = employee['date_of_work']
                try:
                    # Пробуем разные форматы даты
                    date = QDate.fromString(date_str, "yyyy-MM-dd")
                    if not date.isValid():
                        date = QDate.fromString(date_str, "dd.MM.yyyy")
                    if date.isValid():
                        self.dateEdit.setDate(date)
                except Exception as e:
                    print(f"❌ Ошибка загрузки даты: {e}")

    def set_edit_mode(self, editing):
        """Переключает режим редактирования"""
        self.is_editing = editing

        if hasattr(self, 'pushButton_3'):
            if editing:
                self.pushButton_3.setText("💾 Обновить")
            else:
                self.pushButton_3.setText("➕ Добавить")
                self.selected_employee_id = None
                self.clear_form()

    def clear_form(self):
        """Очищает форму"""
        if hasattr(self, 'lineEdit'):
            self.lineEdit.clear()
        if hasattr(self, 'lineEdit_2'):
            self.lineEdit_2.clear()
        if hasattr(self, 'dateEdit'):
            self.dateEdit.setDate(QDate.currentDate())

    def save_employee(self):
        """Сохраняет нового сотрудника"""
        try:
            # Проверяем существование полей
            if not hasattr(self, 'lineEdit') or not hasattr(self, 'lineEdit_2'):
                QMessageBox.critical(self, "Ошибка",
                                     "Не найдены поля для ввода. Проверьте имена виджетов.")
                return

            # Получаем данные
            name = self.lineEdit.text().strip()
            job_title = self.lineEdit_2.text().strip()

            # Получаем дату
            date_str = None
            if hasattr(self, 'dateEdit'):
                date = self.dateEdit.date()
                date_str = date.toString("yyyy-MM-dd")
            else:
                date_str = datetime.now().strftime("%Y-%m-%d")

            # Валидация
            if not name:
                QMessageBox.warning(self, "Ошибка", "Введите имя сотрудника!")
                return

            if not job_title:
                QMessageBox.warning(self, "Ошибка", "Введите должность!")
                return

            # Сохраняем в БД
            employee_id = self.db_manager.add_item(
                name_id=name,
                job_title=job_title,
                date_of_work=date_str
            )

            QMessageBox.information(
                self,
                "Успех",
                f"Сотрудник добавлен!\nID: {employee_id}"
            )

            # Очищаем форму
            self.clear_form()

            # Обновляем таблицу
            self.load_data_to_table()

            print(f"✅ Сотрудник добавлен! ID: {employee_id}")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {str(e)}")
            print(f"❌ Ошибка: {e}")

    def update_employee(self):
        """Обновляет существующего сотрудника"""
        if not self.selected_employee_id:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите сотрудника для редактирования!")
            return

        try:
            # Получаем данные
            name = self.lineEdit.text().strip()
            job_title = self.lineEdit_2.text().strip()

            # Получаем дату
            date_str = None
            if hasattr(self, 'dateEdit'):
                date = self.dateEdit.date()
                date_str = date.toString("yyyy-MM-dd")

            # Валидация
            if not name:
                QMessageBox.warning(self, "Ошибка", "Введите имя!")
                return

            if not job_title:
                QMessageBox.warning(self, "Ошибка", "Введите должность!")
                return

            # Обновляем в БД
            success = self.db_manager.update_item(
                worker_id=self.selected_employee_id,
                name_id=name,
                job_title=job_title,
                date_of_work=date_str
            )

            if success:
                QMessageBox.information(self, "Успех", "Данные обновлены!")
                self.set_edit_mode(False)
                self.load_data_to_table()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось обновить")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")

    def delete_employee(self):
        """Удаляет выбранного сотрудника"""
        if not hasattr(self, 'tableWidget') or self.tableWidget is None:
            return

        selected_rows = self.tableWidget.selectionModel().selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите сотрудника в таблице!")
            return

        row = selected_rows[0].row()
        id_item = self.tableWidget.item(row, 0)

        if not id_item:
            QMessageBox.warning(self, "Ошибка", "Не удалось получить ID сотрудника!")
            return

        worker_id = int(id_item.text())

        name_item = self.tableWidget.item(row, 1)
        employee_name = name_item.text() if name_item else "Неизвестно"

        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f"Вы уверены, что хотите удалить сотрудника:\n\n"
            f"ID: {worker_id}\n"
            f"ФИО: {employee_name}",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                success = self.db_manager.delete_item(worker_id)

                if success:
                    QMessageBox.information(
                        self,
                        "Успех",
                        f"Сотрудник {employee_name} удален!"
                    )
                    print(f"✅ Сотрудник #{worker_id} удален")

                    # Если удаляем редактируемого сотрудника
                    if self.selected_employee_id == worker_id:
                        self.set_edit_mode(False)

                    self.load_data_to_table()
                else:
                    QMessageBox.warning(self, "Ошибка", "Не удалось удалить сотрудника")

            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при удалении:\n{str(e)}")

    def load_data_to_table(self):
        """Загружает данные из БД в таблицу"""
        if not hasattr(self, 'tableWidget') or self.tableWidget is None:
            print("❌ tableWidget не найден")
            return

        try:
            employees = self.db_manager.get_all_items()
            table = self.tableWidget
            table.clear()
            table.setRowCount(0)

            if not employees:
                table.setRowCount(1)
                table.setColumnCount(1)
                table.setItem(0, 0, QTableWidgetItem("Нет данных"))
                return

            table.setColumnCount(5)  # 5 полей в таблице employees
            headers = ["ID", "ФИО", "Должность", "Отчетов", "Дата приема"]
            table.setHorizontalHeaderLabels(headers)
            table.setRowCount(len(employees))

            for row, employee in enumerate(employees):
                table.setItem(row, 0, QTableWidgetItem(str(employee.get('worker_id', ''))))
                table.setItem(row, 1, QTableWidgetItem(employee.get('name_id', '')))
                table.setItem(row, 2, QTableWidgetItem(employee.get('job_title', '')))
                table.setItem(row, 3, QTableWidgetItem(str(employee.get('report_count', 0))))
                table.setItem(row, 4, QTableWidgetItem(employee.get('date_of_work', '')))

            table.resizeColumnsToContents()
            table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            table.setAlternatingRowColors(True)
            table.setSortingEnabled(True)

            print(f"✅ Загружено {len(employees)} записей в таблицу")

        except Exception as e:
            print(f"❌ Ошибка загрузки данных в таблицу: {e}")


class DatabaseManager:
    def __init__(self, db_path: str = r"C:\Users\lowar\PycharmProjects\diplom\python_files\database\company.db"):
        self.db_path = db_path
        print(f"📊 Путь к БД: {self.db_path}")

        if not self.test_connection():
            print("❌ Не удалось подключиться к БД")

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
            print(f"❌ Ошибка подключения к БД: {e}")
            return False

    def add_item(self, name_id: str, job_title: str, date_of_work: str = None, report_count: int = 0) -> int:
        """Добавляет нового сотрудника"""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            if date_of_work is None:
                date_of_work = datetime.now().strftime("%Y-%m-%d")

            cursor.execute(
                "INSERT INTO employees (name_id, job_title, report_count, date_of_work) VALUES (?, ?, ?, ?)",
                (name_id, job_title, report_count, date_of_work)
            )
            return cursor.lastrowid

    def get_all_items(self) -> List[Dict]:
        """Получает всех сотрудников"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM employees ORDER BY worker_id DESC")
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"❌ Ошибка получения данных: {e}")
            return []

    def get_item_by_id(self, worker_id: int) -> Dict:
        """Получает сотрудника по ID"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM employees WHERE worker_id = ?", (worker_id,))
                row = cursor.fetchone()
                return dict(row) if row else {}
        except Exception as e:
            print(f"❌ Ошибка получения сотрудника: {e}")
            return {}

    def update_item(self, worker_id: int, **kwargs) -> bool:
        """Обновляет сотрудника"""
        if not kwargs:
            return False

        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()

                # Формируем запрос
                set_parts = []
                values = []

                if 'name_id' in kwargs and kwargs['name_id'] is not None:
                    set_parts.append("name_id = ?")
                    values.append(kwargs['name_id'])

                if 'job_title' in kwargs and kwargs['job_title'] is not None:
                    set_parts.append("job_title = ?")
                    values.append(kwargs['job_title'])

                if 'report_count' in kwargs and kwargs['report_count'] is not None:
                    set_parts.append("report_count = ?")
                    values.append(kwargs['report_count'])

                if 'date_of_work' in kwargs and kwargs['date_of_work'] is not None:
                    set_parts.append("date_of_work = ?")
                    values.append(kwargs['date_of_work'])

                if not set_parts:
                    return False

                values.append(worker_id)
                sql = f"UPDATE employees SET {', '.join(set_parts)} WHERE worker_id = ?"

                cursor.execute(sql, values)
                return cursor.rowcount > 0

        except Exception as e:
            print(f"❌ Ошибка обновления: {e}")
            return False

    def delete_item(self, worker_id: int) -> bool:
        """Удаляет сотрудника"""
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