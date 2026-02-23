import os
import sqlite3
from datetime import datetime


class DatabaseHandler:
    def __init__(self, db_path="database/company.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        print(f"🔄 Подключение к БД: {db_path}")
        self.create_tables()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def create_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        # Таблица филиалов
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS branches (
                                                               branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                               name TEXT NOT NULL,
                                                               floors_count INTEGER NOT NULL,
                                                               address TEXT NOT NULL
                       )
                       ''')

        # Таблица сотрудников
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS employees (
                                                                worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                name_id TEXT NOT NULL,
                                                                job_title TEXT NOT NULL,
                                                                report_count INTEGER NOT NULL,
                                                                date_of_work TEXT NOT NULL,
                                                                branch_id INTEGER,
                                                                phone TEXT,
                                                                email TEXT,
                                                                FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE SET NULL
                           )
                       ''')

        # Таблица окружения
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS environment (
                                                                  environment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                  environment_name TEXT NOT NULL,
                                                                  branch_id INTEGER NOT NULL,
                                                                  FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE
                           )
                       ''')

        # ========== ГЛАВНОЕ: ПОЛНАЯ ТАБЛИЦА room ==========
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS room (
                                                           room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           room_number TEXT NOT NULL,
                                                           room_name TEXT NOT NULL,
                                                           branch_id INTEGER,
                                                           floor INTEGER DEFAULT 1,
                                                           capacity INTEGER DEFAULT 0,
                                                           desks_count INTEGER DEFAULT 0,
                                                           chairs_count INTEGER DEFAULT 0,
                                                           sockets_count INTEGER DEFAULT 0,
                                                           area REAL DEFAULT 0.0,
                                                           responsible_employee_id INTEGER,
                                                           notes TEXT DEFAULT '',
                                                           FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE,
                           FOREIGN KEY (responsible_employee_id) REFERENCES employees(worker_id) ON DELETE SET NULL
                           )
                       ''')

        # Таблица оборудования
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS equipment (
                                                                equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                quantity INTEGER NOT NULL,
                                                                category TEXT NOT NULL,
                                                                type TEXT NOT NULL,
                                                                name TEXT NOT NULL,
                                                                date_incoming INTEGER NOT NULL,
                                                                state_incoming INTEGER NOT NULL,
                                                                serial_number TEXT NOT NULL UNIQUE,
                                                                supplier TEXT NOT NULL,
                                                                price INTEGER NOT NULL,
                                                                phone_supplier TEXT NOT NULL,
                                                                email_supplier TEXT NOT NULL,
                                                                room_id INTEGER,
                                                                branch_id INTEGER,
                                                                status TEXT DEFAULT 'in_use',
                                                                last_inventory_date TEXT,
                                                                notes TEXT,
                                                                FOREIGN KEY (room_id) REFERENCES room(room_id) ON DELETE SET NULL
                           )
                       ''')

        # Таблица отчетов
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS reports (
                                                              report_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                              report_name TEXT NOT NULL,
                                                              report_date TIMESTAMP NOT NULL,
                                                              description TEXT NOT NULL,
                                                              order_number INTEGER NOT NULL,
                                                              worker_id INTEGER,
                                                              environment_id INTEGER,
                                                              equipment_id INTEGER,
                                                              FOREIGN KEY (worker_id) REFERENCES employees(worker_id) ON DELETE SET NULL,
                           FOREIGN KEY (environment_id) REFERENCES environment(environment_id) ON DELETE SET NULL,
                           FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE SET NULL
                           )
                       ''')

        # Таблица лога инвентаризации
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS inventory_log (
                                                                    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                    report_id INTEGER NOT NULL,
                                                                    equipment_id INTEGER NOT NULL,
                                                                    old_status TEXT,
                                                                    new_status TEXT,
                                                                    comment TEXT,
                                                                    inventory_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                                                    worker_id INTEGER,
                                                                    FOREIGN KEY (report_id) REFERENCES reports(report_id) ON DELETE CASCADE,
                           FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE,
                           FOREIGN KEY (worker_id) REFERENCES employees(worker_id) ON DELETE SET NULL
                           )
                       ''')

        # Таблица пользователей
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users (
                                                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            username TEXT UNIQUE NOT NULL,
                                                            password TEXT NOT NULL,
                                                            role TEXT DEFAULT 'user'
                       )
                       ''')

        # Таблица компании
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS company (
                                                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                              name TEXT NOT NULL
                       )
                       ''')

        conn.commit()
        conn.close()
        print("✅ База данных создана/обновлена!")

    # ========== МЕТОДЫ ДЛЯ КОМНАТ ==========

    def get_rooms(self, branch_id=None):
        """Получение всех комнат филиала"""
        conn = self.get_connection()
        cursor = conn.cursor()

        if branch_id:
            cursor.execute("""
                           SELECT
                               r.room_id,
                               r.room_number,
                               r.room_name,
                               r.floor,
                               r.capacity,
                               r.desks_count,
                               r.chairs_count,
                               r.sockets_count,
                               r.area,
                               r.responsible_employee_id,
                               r.notes,
                               e.name_id as responsible_name
                           FROM room r
                                    LEFT JOIN employees e ON r.responsible_employee_id = e.worker_id
                           WHERE r.branch_id = ?
                           ORDER BY r.floor, r.room_number
                           """, (branch_id,))
        else:
            cursor.execute("""
                           SELECT
                               r.room_id,
                               r.room_number,
                               r.room_name,
                               r.floor,
                               r.capacity,
                               r.desks_count,
                               r.chairs_count,
                               r.sockets_count,
                               r.area,
                               r.responsible_employee_id,
                               r.notes,
                               e.name_id as responsible_name
                           FROM room r
                                    LEFT JOIN employees e ON r.responsible_employee_id = e.worker_id
                           ORDER BY r.branch_id, r.floor, r.room_number
                           """)

        rooms = cursor.fetchall()
        conn.close()
        return rooms

    def add_room(self, room_number, room_name, branch_id=None, floor=1,
                 capacity=0, desks_count=0, chairs_count=0, sockets_count=0,
                 area=0.0, responsible_id=None, notes=""):
        """Добавление новой комнаты"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO room (
                           room_number, room_name, branch_id, floor,
                           capacity, desks_count, chairs_count, sockets_count,
                           area, responsible_employee_id, notes
                       ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       """, (
                           room_number, room_name, branch_id, floor,
                           capacity, desks_count, chairs_count, sockets_count,
                           area, responsible_id, notes
                       ))

        room_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return room_id

    def update_room(self, room_id, room_number, room_name, floor=1,
                    capacity=0, desks_count=0, chairs_count=0, sockets_count=0,
                    area=0.0, responsible_id=None, notes=""):
        """Обновление комнаты"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                       UPDATE room SET
                                       room_number = ?,
                                       room_name = ?,
                                       floor = ?,
                                       capacity = ?,
                                       desks_count = ?,
                                       chairs_count = ?,
                                       sockets_count = ?,
                                       area = ?,
                                       responsible_employee_id = ?,
                                       notes = ?
                       WHERE room_id = ?
                       """, (
                           room_number, room_name, floor,
                           capacity, desks_count, chairs_count,
                           sockets_count, area, responsible_id,
                           notes, room_id
                       ))

        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success

    def delete_room(self, room_id):
        """Удаление комнаты"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Сначала обновляем оборудование
        cursor.execute("UPDATE equipment SET room_id = NULL WHERE room_id = ?", (room_id,))
        # Удаляем комнату
        cursor.execute("DELETE FROM room WHERE room_id = ?", (room_id,))

        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success

    def get_room(self, room_id):
        """Получение комнаты по ID"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                       SELECT
                           r.room_id,
                           r.room_number,
                           r.room_name,
                           r.floor,
                           r.capacity,
                           r.desks_count,
                           r.chairs_count,
                           r.sockets_count,
                           r.area,
                           r.responsible_employee_id,
                           r.notes,
                           e.name_id as responsible_name,
                           r.branch_id
                       FROM room r
                                LEFT JOIN employees e ON r.responsible_employee_id = e.worker_id
                       WHERE r.room_id = ?
                       """, (room_id,))

        room = cursor.fetchone()
        conn.close()
        return room

    # ========== МЕТОДЫ ДЛЯ ФИЛИАЛОВ ==========

    def get_all_branches(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT branch_id, name, floors_count, address FROM branches")
        branches = cursor.fetchall()
        conn.close()
        return branches

    def get_branch(self, branch_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT branch_id, name, floors_count, address FROM branches WHERE branch_id = ?", (branch_id,))
        branch = cursor.fetchone()
        conn.close()
        return branch

    def add_branch(self, name, floors_count=1, address=''):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO branches (name, floors_count, address) VALUES (?, ?, ?)",
                       (name, floors_count, address))
        branch_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return branch_id

    def update_branch(self, branch_id, name, floors_count, address):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE branches SET name = ?, floors_count = ?, address = ? WHERE branch_id = ?",
                       (name, floors_count, address, branch_id))
        conn.commit()
        conn.close()

    def delete_branch(self, branch_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM branches WHERE branch_id = ?", (branch_id,))
        conn.commit()
        conn.close()

    # ========== МЕТОДЫ ДЛЯ СОТРУДНИКОВ ==========

    def get_employees(self, branch_id=None):
        conn = self.get_connection()
        cursor = conn.cursor()

        if branch_id:
            cursor.execute("""
                           SELECT worker_id, name_id, job_title, report_count, date_of_work
                           FROM employees WHERE branch_id = ?
                           ORDER BY name_id
                           """, (branch_id,))
        else:
            cursor.execute("""
                           SELECT worker_id, name_id, job_title, report_count, date_of_work
                           FROM employees ORDER BY name_id
                           """)

        employees = cursor.fetchall()
        conn.close()
        return employees

    def add_employee(self, name, job_title, date_of_work, branch_id=None):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO employees (name_id, job_title, report_count, date_of_work, branch_id)
                       VALUES (?, ?, ?, ?, ?)
                       """, (name, job_title, 0, date_of_work, branch_id))

        employee_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return employee_id

    def update_employee(self, worker_id, name, job_title, date_of_work):
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
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE worker_id = ?", (employee_id,))
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success

    # ========== МЕТОДЫ ДЛЯ ПОЛЬЗОВАТЕЛЕЙ ==========

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

    def change_password(self, username, new_password):
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

    # ========== МЕТОДЫ ДЛЯ КОМПАНИИ ==========

    def get_company_name(self):
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
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM company")
            cursor.execute("INSERT INTO company (name) VALUES (?)", (name,))
            conn.commit()
        except Exception as e:
            print(f"Ошибка сохранения названия: {e}")
        finally:
            conn.close()

    def add_report(self, report_data):
        """Добавление нового отчета"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
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
            return report_id
        except Exception as e:
            print(f"Ошибка добавления отчета: {e}")
            return None
        finally:
            conn.close()

    def get_all_reports(self):
        """Получение всех отчетов"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                       SELECT report_id, report_name, report_date, description, order_number
                       FROM reports
                       ORDER BY report_date DESC
                       """)
            reports = cursor.fetchall()
            return reports
        except Exception as e:
            print(f"Ошибка загрузки отчетов: {e}")
            return []
        finally:
            conn.close()

    def get_report(self, report_id):
        """Получение отчета по ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                       SELECT report_id, report_name, report_date, description, order_number,
                              worker_id, environment_id
                       FROM reports
                       WHERE report_id = ?
                       """, (report_id,))
            report = cursor.fetchone()
            return report
        except Exception as e:
            print(f"Ошибка загрузки отчета: {e}")
            return None
        finally:
            conn.close()

if __name__ == "__main__":
    db = DatabaseHandler()
    print("\n✅ DatabaseHandler готов к работе!")

    # Проверка создания таблиц
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("\n📊 Таблицы в БД:")
    for table in tables:
        print(f"  - {table[0]}")

    # Проверка структуры комнат
    cursor.execute("PRAGMA table_info(room)")
    columns = cursor.fetchall()
    print("\n🏢 Структура таблицы room:")
    for col in columns:
        print(f"  - {col[1]}: {col[2]}")

    conn.close()