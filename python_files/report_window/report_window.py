import sys
import os
import sqlite3
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QTableWidget, QTableWidgetItem, QHeaderView,
                               QPushButton, QHBoxLayout, QVBoxLayout, QWidget,
                               QComboBox, QSpinBox, QCheckBox, QLineEdit,
                               QTextEdit, QGroupBox, QLabel, QProgressBar,
                               QTabWidget, QAbstractItemView, QDialog, QFormLayout,
                               QDialogButtonBox, QFileDialog, QScrollArea, QGridLayout,
                               QDoubleSpinBox, QDateEdit, QDateTimeEdit, QPlainTextEdit,
                               QListView, QMenuBar, QMenu, QSplitter, QFrame)
from PySide6.QtCore import Qt, QDate, QDateTime, Signal, Slot, QFile, QIODevice, QStringListModel
from PySide6.QtGui import QAction, QIcon, QFont, QStandardItemModel, QStandardItem
from PySide6.QtUiTools import QUiLoader

# Добавляем путь к папке settings
settings_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "settings")
if settings_path not in sys.path:
    sys.path.insert(0, settings_path)
    print(f"✅ Добавлен путь к настройкам: {settings_path}")

# Пробуем импортировать настройки
try:
    from settings import MainWindow as SettingsWindow
    SETTINGS_AVAILABLE = True
    print("✅ Модуль настроек загружен")
except ImportError as e:
    print(f"❌ Ошибка загрузки настроек: {e}")
    SETTINGS_AVAILABLE = False
    SettingsWindow = None

# Путь к БД
python_files_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(python_files_dir, "database", "database", "company.db")
ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ReportWindow.ui")

print(f"Путь к БД: {db_path}")
print(f"Файл БД существует: {os.path.exists(db_path)}")
print(f"Путь к UI: {ui_path}")
print(f"Файл UI существует: {os.path.exists(ui_path)}")


