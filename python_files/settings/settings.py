import sys
import os
import sqlite3
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QListWidgetItem, QDialog, QVBoxLayout,
                               QTableWidget, QTableWidgetItem, QHeaderView,
                               QPushButton, QHBoxLayout, QFormLayout,
                               QLineEdit, QSpinBox, QDateEdit)
from PySide6.QtCore import Qt, QDate
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QScreen

# Путь к твоей БД
python_files_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(python_files_dir, "database", "database", "company.db")

print(f"Путь к БД: {db_path}")
print(f"Файл существует: {os.path.exists(db_path)}")


class DatabaseHandler:
    """Класс для работы с существующей БД"""

    def __init__(self, db_path):
        self.db_path = db_path
        print("✅ Используем существующую БД")

    def get_connection(self):
        """Получение соединения с БД"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    # ========== МЕТОДЫ ДЛЯ ПРЕДПРИЯТИЯ ==========
    def get_company_name(self):
        """Получение названия предприятия"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT name FROM company LIMIT 1")
            result = cursor.fetchone()
            conn.close()
            return result[0] if result else "ГБОУ Больница 2 г. Апшеронск"
        except:
            conn.close()
            return "ГБОУ Больница 2 г. Апшеронск"

    def save_company_name(self, name):
        """Сохранение названия предприятия"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS company (id INTEGER PRIMARY KEY, name TEXT)")
            cursor.execute("DELETE FROM company")
            cursor.execute("INSERT INTO company (name) VALUES (?)", (name,))
            conn.commit()
        except Exception as e:
            print(f"Ошибка сохранения названия: {e}")
        finally:
            conn.close()

    # ========== МЕТОДЫ ДЛЯ ФИЛИАЛОВ ==========
    def get_all_branches(self):
        """Получение всех филиалов"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT branch_id, name, floors_count, address FROM branches")
        branches = cursor.fetchall()
        conn.close()
        return branches

    def add_branch(self, name, floors_count=1, address=''):
        """Добавление филиала"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO branches (name, floors_count, address)
                       VALUES (?, ?, ?)
                       """, (name, floors_count, address))
        branch_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return branch_id

    def update_branch(self, branch_id, name, floors_count, address):
        """Обновление филиала"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       UPDATE branches
                       SET name = ?, floors_count = ?, address = ?
                       WHERE branch_id = ?
                       """, (name, floors_count, address, branch_id))
        conn.commit()
        conn.close()

    def delete_branch(self, branch_id):
        """Удаление филиала"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM branches WHERE branch_id = ?", (branch_id,))
        conn.commit()
        conn.close()

    def get_branch(self, branch_id):
        """Получение филиала по ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT branch_id, name, floors_count, address
                       FROM branches WHERE branch_id = ?
                       """, (branch_id,))
        branch = cursor.fetchone()
        conn.close()
        return branch

    # ========== МЕТОДЫ ДЛЯ СОТРУДНИКОВ ==========
    def get_employees(self, branch_id=None):
        """Получение сотрудников"""
        conn = self.get_connection()
        cursor = conn.cursor()

        if branch_id:
            try:
                cursor.execute("""
                               SELECT worker_id, name_id, job_title, report_count, date_of_work
                               FROM employees WHERE branch_id = ?
                               """, (branch_id,))
            except sqlite3.OperationalError:
                cursor.execute("""
                               SELECT worker_id, name_id, job_title, report_count, date_of_work
                               FROM employees
                               """)
        else:
            cursor.execute("""
                           SELECT worker_id, name_id, job_title, report_count, date_of_work
                           FROM employees ORDER BY worker_id DESC
                           """)

        employees = cursor.fetchall()
        conn.close()
        return employees

    def add_employee(self, name, job_title, date_of_work, branch_id=None):
        """Добавление сотрудника"""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                           INSERT INTO employees (name_id, job_title, report_count, date_of_work, branch_id)
                           VALUES (?, ?, ?, ?, ?)
                           """, (name, job_title, 0, date_of_work, branch_id))
        except sqlite3.OperationalError:
            cursor.execute("""
                           INSERT INTO employees (name_id, job_title, report_count, date_of_work)
                           VALUES (?, ?, ?, ?)
                           """, (name, job_title, 0, date_of_work))

        employee_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return employee_id

    def update_employee(self, worker_id, name, job_title, date_of_work):
        """Обновление сотрудника"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       UPDATE employees
                       SET name_id = ?, job_title = ?, date_of_work = ?
                       WHERE worker_id = ?
                       """, (name, job_title, date_of_work, worker_id))
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success

    def delete_employee(self, employee_id):
        """Удаление сотрудника"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE worker_id = ?", (employee_id,))
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success

    # ========== МЕТОДЫ ДЛЯ КОМНАТ ==========
    def get_rooms(self, branch_id=None):
        """Получение комнат"""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            if branch_id:
                cursor.execute("""
                               SELECT room_id, room_number, room_name
                               FROM room WHERE branch_id = ?
                               """, (branch_id,))
            else:
                cursor.execute("SELECT room_id, room_number, room_name FROM room")
        except sqlite3.OperationalError:
            cursor.execute("SELECT room_id, room_number, room_name FROM room")

        rooms = cursor.fetchall()
        conn.close()
        return rooms

    def add_room(self, room_number, room_name, branch_id=None):
        """Добавление комнаты"""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                           INSERT INTO room (room_number, room_name, branch_id)
                           VALUES (?, ?, ?)
                           """, (room_number, room_name, branch_id))
        except sqlite3.OperationalError:
            cursor.execute("""
                           INSERT INTO room (room_number, room_name)
                           VALUES (?, ?)
                           """, (room_number, room_name))

        room_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return room_id

    def delete_room(self, room_id):
        """Удаление комнаты"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM room WHERE room_id = ?", (room_id,))
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success

    # ========== МЕТОДЫ ДЛЯ ПОЛЬЗОВАТЕЛЕЙ ==========
    def get_users(self):
        """Получение пользователей"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT username FROM users")
            users = cursor.fetchall()
        except sqlite3.OperationalError:
            users = []
        conn.close()
        return users

    def change_password(self, username, new_password):
        """Смена пароля"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
            conn.commit()
            success = True
        except:
            success = False
        conn.close()
        return success


class EmployeesDialog(QDialog):
    """Диалог для управления сотрудниками"""

    def __init__(self, db, branch_id, branch_name, parent=None):
        super().__init__(parent)
        self.db = db
        self.branch_id = branch_id
        self.selected_employee_id = None
        self.setWindowTitle(f"Сотрудники филиала: {branch_name}")
        self.setMinimumSize(700, 500)

        # На весь экран не делаем, но делаем побольше
        self.resize(800, 600)

        layout = QVBoxLayout(self)

        # Таблица сотрудников
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "ФИО", "Должность", "Отчетов", "Дата приема"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.cellClicked.connect(self.on_row_selected)
        layout.addWidget(self.table)

        # Форма для ввода
        form_layout = QFormLayout()

        self.name_edit = QLineEdit()
        self.job_edit = QLineEdit()
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)

        form_layout.addRow("ФИО:", self.name_edit)
        form_layout.addRow("Должность:", self.job_edit)
        form_layout.addRow("Дата приема:", self.date_edit)

        layout.addLayout(form_layout)

        # Кнопки
        btn_layout = QHBoxLayout()

        self.add_btn = QPushButton("➕ Добавить")
        self.add_btn.clicked.connect(self.add_employee)

        self.update_btn = QPushButton("✏️ Обновить")
        self.update_btn.clicked.connect(self.update_employee)
        self.update_btn.setEnabled(False)

        self.delete_btn = QPushButton("🗑️ Удалить")
        self.delete_btn.clicked.connect(self.delete_employee)
        self.delete_btn.setEnabled(False)

        close_btn = QPushButton("❌ Закрыть")
        close_btn.clicked.connect(self.accept)

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)

        # Загружаем данные
        self.load_employees()

    def load_employees(self):
        """Загрузка сотрудников в таблицу"""
        employees = self.db.get_employees(self.branch_id)
        self.table.setRowCount(len(employees))

        for i, emp in enumerate(employees):
            self.table.setItem(i, 0, QTableWidgetItem(str(emp[0])))  # ID
            self.table.setItem(i, 1, QTableWidgetItem(emp[1]))  # Имя
            self.table.setItem(i, 2, QTableWidgetItem(emp[2]))  # Должность
            self.table.setItem(i, 3, QTableWidgetItem(str(emp[3])))  # Отчеты
            self.table.setItem(i, 4, QTableWidgetItem(emp[4]))  # Дата

    def on_row_selected(self, row, column):
        """Выбор строки в таблице"""
        id_item = self.table.item(row, 0)
        if id_item:
            self.selected_employee_id = int(id_item.text())

            # Загружаем данные в форму
            name_item = self.table.item(row, 1)
            job_item = self.table.item(row, 2)
            date_item = self.table.item(row, 4)

            if name_item:
                self.name_edit.setText(name_item.text())
            if job_item:
                self.job_edit.setText(job_item.text())
            if date_item:
                date = QDate.fromString(date_item.text(), "yyyy-MM-dd")
                if date.isValid():
                    self.date_edit.setDate(date)

            # Активируем кнопки
            self.update_btn.setEnabled(True)
            self.delete_btn.setEnabled(True)
            self.add_btn.setText("➕ Добавить (нового)")

    def add_employee(self):
        """Добавление нового сотрудника"""
        name = self.name_edit.text().strip()
        job = self.job_edit.text().strip()
        date = self.date_edit.date().toString("yyyy-MM-dd")

        if not name or not job:
            QMessageBox.warning(self, "Ошибка", "Заполните ФИО и должность")
            return

        employee_id = self.db.add_employee(name, job, date, self.branch_id)

        QMessageBox.information(self, "Успех", f"Сотрудник добавлен с ID: {employee_id}")

        # Очищаем форму и обновляем таблицу
        self.name_edit.clear()
        self.job_edit.clear()
        self.date_edit.setDate(QDate.currentDate())
        self.selected_employee_id = None
        self.update_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.add_btn.setText("➕ Добавить")
        self.load_employees()

    def update_employee(self):
        """Обновление сотрудника"""
        if not self.selected_employee_id:
            return

        name = self.name_edit.text().strip()
        job = self.job_edit.text().strip()
        date = self.date_edit.date().toString("yyyy-MM-dd")

        if not name or not job:
            QMessageBox.warning(self, "Ошибка", "Заполните ФИО и должность")
            return

        success = self.db.update_employee(self.selected_employee_id, name, job, date)

        if success:
            QMessageBox.information(self, "Успех", "Данные обновлены")
            self.selected_employee_id = None
            self.update_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
            self.add_btn.setText("➕ Добавить")
            self.name_edit.clear()
            self.job_edit.clear()
            self.date_edit.setDate(QDate.currentDate())
            self.load_employees()

    def delete_employee(self):
        """Удаление сотрудника"""
        if not self.selected_employee_id:
            return

        reply = QMessageBox.question(self, "Подтверждение",
                                     "Удалить сотрудника?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            success = self.db.delete_employee(self.selected_employee_id)

            if success:
                QMessageBox.information(self, "Успех", "Сотрудник удален")
                self.selected_employee_id = None
                self.update_btn.setEnabled(False)
                self.delete_btn.setEnabled(False)
                self.add_btn.setText("➕ Добавить")
                self.name_edit.clear()
                self.job_edit.clear()
                self.date_edit.setDate(QDate.currentDate())
                self.load_employees()


class RoomsDialog(QDialog):
    """Диалог для управления комнатами"""

    def __init__(self, db, branch_id, branch_name, parent=None):
        super().__init__(parent)
        self.db = db
        self.branch_id = branch_id
        self.setWindowTitle(f"Комнаты филиала: {branch_name}")
        self.setMinimumSize(600, 500)

        layout = QVBoxLayout(self)

        # Таблица комнат
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Номер", "Название"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        # Форма
        form_layout = QFormLayout()
        self.number_edit = QLineEdit()
        self.name_edit = QLineEdit()

        form_layout.addRow("Номер комнаты:", self.number_edit)
        form_layout.addRow("Название:", self.name_edit)
        layout.addLayout(form_layout)

        # Кнопки
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("➕ Добавить")
        add_btn.clicked.connect(self.add_room)
        delete_btn = QPushButton("🗑️ Удалить")
        delete_btn.clicked.connect(self.delete_room)
        close_btn = QPushButton("❌ Закрыть")
        close_btn.clicked.connect(self.accept)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(delete_btn)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)

        self.load_rooms()

    def load_rooms(self):
        """Загрузка комнат"""
        rooms = self.db.get_rooms(self.branch_id)
        self.table.setRowCount(len(rooms))

        for i, room in enumerate(rooms):
            self.table.setItem(i, 0, QTableWidgetItem(str(room[0])))
            self.table.setItem(i, 1, QTableWidgetItem(room[1]))
            self.table.setItem(i, 2, QTableWidgetItem(room[2]))

    def add_room(self):
        """Добавление комнаты"""
        number = self.number_edit.text().strip()
        name = self.name_edit.text().strip()

        if not number or not name:
            QMessageBox.warning(self, "Ошибка", "Заполните номер и название комнаты")
            return

        self.db.add_room(number, name, self.branch_id)
        self.load_rooms()
        self.number_edit.clear()
        self.name_edit.clear()

    def delete_room(self):
        """Удаление комнаты"""
        row = self.table.currentRow()
        if row >= 0:
            room_id = int(self.table.item(row, 0).text())

            reply = QMessageBox.question(self, "Подтверждение",
                                         "Удалить комнату?",
                                         QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.db.delete_room(room_id)
                self.load_rooms()


class MainWindow(QMainWindow):
    """Главное окно настроек"""

    def __init__(self):
        super().__init__()

        # Подключаемся к БД
        self.db = DatabaseHandler(db_path)

        self.current_branch_id = None
        self.original_company_name = ""  # Для отслеживания изменений
        self.changes_made = False  # Флаг наличия изменений

        self.load_ui()
        if self.ui:
            self.setup_connections()
            self.load_initial_data()
            self.showMaximized()  # 👈 РАЗВОРАЧИВАЕМ НА ВЕСЬ ЭКРАН

    def load_ui(self):
        """Загрузка UI из View.ui"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(current_dir, "View.ui")

        if not os.path.exists(ui_path):
            QMessageBox.critical(self, "Ошибка", f"Файл View.ui не найден: {ui_path}")
            return

        loader = QUiLoader()
        ui_file = QFile(ui_path)
        ui_file.open(QIODevice.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        if not self.ui:
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить интерфейс")
            return

        self.setCentralWidget(self.ui.centralwidget)

        # Сохраняем ссылки на виджеты
        self.company_name_edit = self.ui.lineEdit
        self.branches_spin = self.ui.spinBox
        self.branches_list = self.ui.listWidget
        self.branch_group = self.ui.groupBox_3
        self.branch_name_edit = self.ui.lineEdit_2
        self.branch_address_edit = self.ui.lineEdit_5
        self.employees_spin = self.ui.spinBox_3
        self.floors_spin = self.ui.spinBox_4
        self.rooms_spin = self.ui.spinBox_2
        self.total_branches_label = self.ui.label_12

        # Кнопки
        self.save_branch_count_btn = self.ui.pushButton_6
        self.edit_branch_btn = self.ui.pushButton
        self.delete_branch_btn = self.ui.pushButton_3
        self.save_branch_btn = self.ui.pushButton_2
        self.save_all_btn = self.ui.pushButton_4
        self.reset_all_btn = self.ui.pushButton_5
        self.employees_btn = self.ui.toolButton_2
        self.rooms_btn = self.ui.toolButton_4

        # Настройки доступа
        self.users_combo = self.ui.comboBox_3
        self.current_pass_edit = self.ui.lineEdit_3
        self.new_pass_edit = self.ui.lineEdit_4

        self.branch_group.setEnabled(False)

    def setup_connections(self):
        """Подключение сигналов"""
        # Отслеживаем изменения
        self.company_name_edit.textChanged.connect(self.on_change)
        self.branches_spin.valueChanged.connect(self.on_change)
        self.branch_name_edit.textChanged.connect(self.on_change)
        self.branch_address_edit.textChanged.connect(self.on_change)
        self.floors_spin.valueChanged.connect(self.on_change)

        # Кнопки
        self.save_branch_count_btn.clicked.connect(self.save_branches_count)
        self.branches_list.itemClicked.connect(self.on_branch_selected)
        self.edit_branch_btn.clicked.connect(lambda: self.branch_group.setEnabled(True))
        self.save_branch_btn.clicked.connect(self.save_branch)
        self.delete_branch_btn.clicked.connect(self.delete_branch)
        self.employees_btn.clicked.connect(self.open_employees_dialog)
        self.rooms_btn.clicked.connect(self.open_rooms_dialog)

        # 🔥 ГЛАВНОЕ: кнопка "Сохранить всё" сохраняет ВСЁ
        self.save_all_btn.clicked.connect(self.save_all_changes)

        self.reset_all_btn.clicked.connect(self.reset_all)

    def on_change(self):
        """Отслеживание изменений"""
        self.changes_made = True

    def load_initial_data(self):
        """Загрузка начальных данных"""
        # Загружаем название предприятия
        company_name = self.db.get_company_name()
        self.company_name_edit.setText(company_name)
        self.original_company_name = company_name

        # Загружаем филиалы
        self.load_branches()

        # Загружаем пользователей
        self.load_users()

    def load_branches(self):
        """Загрузка списка филиалов"""
        self.branches_list.clear()
        branches = self.db.get_all_branches()

        for branch in branches:
            item = QListWidgetItem(branch[1])  # name
            item.setData(Qt.UserRole, branch[0])  # branch_id
            self.branches_list.addItem(item)

        self.branches_spin.setValue(len(branches))
        self.total_branches_label.setText(f"Всего филиалов: {len(branches)}")

    def load_users(self):
        """Загрузка пользователей"""
        self.users_combo.clear()
        users = self.db.get_users()
        for user in users:
            self.users_combo.addItem(user[0])

    def save_branches_count(self):
        """Сохранение количества филиалов"""
        current = self.branches_list.count()
        target = self.branches_spin.value()

        if target > current:
            for i in range(current + 1, target + 1):
                self.db.add_branch(f"Филиал №{i}")
            self.load_branches()
            self.changes_made = False
            QMessageBox.information(self, "Успех", f"Добавлено {target - current} филиалов")

    def on_branch_selected(self, item):
        """Выбор филиала"""
        self.current_branch_id = item.data(Qt.UserRole)
        branch = self.db.get_branch(self.current_branch_id)

        if branch:
            self.branch_name_edit.setText(branch[1])
            self.floors_spin.setValue(branch[2])
            self.branch_address_edit.setText(branch[3] or "")
            self.branch_group.setEnabled(True)

            # Подсчитываем сотрудников и комнаты
            employees = self.db.get_employees(self.current_branch_id)
            rooms = self.db.get_rooms(self.current_branch_id)
            self.employees_spin.setValue(len(employees))
            self.rooms_spin.setValue(len(rooms))

    def save_branch(self):
        """Сохранение текущего филиала"""
        if not self.current_branch_id:
            return

        name = self.branch_name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите название филиала")
            return

        self.db.update_branch(
            self.current_branch_id,
            name,
            self.floors_spin.value(),
            self.branch_address_edit.text().strip()
        )

        # Обновляем название в списке
        for i in range(self.branches_list.count()):
            item = self.branches_list.item(i)
            if item.data(Qt.UserRole) == self.current_branch_id:
                item.setText(name)
                break

        QMessageBox.information(self, "Успех", "Филиал сохранен")

    def delete_branch(self):
        """Удаление филиала"""
        if not self.current_branch_id:
            return

        reply = QMessageBox.question(self, "Подтверждение",
                                     "Удалить филиал? Все связанные данные будут потеряны.",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.db.delete_branch(self.current_branch_id)
            self.load_branches()
            self.branch_group.setEnabled(False)
            self.current_branch_id = None
            self.changes_made = True

    def open_employees_dialog(self):
        """Открыть диалог сотрудников"""
        if self.current_branch_id:
            dialog = EmployeesDialog(self.db, self.current_branch_id,
                                     self.branch_name_edit.text(), self)
            dialog.exec()
            # Обновляем счетчик
            employees = self.db.get_employees(self.current_branch_id)
            self.employees_spin.setValue(len(employees))
            self.changes_made = True

    def open_rooms_dialog(self):
        """Открыть диалог комнат"""
        if self.current_branch_id:
            dialog = RoomsDialog(self.db, self.current_branch_id,
                                 self.branch_name_edit.text(), self)
            dialog.exec()
            # Обновляем счетчик
            rooms = self.db.get_rooms(self.current_branch_id)
            self.rooms_spin.setValue(len(rooms))
            self.changes_made = True

    def save_all_changes(self):
        """🔥 Сохраняет ВСЕ изменения в окне"""
        try:
            # 1. Сохраняем название предприятия
            company_name = self.company_name_edit.text().strip()
            if company_name:
                self.db.save_company_name(company_name)

            # 2. Сохраняем текущий филиал, если выбран
            if self.current_branch_id:
                self.save_branch()

            # 3. Проверяем изменение количества филиалов
            current_count = self.branches_list.count()
            target_count = self.branches_spin.value()

            if target_count != current_count:
                self.save_branches_count()

            # 4. Сохраняем настройки доступа (пароль)
            current_user = self.users_combo.currentText()
            new_pass = self.new_pass_edit.text().strip()

            if new_pass and current_user:
                username = current_user.split()[0] if '(' in current_user else current_user
                if self.db.change_password(username, new_pass):
                    QMessageBox.information(self, "Успех", "Пароль изменен")
                    self.current_pass_edit.clear()
                    self.new_pass_edit.clear()

            self.changes_made = False
            QMessageBox.information(self, "Успех", "Все изменения сохранены!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить изменения: {str(e)}")

    def reset_all(self):
        """Сброс всех изменений"""
        if self.changes_made:
            reply = QMessageBox.question(self, "Подтверждение",
                                         "Сбросить все изменения? Несохраненные данные будут потеряны.",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                return

        self.load_initial_data()
        self.branch_group.setEnabled(False)
        self.current_branch_id = None
        self.current_pass_edit.clear()
        self.new_pass_edit.clear()
        self.changes_made = False


def main():
    app = QApplication(sys.argv)

    print(f"Используется БД: {db_path}")
    print(f"Файл БД существует: {os.path.exists(db_path)}")

    # Проверяем структуру БД
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print("Существующие таблицы:")
        for table in tables:
            print(f"  - {table[0]}")
        conn.close()
    except Exception as e:
        print(f"Ошибка при проверке БД: {e}")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()