# ========== КЛАСС ДЛЯ РАБОТЫ С БД ==========
class DatabaseHandler:
    """Класс для работы с БД"""

    def __init__(self, db_path):
        self.db_path = db_path
        print("✅ DatabaseHandler инициализирован")

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    # ========== ПРЕДПРИЯТИЕ ==========
    def get_company_name(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT name FROM company LIMIT 1")
            result = cursor.fetchone()
            return result[0] if result else "ГБОУ Больница 2 г. Апшеронск"
        except:
            return "ГБОУ Больница 2 г. Апшеронск"
        finally:
            conn.close()

    # ========== ФИЛИАЛЫ ==========
    def get_all_branches(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT branch_id, name FROM branches")
        branches = cursor.fetchall()
        conn.close()
        return branches

    def get_branch(self, branch_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT branch_id, name, floors_count FROM branches WHERE branch_id = ?", (branch_id,))
        branch = cursor.fetchone()
        conn.close()
        return branch

    # ========== СОТРУДНИКИ ==========
    def get_employees(self, branch_id=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        if branch_id:
            cursor.execute("""
                           SELECT worker_id, name_id, job_title
                           FROM employees
                           WHERE branch_id = ?
                           ORDER BY name_id
                           """, (branch_id,))
        else:
            cursor.execute("SELECT worker_id, name_id, job_title FROM employees ORDER BY name_id")
        employees = cursor.fetchall()
        conn.close()
        return employees

    def get_employee(self, worker_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT worker_id, name_id, job_title FROM employees WHERE worker_id = ?", (worker_id,))
        emp = cursor.fetchone()
        conn.close()
        return emp

    # ========== КОМНАТЫ ==========
    def get_rooms_by_branch_and_floor(self, branch_id, floor):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT room_id, room_number, room_name, capacity, desks_count,
                              chairs_count, sockets_count, area
                       FROM room
                       WHERE branch_id = ? AND floor = ?
                       ORDER BY room_number
                       """, (branch_id, floor))
        rooms = cursor.fetchall()
        conn.close()
        return rooms

    def get_room(self, room_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT room_id, room_number, room_name, floor, capacity,
                              desks_count, chairs_count, sockets_count, area,
                              responsible_employee_id, notes
                       FROM room
                       WHERE room_id = ?
                       """, (room_id,))
        room = cursor.fetchone()
        conn.close()
        return room

    # ========== ОБОРУДОВАНИЕ ==========
    def get_equipment_by_room(self, room_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT equipment_id, name, category, type, serial_number, status
                       FROM equipment
                       WHERE room_id = ?
                       ORDER BY name
                       """, (room_id,))
        equipment = cursor.fetchall()
        conn.close()
        return equipment

    def get_all_equipment(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT e.equipment_id, e.name, e.category, e.type, e.serial_number,
                              e.status, r.room_number, r.room_name, b.name as branch_name
                       FROM equipment e
                                LEFT JOIN room r ON e.room_id = r.room_id
                                LEFT JOIN branches b ON r.branch_id = b.branch_id
                       ORDER BY e.name
                       """)
        equipment = cursor.fetchall()
        conn.close()
        return equipment

    def add_equipment(self, data):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO equipment (
                           name, category, type, quantity, serial_number,
                           supplier, price, date_incoming, state_incoming,
                           phone_supplier, email_supplier, status, notes
                       ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, (
                           data.get('name', ''),
                           data.get('category', ''),
                           data.get('type', ''),
                           data.get('quantity', 1),
                           data.get('serial_number', ''),
                           data.get('supplier', ''),
                           data.get('price', 0),
                           data.get('date_incoming', datetime.now().strftime("%Y-%m-%d")),
                           data.get('state_incoming', 1),
                           data.get('phone_supplier', ''),
                           data.get('email_supplier', ''),
                           data.get('status', 'in_use'),
                           data.get('notes', '')
                       ))
        equip_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return equip_id

    def update_equipment_room(self, equipment_id, room_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE equipment SET room_id = ? WHERE equipment_id = ?", (room_id, equipment_id))
        conn.commit()
        conn.close()

    # ========== ОТЧЕТЫ ==========
    def add_report(self, report_data):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO reports (
                           report_name, report_date, description, order_number,
                           worker_id, environment_id
                       ) VALUES (?, ?, ?, ?, ?, ?)
                       """, (
                           report_data.get('name', ''),
                           report_data.get('date', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                           report_data.get('description', ''),
                           report_data.get('order_number', 0),
                           report_data.get('worker_id'),
                           report_data.get('environment_id')
                       ))
        report_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return report_id

    def get_all_reports(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT report_id, report_name, report_date, description, order_number
                       FROM reports
                       ORDER BY report_date DESC
                       """)
        reports = cursor.fetchall()
        conn.close()
        return reports

    def get_report(self, report_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT report_id, report_name, report_date, description, order_number,
                              worker_id, environment_id
                       FROM reports
                       WHERE report_id = ?
                       """, (report_id,))
        report = cursor.fetchone()
        conn.close()
        return report

    # ========== ИНВЕНТАРИЗАЦИЯ ==========
    def add_inventory_log(self, log_data):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO inventory_log (
                           report_id, equipment_id, old_status, new_status,
                           comment, worker_id
                       ) VALUES (?, ?, ?, ?, ?, ?)
                       """, (
                           log_data.get('report_id'),
                           log_data.get('equipment_id'),
                           log_data.get('old_status'),
                           log_data.get('new_status'),
                           log_data.get('comment', ''),
                           log_data.get('worker_id')
                       ))
        log_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return log_id

    # ========== ПОЛЬЗОВАТЕЛИ ==========
    def get_users(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT username FROM users")
            users = cursor.fetchall()
        except:
            users = []
        conn.close()
        return users


# ========== ДИАЛОГ СПИСКА ОТЧЕТОВ ==========
class ReportsListDialog(QDialog):
    """Диалог со списком всех отчетов"""

    def __init__(self, db, parent=None):
        super().__init__(parent)
        self.db = db
        self.selected_report_id = None
        self.setWindowTitle("Список отчетов")
        self.setMinimumSize(800, 500)

        layout = QVBoxLayout(self)

        # Таблица отчетов
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Название", "Дата", "Описание", "№ приказа"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.doubleClicked.connect(self.open_report)
        layout.addWidget(self.table)

        # Кнопки
        btn_layout = QHBoxLayout()
        open_btn = QPushButton("Открыть")
        open_btn.clicked.connect(self.open_report)
        cancel_btn = QPushButton("Закрыть")
        cancel_btn.clicked.connect(self.reject)

        btn_layout.addWidget(open_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

        self.load_reports()

    def load_reports(self):
        reports = self.db.get_all_reports()
        self.table.setRowCount(len(reports))

        for i, report in enumerate(reports):
            self.table.setItem(i, 0, QTableWidgetItem(str(report[0])))
            self.table.setItem(i, 1, QTableWidgetItem(report[1]))
            self.table.setItem(i, 2, QTableWidgetItem(report[2]))
            self.table.setItem(i, 3, QTableWidgetItem(report[3]))
            self.table.setItem(i, 4, QTableWidgetItem(str(report[4])))

    def open_report(self):
        selected = self.table.currentRow()
        if selected >= 0:
            self.selected_report_id = int(self.table.item(selected, 0).text())
            self.accept()


# ========== ДИАЛОГ ПОДТВЕРЖДЕНИЯ ==========
class ConfirmationDialog(QDialog):
    """Диалог подтверждения действия"""

    def __init__(self, message="Вы уверены?", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Подтверждение")
        self.setMinimumWidth(300)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(message))

        btn_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)


# ========== ДИАЛОГ СОХРАНЕНИЯ ==========
class SaveConfirmationDialog(QDialog):
    """Диалог сохранения перед новым документом"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Сохранение")
        self.setMinimumWidth(350)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Сохранить изменения?"))

        btn_box = QDialogButtonBox()
        btn_save = btn_box.addButton("Сохранить", QDialogButtonBox.AcceptRole)
        btn_discard = btn_box.addButton("Не сохранять", QDialogButtonBox.DestructiveRole)
        btn_cancel = btn_box.addButton("Отмена", QDialogButtonBox.RejectRole)

        btn_save.clicked.connect(lambda: self.done(1))
        btn_discard.clicked.connect(lambda: self.done(2))
        btn_cancel.clicked.connect(self.reject)

        layout.addWidget(btn_box)


# ========== ДИАЛОГ НОВОГО РАБОЧЕГО МЕСТА ==========
class WorkplaceDialog(QDialog):
    """Диалог для создания/редактирования рабочего места"""

    def __init__(self, db, room_id, workplace_number, parent=None):
        super().__init__(parent)
        self.db = db
        self.room_id = room_id
        self.workplace_number = workplace_number
        self.setWindowTitle(f"Рабочее место №{workplace_number}")
        self.setMinimumWidth(400)

        layout = QVBoxLayout(self)

        # Форма
        form = QFormLayout()

        self.equipment_type = QComboBox()
        self.equipment_type.addItems(["Компьютер", "Монитор", "Ноутбук", "Принтер", "МФУ", "Другое"])
        form.addRow("Тип оборудования:", self.equipment_type)

        self.equipment_name = QLineEdit()
        form.addRow("Название:", self.equipment_name)

        self.serial_number = QLineEdit()
        form.addRow("Серийный номер:", self.serial_number)

        self.has_monitor = QCheckBox("Есть монитор")
        form.addRow("", self.has_monitor)

        self.has_keyboard = QCheckBox("Есть клавиатура")
        form.addRow("", self.has_keyboard)

        self.has_mouse = QCheckBox("Есть мышь")
        form.addRow("", self.has_mouse)

        self.has_power_cable = QCheckBox("Есть кабель питания")
        form.addRow("", self.has_power_cable)

        self.notes = QLineEdit()
        form.addRow("Примечания:", self.notes)

        layout.addLayout(form)

        # Кнопки
        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)

    def get_data(self):
        return {
            'number': self.workplace_number,
            'type': self.equipment_type.currentText(),
            'name': self.equipment_name.text(),
            'serial': self.serial_number.text(),
            'has_monitor': self.has_monitor.isChecked(),
            'has_keyboard': self.has_keyboard.isChecked(),
            'has_mouse': self.has_mouse.isChecked(),
            'has_power_cable': self.has_power_cable.isChecked(),
            'notes': self.notes.text()
        }


# ========== ВИДЖЕТ РАБОЧЕГО МЕСТА ==========
class WorkplaceWidget(QWidget):
    """Виджет для отображения рабочего места"""

    edit_clicked = Signal(int)  # номер места
    delete_clicked = Signal(int)

    def __init__(self, number, data=None):
        super().__init__()
        self.number = number
        self.data = data or {}

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        # Заголовок
        title = QLabel(f"Место №{number}")
        title.setMinimumWidth(80)
        layout.addWidget(title)

        # Информация
        if data and data.get('name'):
            info = QLabel(f"{data.get('type', '')}: {data.get('name', '')}")
            layout.addWidget(info, 1)
        else:
            empty = QLabel("не заполнено")
            empty.setStyleSheet("color: gray; font-style: italic;")
            layout.addWidget(empty, 1)

        # Кнопки
        edit_btn = QPushButton("✏️")
        edit_btn.setMaximumWidth(30)
        edit_btn.clicked.connect(lambda: self.edit_clicked.emit(self.number))

        delete_btn = QPushButton("🗑️")
        delete_btn.setMaximumWidth(30)
        delete_btn.clicked.connect(lambda: self.delete_clicked.emit(self.number))

        layout.addWidget(edit_btn)
        layout.addWidget(delete_btn)


# ========== ГЛАВНОЕ ОКНО ==========
class ReportWindow(QMainWindow):
    """Главное окно отчетности"""

    def __init__(self):
        super().__init__()
        self.db = DatabaseHandler(db_path)
        self.current_report_id = None
        self.current_room_id = None
        self.workplaces_data = {}  # {номер_места: данные}
        self.arrival_items = []  # Список позиций поступления для переноса
        self.distribution_model = None  # Модель для таблицы распределения
        self.settings_window = None  # Для окна настроек
        self.setup_ui()
        self.load_initial_data()
        self.showMaximized()

    def setup_ui(self):
        """Загрузка UI из файла"""
        if not os.path.exists(ui_path):
            QMessageBox.critical(self, "Ошибка", f"Файл UI не найден: {ui_path}")
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

        # НЕ используем меню из UI, создаем свое
        self.create_menu()

        self.setup_tabs()

    def create_menu(self):
        """Создание меню программно"""
        menubar = self.menuBar()

        # Файл
        file_menu = menubar.addMenu("Файл")
        file_menu.addAction("Новая отчетность", self.new_report)
        file_menu.addAction("Новое поступление", self.new_arrival)
        file_menu.addSeparator()
        file_menu.addAction("Сохранить отчет", self.save_report_txt)
        file_menu.addAction("Сохранить как...", self.save_report_as)
        file_menu.addSeparator()
        file_menu.addAction("Полный список отчетов", self.show_reports_list)
        file_menu.addSeparator()
        file_menu.addAction("Выход", self.close)

        # Настройки
        settings_menu = menubar.addMenu("Настройки")
        settings_menu.addAction("Размер шрифта", self.on_font_size)
        settings_menu.addAction("Тема", self.on_theme)
        settings_menu.addSeparator()

        # Настройка окружения - если доступен файл настроек
        if SETTINGS_AVAILABLE:
            settings_menu.addAction("Редактировать рабочее окружение", self.open_settings_window)
        else:
            action = settings_menu.addAction("Редактировать рабочее окружение (недоступно)")
            action.setEnabled(False)

        # Справка
        help_menu = menubar.addMenu("Справка")
        help_menu.addAction("Версия", self.show_version)
        help_menu.addAction("О программе", self.show_project_info)

        # Открыть схему
        schema_menu = menubar.addMenu("Открыть схему")
        schema_menu.addAction("Показать схему", self.show_schema)

        print("✅ Меню создано")

    def open_settings_window(self):
        """Открыть окно настроек из settings.py"""
        if not SETTINGS_AVAILABLE:
            QMessageBox.warning(self, "Ошибка", "Модуль настроек не найден")
            return

        try:
            # Создаем экземпляр окна настроек
            self.settings_window = SettingsWindow()

            # Чтобы окно удалялось при закрытии
            self.settings_window.setAttribute(Qt.WA_DeleteOnClose)

            # Показываем окно
            self.settings_window.show()

            print("✅ Окно настроек открыто")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть настройки:\n{e}")

    def show_schema(self):
        """Показать схему"""
        QMessageBox.information(self, "Схема", "Здесь будет открываться схема")

    def setup_tabs(self):
        """Настройка вкладок"""
        self.setup_arrival_tab()
        self.setup_inventory_tab()
        self.setup_distribution_tab()

    # ========== ВКЛАДКА ПОСТУПЛЕНИЕ ==========
    def setup_arrival_tab(self):
        """Настройка вкладки Поступление"""
        # Заполняем комбобоксы
        self.load_branches_to_combo(self.ui.comboBox_5)
        self.load_branches_to_combo(self.ui.comboBox_6)
        self.load_employees_to_combo(self.ui.comboBox_8)

        # Настройка tableWidget для отображения базы данных поступлений
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels([
            "№", "Название", "Категория", "Тип", "Количество", "Цена", "Серийный №"
        ])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableWidget.setSelectionMode(QTableWidget.MultiSelection)

        # Подключаем кнопки из UI
        if hasattr(self.ui, 'pushButton_5'):
            self.ui.pushButton_5.clicked.connect(self.export_arrival_pdf)
        if hasattr(self.ui, 'pushButton_3'):
            self.ui.pushButton_3.clicked.connect(self.export_arrival_txt)
        if hasattr(self.ui, 'pushButton_2'):
            self.ui.pushButton_2.clicked.connect(self.cancel_arrival)
        if hasattr(self.ui, 'pushButton'):
            self.ui.pushButton.clicked.connect(self.save_arrival)
        if hasattr(self.ui, 'pushButton_16'):
            self.ui.pushButton_16.clicked.connect(self.add_arrival_position)

        # Загружаем существующие поступления
        self.load_arrival_data()

    def load_arrival_data(self):
        """Загрузка данных из БД в таблицу поступлений"""
        try:
            equipment = self.db.get_all_equipment()
            self.ui.tableWidget.setRowCount(0)
            for i, item in enumerate(equipment):
                self.ui.tableWidget.insertRow(i)
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(item[1]))  # name
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(item[2]))  # category
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(item[3]))  # type
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem("1"))  # quantity
                self.ui.tableWidget.setItem(i, 5, QTableWidgetItem("0"))  # price
                self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(item[4]))  # serial_number
            print(f"Загружено позиций: {len(equipment)}")
        except Exception as e:
            print(f"Ошибка загрузки поступлений: {e}")

    def add_arrival_position(self):
        """Добавление позиции в таблицу поступления и БД"""
        data = {
            'name': self.ui.lineEdit_15.text() if hasattr(self.ui, 'lineEdit_15') else "",
            'category': self.ui.comboBox_9.currentText() if hasattr(self.ui, 'comboBox_9') else "",
            'type': self.ui.comboBox_10.currentText() if hasattr(self.ui, 'comboBox_10') else "",
            'quantity': self.ui.spinBox_2.value() if hasattr(self.ui, 'spinBox_2') else 1,
            'serial_number': self.ui.lineEdit_18.text() if hasattr(self.ui, 'lineEdit_18') else "",
            'supplier': self.ui.lineEdit_7.text() if hasattr(self.ui, 'lineEdit_7') else "",
            'price': self.ui.doubleSpinBox.value() if hasattr(self.ui, 'doubleSpinBox') else 0,
            'date_incoming': self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd") if hasattr(self.ui, 'dateTimeEdit') else datetime.now().strftime("%Y-%m-%d"),
            'state_incoming': 1,
            'phone_supplier': self.ui.lineEdit_9.text() if hasattr(self.ui, 'lineEdit_9') else "",
            'email_supplier': self.ui.lineEdit_10.text() if hasattr(self.ui, 'lineEdit_10') else "",
            'notes': self.ui.plainTextEdit.toPlainText() if hasattr(self.ui, 'plainTextEdit') else ""
        }

        if not data['name'] or not data['serial_number']:
            QMessageBox.warning(self, "Ошибка", "Заполните название и серийный номер")
            return

        try:
            equip_id = self.db.add_equipment(data)
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(data['name']))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(data['category']))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(data['type']))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(data['quantity'])))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(data['price'])))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(data['serial_number']))
            self.clear_arrival_form()
            QMessageBox.information(self, "Успех", f"Позиция добавлена (ID: {equip_id})")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {e}")

    def clear_arrival_form(self):
        """Очистка формы поступления"""
        if hasattr(self.ui, 'lineEdit_15'):
            self.ui.lineEdit_15.clear()
        if hasattr(self.ui, 'lineEdit_18'):
            self.ui.lineEdit_18.clear()
        if hasattr(self.ui, 'spinBox_2'):
            self.ui.spinBox_2.setValue(1)
        if hasattr(self.ui, 'doubleSpinBox'):
            self.ui.doubleSpinBox.setValue(0)

    def export_arrival_txt(self):
        """Выгрузка поступления в .txt"""
        if self.ui.tableWidget.rowCount() == 0:
            QMessageBox.warning(self, "Ошибка", "Нет данных для выгрузки")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить отчет", "", "Текстовые файлы (*.txt)"
        )

        if not file_path:
            return

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("=" * 50 + "\n")
                f.write("ОТЧЕТ О ПОСТУПЛЕНИИ\n")
                f.write(f"Дата: {QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')}\n")
                f.write("=" * 50 + "\n\n")

                f.write("ДАННЫЕ ПОСТУПЛЕНИЯ:\n")
                if hasattr(self.ui, 'lineEdit_5'):
                    f.write(f"Название: {self.ui.lineEdit_5.text()}\n")
                if hasattr(self.ui, 'lineEdit_6'):
                    f.write(f"Номер приказа: {self.ui.lineEdit_6.text()}\n")
                if hasattr(self.ui, 'textEdit_4'):
                    f.write(f"Описание: {self.ui.textEdit_4.toPlainText()}\n")

                f.write("\nПОЗИЦИИ:\n")
                f.write("-" * 50 + "\n")
                f.write(f"{'№':<4} {'Название':<20} {'Категория':<15} {'Кол-во':<8} {'Цена':<10}\n")
                f.write("-" * 50 + "\n")

                total = 0
                for row in range(self.ui.tableWidget.rowCount()):
                    num = self.ui.tableWidget.item(row, 0).text() if self.ui.tableWidget.item(row, 0) else ""
                    name = self.ui.tableWidget.item(row, 1).text() if self.ui.tableWidget.item(row, 1) else ""
                    cat = self.ui.tableWidget.item(row, 2).text() if self.ui.tableWidget.item(row, 2) else ""
                    qty = self.ui.tableWidget.item(row, 4).text() if self.ui.tableWidget.item(row, 4) else "0"
                    price = self.ui.tableWidget.item(row, 5).text() if self.ui.tableWidget.item(row, 5) else "0"

                    f.write(f"{num:<4} {name:<20} {cat:<15} {qty:<8} {price:<10}\n")

                    try:
                        total += int(qty) * float(price)
                    except:
                        pass

                f.write("-" * 50 + "\n")
                f.write(f"ИТОГО: {total} руб.\n")

            QMessageBox.information(self, "Успех", f"Отчет сохранен: {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {e}")

    def export_arrival_pdf(self):
        """Заглушка для PDF"""
        QMessageBox.information(self, "Информация", "Функция PDF будет добавлена позже")

    def cancel_arrival(self):
        """Отмена поступления"""
        dlg = ConfirmationDialog("Отменить ввод данных?", self)
        if dlg.exec() == QDialog.Accepted:
            self.clear_arrival_form()

    def save_arrival(self):
        """Сохранение поступления"""
        dlg = ConfirmationDialog("Сохранить все изменения?", self)
        if dlg.exec() == QDialog.Accepted:
            try:
                self.ui.progressBar.setValue(100)
                QMessageBox.information(self, "Успех", "Данные сохранены в БД")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {e}")

    # ========== ВКЛАДКА ИНВЕНТАРИЗАЦИЯ ==========
    def setup_inventory_tab(self):
        """Настройка вкладки Инвентаризация"""
        self.load_branches_to_combo(self.ui.comboBox_3)
        self.load_branches_to_combo(self.ui.comboBox_4)
        self.load_employees_to_combo(self.ui.comboBox)
        self.load_employees_to_combo(self.ui.comboBox_2)

        if hasattr(self.ui, 'comboBox_4'):
            self.ui.comboBox_4.currentIndexChanged.connect(self.on_branch_changed_inventory)
        if hasattr(self.ui, 'spinBox_3'):
            self.ui.spinBox_3.valueChanged.connect(self.on_floor_changed_inventory)

        if hasattr(self.ui, 'tableView'):
            self.ui.tableView.setModel(QStandardItemModel())
            model = self.ui.tableView.model()
            if model:
                model.setHorizontalHeaderLabels(["ID", "Название", "Категория", "Серийный №", "Статус"])

        if hasattr(self.ui, 'comboBox_12'):
            self.ui.comboBox_12.currentIndexChanged.connect(self.apply_inventory_filters)
        if hasattr(self.ui, 'comboBox_11'):
            self.ui.comboBox_11.currentIndexChanged.connect(self.apply_inventory_filters)
        if hasattr(self.ui, 'lineEdit_20'):
            self.ui.lineEdit_20.textChanged.connect(self.apply_inventory_filters)
        if hasattr(self.ui, 'lineEdit_21'):
            self.ui.lineEdit_21.textChanged.connect(self.apply_inventory_filters)
        if hasattr(self.ui, 'lineEdit_22'):
            self.ui.lineEdit_22.textChanged.connect(self.apply_inventory_filters)

        self.load_categories_to_combo(self.ui.comboBox_12)
        self.load_types_to_combo(self.ui.comboBox_11)

    def on_branch_changed_inventory(self):
        """Изменение филиала во вкладке инвентаризация"""
        branch_id = self.ui.comboBox_4.currentData()
        if branch_id:
            branch = self.db.get_branch(branch_id)
            if branch and hasattr(self.ui, 'spinBox_3'):
                self.ui.spinBox_3.setMaximum(branch[2])

    def on_floor_changed_inventory(self):
        """Изменение этажа во вкладке инвентаризация"""
        branch_id = self.ui.comboBox_4.currentData()
        floor = self.ui.spinBox_3.value() if hasattr(self.ui, 'spinBox_3') else 1
        if branch_id and floor and hasattr(self.ui, 'comboBox_7'):
            self.load_rooms_to_combo(self.ui.comboBox_7, branch_id, floor)

    def apply_inventory_filters(self):
        """Применение фильтров инвентаризации"""
        pass

    # ========== ВКЛАДКА РАСПРЕДЕЛЕНИЕ ==========
    def setup_distribution_tab(self):
        """Настройка вкладки Распределение"""
        self.load_employees_with_position(self.ui.comboBox_13)
        self.load_branches_to_combo(self.ui.comboBox_15)
        self.load_branches_to_combo(self.ui.comboBox_14)

        self.ui.comboBox_14.currentIndexChanged.connect(self.on_branch_changed_distribution)
        self.ui.spinBox_6.valueChanged.connect(self.on_floor_changed_distribution)
        self.ui.comboBox_16.currentIndexChanged.connect(self.on_room_changed_distribution)

        self.setup_workplaces_area()
        self.setup_distribution_table()

        if hasattr(self.ui, 'pushButton_15'):
            self.ui.pushButton_15.clicked.connect(self.transfer_selected_items)
            print("✅ Кнопка переноса подключена")

        self.ui.comboBox_17.currentIndexChanged.connect(self.apply_distribution_filters)
        self.ui.comboBox_18.currentIndexChanged.connect(self.apply_distribution_filters)
        self.ui.lineEdit_27.textChanged.connect(self.apply_distribution_filters)
        self.ui.lineEdit_26.textChanged.connect(self.apply_distribution_filters)
        self.ui.lineEdit_25.textChanged.connect(self.apply_distribution_filters)

        self.load_categories_to_combo(self.ui.comboBox_17)
        self.load_types_to_combo(self.ui.comboBox_18)

        if hasattr(self.ui, 'pushButton_8'):
            self.ui.pushButton_8.clicked.connect(self.save_all_distribution)
        if hasattr(self.ui, 'pushButton_9'):
            self.ui.pushButton_9.clicked.connect(self.delete_all_distribution)
        if hasattr(self.ui, 'pushButton_4'):
            self.ui.pushButton_4.clicked.connect(self.save_room_distribution)
        if hasattr(self.ui, 'pushButton_6'):
            self.ui.pushButton_6.clicked.connect(self.reset_room_distribution)
        if hasattr(self.ui, 'pushButton_7'):
            self.ui.pushButton_7.clicked.connect(self.export_room_report)
        if hasattr(self.ui, 'pushButton_10'):
            self.ui.pushButton_10.clicked.connect(self.export_final_report)

    def setup_distribution_table(self):
        """Настройка таблицы для распределения"""
        self.distribution_model = QStandardItemModel()
        self.distribution_model.setHorizontalHeaderLabels([
            "ID", "Название", "Категория", "Тип", "Серийный №", "Выбрать"
        ])
        self.ui.tableView_2.setModel(self.distribution_model)
        self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableView_2.setSelectionMode(QAbstractItemView.MultiSelection)
        self.load_distribution_equipment()

    def load_distribution_equipment(self):
        """Загрузка оборудования для распределения"""
        try:
            equipment = self.db.get_all_equipment()
            self.distribution_model.removeRows(0, self.distribution_model.rowCount())
            for item in equipment:
                row = []
                id_item = QStandardItem(str(item[0]))
                id_item.setEditable(False)
                row.append(id_item)
                name_item = QStandardItem(item[1])
                name_item.setEditable(False)
                row.append(name_item)
                cat_item = QStandardItem(item[2])
                cat_item.setEditable(False)
                row.append(cat_item)
                type_item = QStandardItem(item[3])
                type_item.setEditable(False)
                row.append(type_item)
                serial_item = QStandardItem(item[4])
                serial_item.setEditable(False)
                row.append(serial_item)
                check_item = QStandardItem()
                check_item.setCheckable(True)
                check_item.setEditable(False)
                row.append(check_item)
                self.distribution_model.appendRow(row)
            print(f"Загружено оборудования для распределения: {len(equipment)}")
        except Exception as e:
            print(f"Ошибка загрузки оборудования: {e}")

    def transfer_selected_items(self):
        """Перенос выбранных позиций в рабочее место"""
        if not self.current_room_id:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите комнату")
            return

        selected_ids = []
        for row in range(self.distribution_model.rowCount()):
            check_item = self.distribution_model.item(row, 5)
            if check_item and check_item.checkState() == Qt.Checked:
                id_item = self.distribution_model.item(row, 0)
                if id_item:
                    selected_ids.append(int(id_item.text()))

        if not selected_ids:
            QMessageBox.warning(self, "Ошибка", "Выберите позиции для переноса")
            return

        free_spot = None
        room = self.db.get_room(self.current_room_id)
        capacity = room[4] if room else 10

        for i in range(1, capacity + 1):
            if i not in self.workplaces_data:
                free_spot = i
                break

        if not free_spot:
            QMessageBox.warning(self, "Ошибка", "Нет свободных мест")
            return

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, category, type, serial_number FROM equipment WHERE equipment_id = ?",
                       (selected_ids[0],))
        equip = cursor.fetchone()
        conn.close()

        if equip:
            data = {
                'type': equip[2] if equip[2] else "Оборудование",
                'name': equip[1],
                'serial': equip[3],
                'has_monitor': False,
                'has_keyboard': False,
                'has_mouse': False,
                'has_power_cable': True,
                'notes': f"ID в БД: {selected_ids[0]}"
            }
            self.workplaces_data[free_spot] = data
            self.update_workplace_widget(free_spot, data)
            self.db.update_equipment_room(selected_ids[0], self.current_room_id)

            for row in range(self.distribution_model.rowCount()):
                id_item = self.distribution_model.item(row, 0)
                if id_item and int(id_item.text()) in selected_ids:
                    check_item = self.distribution_model.item(row, 5)
                    if check_item:
                        check_item.setCheckState(Qt.Unchecked)

            QMessageBox.information(self, "Успех", f"Позиция перенесена на место №{free_spot}")

    def on_branch_changed_distribution(self):
        """Изменение филиала во вкладке распределение"""
        branch_id = self.ui.comboBox_14.currentData()
        if branch_id:
            branch = self.db.get_branch(branch_id)
            if branch:
                self.ui.spinBox_6.setMaximum(branch[2])
                self.load_distribution_equipment()

    def on_floor_changed_distribution(self):
        """Изменение этажа во вкладке распределение"""
        branch_id = self.ui.comboBox_14.currentData()
        floor = self.ui.spinBox_6.value()
        if branch_id and floor:
            self.load_rooms_to_combo(self.ui.comboBox_16, branch_id, floor)

    def on_room_changed_distribution(self):
        """Изменение комнаты - создаем рабочие места"""
        room_id = self.ui.comboBox_16.currentData()
        if not room_id:
            return
        self.current_room_id = room_id
        room = self.db.get_room(room_id)
        if room:
            capacity = room[4]
            self.create_workplaces(capacity)

    def apply_distribution_filters(self):
        """Применение фильтров распределения"""
        category = self.ui.comboBox_17.currentData()
        type_ = self.ui.comboBox_18.currentData()
        name_filter = self.ui.lineEdit_27.text().lower()

        for row in range(self.distribution_model.rowCount()):
            show = True
            if category and category != "Все категории":
                cat_item = self.distribution_model.item(row, 2)
                if cat_item and cat_item.text() != category:
                    show = False
            if show and type_ and type_ != "Все типы":
                type_item = self.distribution_model.item(row, 3)
                if type_item and type_item.text() != type_:
                    show = False
            if show and name_filter:
                name_item = self.distribution_model.item(row, 1)
                if name_item and name_filter not in name_item.text().lower():
                    show = False
            self.ui.tableView_2.setRowHidden(row, not show)

    def save_room_distribution(self):
        """Сохранение распределения для комнаты"""
        if not self.current_room_id:
            QMessageBox.warning(self, "Ошибка", "Выберите комнату")
            return
        dlg = ConfirmationDialog("Сохранить распределение для этой комнаты?", self)
        if dlg.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Успех", "Распределение сохранено")

    def reset_room_distribution(self):
        """Сброс распределения для комнаты"""
        dlg = ConfirmationDialog("Сбросить распределение для этой комнаты?", self)
        if dlg.exec() == QDialog.Accepted:
            self.workplaces_data.clear()
            room_id = self.ui.comboBox_16.currentData()
            if room_id:
                room = self.db.get_room(room_id)
                if room:
                    self.create_workplaces(room[4])

    def save_all_distribution(self):
        """Сохранение всего распределения"""
        dlg = ConfirmationDialog("Сохранить все распределения?", self)
        if dlg.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Успех", "Все распределения сохранены")

    def delete_all_distribution(self):
        """Удаление всего распределения"""
        dlg = ConfirmationDialog("Удалить все распределения?", self)
        if dlg.exec() == QDialog.Accepted:
            self.workplaces_data.clear()
            self.clear_workplaces()

    def export_room_report(self):
        """Выгрузка отчетности по комнате в .txt"""
        room_id = self.ui.comboBox_16.currentData()
        if not room_id:
            QMessageBox.warning(self, "Ошибка", "Выберите комнату")
            return

        room = self.db.get_room(room_id)
        if not room:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить отчет по комнате", "", "Текстовые файлы (*.txt)"
        )

        if not file_path:
            return

        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("=" * 50 + "\n")
                f.write(f"ОТЧЕТ ПО КОМНАТЕ: {room[1]} - {room[2]}\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Этаж: {room[3]}\n")
                f.write(f"Вместимость: {room[4]} чел.\n")
                f.write(f"Столов: {room[5]}, Стульев: {room[6]}\n")
                f.write(f"Розеток: {room[7]}, Площадь: {room[8]} м²\n\n")
                f.write("РАБОЧИЕ МЕСТА:\n")
                f.write("-" * 50 + "\n")
                for i in range(1, room[4] + 1):
                    data = self.workplaces_data.get(i, {})
                    f.write(f"\nМесто №{i}:\n")
                    if data:
                        f.write(f"  Тип: {data.get('type', '')}\n")
                        f.write(f"  Название: {data.get('name', '')}\n")
                        f.write(f"  Серийный номер: {data.get('serial', '')}\n")
                        f.write(f"  Комплектация: ")
                        items = []
                        if data.get('has_monitor'): items.append("монитор")
                        if data.get('has_keyboard'): items.append("клавиатура")
                        if data.get('has_mouse'): items.append("мышь")
                        if data.get('has_power_cable'): items.append("кабель питания")
                        f.write(", ".join(items) if items else "нет")
                        f.write("\n")
                        if data.get('notes'):
                            f.write(f"  Примечания: {data['notes']}\n")
                    else:
                        f.write("  не заполнено\n")
                f.write("\n" + "=" * 50 + "\n")
            QMessageBox.information(self, "Успех", f"Отчет сохранен: {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {e}")

    def export_final_report(self):
        """Выгрузка финальной отчетности"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить финальный отчет", "", "Текстовые файлы (*.txt)"
        )
        if not file_path:
            return
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("=" * 50 + "\n")
                f.write("ФИНАЛЬНЫЙ ОТЧЕТ ПО РАСПРЕДЕЛЕНИЮ\n")
                f.write(f"Дата: {QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')}\n")
                f.write("=" * 50 + "\n\n")
                if self.current_room_id:
                    room = self.db.get_room(self.current_room_id)
                    if room:
                        f.write(f"Комната: {room[1]} - {room[2]}\n")
                        f.write(f"Заполнено мест: {len(self.workplaces_data)} из {room[4]}\n\n")
                        for num, data in self.workplaces_data.items():
                            f.write(f"Место {num}: {data.get('name', 'не заполнено')}\n")
            QMessageBox.information(self, "Успех", f"Отчет сохранен: {file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {e}")

    def setup_workplaces_area(self):
        """Настройка области для динамических рабочих мест"""
        self.workplaces_scroll = QScrollArea()
        self.workplaces_scroll.setWidgetResizable(True)
        self.workplaces_scroll.setMinimumHeight(300)
        self.workplaces_container = QWidget()
        self.workplaces_layout = QVBoxLayout(self.workplaces_container)
        self.workplaces_layout.addStretch()
        self.workplaces_scroll.setWidget(self.workplaces_container)
        if hasattr(self.ui, 'groupBox_15'):
            layout = self.ui.groupBox_15.layout()
            if layout:
                while layout.count():
                    item = layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()
            else:
                layout = QVBoxLayout(self.ui.groupBox_15)
            layout.addWidget(self.workplaces_scroll)

    def create_workplaces(self, count):
        """Создание рабочих мест по количеству"""
        self.clear_workplaces()
        for i in range(1, count + 1):
            widget = WorkplaceWidget(i, self.workplaces_data.get(i))
            widget.edit_clicked.connect(self.edit_workplace)
            widget.delete_clicked.connect(self.delete_workplace)
            self.workplaces_layout.insertWidget(self.workplaces_layout.count() - 1, widget)

    def clear_workplaces(self):
        """Очистка всех рабочих мест"""
        while self.workplaces_layout.count() > 1:
            item = self.workplaces_layout.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()

    def edit_workplace(self, number):
        """Редактирование рабочего места"""
        dlg = WorkplaceDialog(self.db, self.current_room_id, number, self)
        if dlg.exec() == QDialog.Accepted:
            data = dlg.get_data()
            self.workplaces_data[number] = data
            self.update_workplace_widget(number, data)

    def update_workplace_widget(self, number, data):
        """Обновление виджета рабочего места"""
        for i in range(self.workplaces_layout.count()):
            item = self.workplaces_layout.itemAt(i)
            if item and item.widget() and isinstance(item.widget(), WorkplaceWidget):
                if item.widget().number == number:
                    new_widget = WorkplaceWidget(number, data)
                    new_widget.edit_clicked.connect(self.edit_workplace)
                    new_widget.delete_clicked.connect(self.delete_workplace)
                    self.workplaces_layout.replaceWidget(item.widget(), new_widget)
                    item.widget().deleteLater()
                    break

    def delete_workplace(self, number):
        """Удаление рабочего места"""
        dlg = ConfirmationDialog(f"Удалить рабочее место №{number}?", self)
        if dlg.exec() == QDialog.Accepted:
            if number in self.workplaces_data:
                del self.workplaces_data[number]
            self.update_workplace_widget(number, None)

    # ========== ОБЩИЕ МЕТОДЫ ==========
    def load_initial_data(self):
        """Загрузка начальных данных"""
        print("Загрузка начальных данных...")
        self.load_branches_to_combo(self.ui.comboBox_5)
        self.load_branches_to_combo(self.ui.comboBox_6)
        self.load_employees_to_combo(self.ui.comboBox_8)
        self.load_branches_to_combo(self.ui.comboBox_3)
        self.load_branches_to_combo(self.ui.comboBox_4)
        self.load_employees_to_combo(self.ui.comboBox)
        self.load_employees_to_combo(self.ui.comboBox_2)
        self.load_employees_with_position(self.ui.comboBox_13)
        self.load_branches_to_combo(self.ui.comboBox_15)
        self.load_branches_to_combo(self.ui.comboBox_14)
        self.load_categories_to_combo(self.ui.comboBox_9)
        self.load_types_to_combo(self.ui.comboBox_10)
        if hasattr(self.ui, 'dateTimeEdit'):
            self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.progressBar.setValue(0)
        print("Загрузка данных завершена")

    def load_branches_to_combo(self, combo):
        """Загрузка филиалов в комбобокс"""
        if not combo:
            return
        combo.clear()
        combo.addItem("Выберите филиал", None)
        try:
            branches = self.db.get_all_branches()
            for branch in branches:
                combo.addItem(branch[1], branch[0])
        except Exception as e:
            print(f"Ошибка загрузки филиалов: {e}")

    def load_employees_to_combo(self, combo):
        """Загрузка сотрудников в комбобокс"""
        if not combo:
            return
        combo.clear()
        combo.addItem("Выберите сотрудника", None)
        try:
            employees = self.db.get_employees()
            for emp in employees:
                combo.addItem(f"{emp[1]} ({emp[2]})", emp[0])
        except Exception as e:
            print(f"Ошибка загрузки сотрудников: {e}")

    def load_employees_with_position(self, combo):
        """Загрузка сотрудников с разделением ФИО и должности"""
        if not combo:
            return
        combo.clear()
        combo.addItem("Выберите сотрудника", None)
        try:
            employees = self.db.get_employees()
            for emp in employees:
                combo.addItem(emp[1], emp[0])
        except Exception as e:
            print(f"Ошибка загрузки сотрудников: {e}")

    def load_categories_to_combo(self, combo):
        """Загрузка категорий оборудования"""
        if not combo:
            return
        combo.clear()
        combo.addItem("Все категории", None)
        categories = ["Оргтехника", "Мебель", "Медицинское", "Инструменты", "Расходные материалы"]
        for cat in categories:
            combo.addItem(cat, cat)

    def load_types_to_combo(self, combo):
        """Загрузка типов оборудования"""
        if not combo:
            return
        combo.clear()
        combo.addItem("Все типы", None)
        types = ["Ноутбук", "Компьютер", "Принтер", "Монитор", "Стол", "Стул", "Кровать", "Холодильник"]
        for t in types:
            combo.addItem(t, t)

    def load_rooms_to_combo(self, combo, branch_id, floor):
        """Загрузка комнат в комбобокс"""
        if not combo:
            return
        combo.clear()
        combo.addItem("Выберите комнату", None)
        if branch_id and floor:
            try:
                rooms = self.db.get_rooms_by_branch_and_floor(branch_id, floor)
                for room in rooms:
                    combo.addItem(f"{room[1]} - {room[2]}", room[0])
                print(f"Загружено комнат: {len(rooms)}")
            except Exception as e:
                print(f"Ошибка загрузки комнат: {e}")

    # ========== МЕТОДЫ МЕНЮ ==========
    def new_report(self):
        """Новая отчетность"""
        dlg = SaveConfirmationDialog(self)
        result = dlg.exec()
        if result == 1:
            self.save_report_txt()
            self.clear_all()
        elif result == 2:
            self.clear_all()

    def new_arrival(self):
        """Новое поступление"""
        dlg = SaveConfirmationDialog(self)
        result = dlg.exec()
        if result == 1:
            self.save_arrival()
            self.clear_arrival_tab()
        elif result == 2:
            self.clear_arrival_tab()

    def save_report_txt(self):
        """Сохранить отчет в .txt"""
        current_tab = self.ui.tabWidget.currentIndex()
        if current_tab == 0:
            self.export_room_report()
        elif current_tab == 1:
            QMessageBox.information(self, "Информация", "Сохранение отчета инвентаризации")
        elif current_tab == 2:
            self.export_arrival_txt()

    def save_report_as(self):
        """Сохранить как"""
        self.save_report_txt()

    def show_reports_list(self):
        """Показать список отчетов"""
        dlg = ReportsListDialog(self.db, self)
        if dlg.exec() == QDialog.Accepted and dlg.selected_report_id:
            report_id = dlg.selected_report_id
            report = self.db.get_report(report_id)
            if report:
                QMessageBox.information(self, "Отчет",
                                        f"ID: {report[0]}\nНазвание: {report[1]}\nДата: {report[2]}")

    def on_font_size(self):
        QMessageBox.information(self, "Информация", "Функция изменения шрифта будет добавлена позже")

    def on_theme(self):
        QMessageBox.information(self, "Информация", "Функция изменения темы будет добавлена позже")

    def show_version(self):
        QMessageBox.information(self, "Версия", "Версия 1.0\nДипломный проект 2026")

    def show_project_info(self):
        QMessageBox.information(self, "Информация о проекте",
                                "Дипломный проект\n"
                                "Тема: Система учета оборудования\n"
                                "Разработчик: ...\n"
                                "Telegram: @katwell1\n\n"
                                "© 2026")

    def open_environment_settings(self):
        """Открыть настройки окружения (старый метод)"""
        self.open_settings_window()

    def clear_all(self):
        self.clear_arrival_tab()
        self.clear_inventory_tab()
        self.clear_distribution_tab()

    def clear_arrival_tab(self):
        if hasattr(self.ui, 'lineEdit_5'):
            self.ui.lineEdit_5.setText("Поступление № ")
        if hasattr(self.ui, 'textEdit_4'):
            self.ui.textEdit_4.clear()
        if hasattr(self.ui, 'lineEdit_6'):
            self.ui.lineEdit_6.clear()
        if hasattr(self.ui, 'plainTextEdit'):
            self.ui.plainTextEdit.clear()

    def clear_inventory_tab(self):
        if hasattr(self.ui, 'lineEdit'):
            self.ui.lineEdit.clear()
        if hasattr(self.ui, 'textEdit'):
            self.ui.textEdit.clear()
        if hasattr(self.ui, 'lineEdit_3'):
            self.ui.lineEdit_3.clear()
        if hasattr(self.ui, 'textEdit_3'):
            self.ui.textEdit_3.clear()
        if hasattr(self.ui, 'lineEdit_4'):
            self.ui.lineEdit_4.clear()

    def clear_distribution_tab(self):
        if hasattr(self.ui, 'lineEdit_23'):
            self.ui.lineEdit_23.clear()
        if hasattr(self.ui, 'textEdit_5'):
            self.ui.textEdit_5.clear()
        if hasattr(self.ui, 'lineEdit_24'):
            self.ui.lineEdit_24.clear()
        self.workplaces_data.clear()
        self.clear_workplaces()


# ========== ЗАПУСК ==========
def main():
    app = QApplication(sys.argv)

    if not os.path.exists(ui_path):
        QMessageBox.critical(None, "Ошибка", f"Файл интерфейса не найден:\n{ui_path}")
        return

    window = ReportWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()