import os
import sqlite3

class DatabaseHandler:
    def __init__(self, db_path="database/company.db"):
        # Создаем папку, если её нет
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        print(f"🔄 Создание/подключение к БД: {db_path}")
        self.create_tables()

    def get_connection(self):
        """Получение соединения с БД"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def create_tables(self):
        """Создание всех таблиц"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 1️⃣ Таблица филиалов
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS branches (
                                                               branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                               name TEXT NOT NULL,
                                                               floors_count INTEGER NOT NULL,
                                                               address TEXT NOT NULL
                       )
                       ''')

        # 2️⃣ Таблица сотрудников (связь с филиалом)
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

        # 3️⃣ Таблица окружения
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS environment (
                                                                  environment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                  environment_name TEXT NOT NULL,
                                                                  branch_id INTEGER NOT NULL,
                                                                  FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE
                           )
                       ''')

        # ========== 👇 ГЛАВНОЕ: ОБНОВЛЕННАЯ ТАБЛИЦА room ==========
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS room (
                                                           room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           room_number TEXT NOT NULL,
                                                           room_name TEXT NOT NULL,
                                                           branch_id INTEGER,
                                                           floor INTEGER DEFAULT 1,
                                                           capacity INTEGER DEFAULT 0,           -- Сколько человек может сидеть
                                                           desks_count INTEGER DEFAULT 0,        -- Количество столов
                                                           chairs_count INTEGER DEFAULT 0,       -- Количество стульев
                                                           sockets_count INTEGER DEFAULT 0,      -- Количество розеток
                                                           area REAL DEFAULT 0.0,                -- Площадь в м²
                                                           responsible_employee_id INTEGER,      -- ID ответственного сотрудника
                                                           notes TEXT DEFAULT '',                -- Дополнительные заметки
                                                           FOREIGN KEY (branch_id) REFERENCES branches(branch_id) ON DELETE CASCADE,
                           FOREIGN KEY (responsible_employee_id) REFERENCES employees(worker_id) ON DELETE SET NULL
                           )
                       ''')

        # 4️⃣ Таблица оборудования (связь с комнатой)
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

        # 5️⃣ Таблица отчетов
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

        # 6️⃣ Таблица лога инвентаризации
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

        # 7️⃣ Таблица пользователей
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users (
                                                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            username TEXT UNIQUE NOT NULL,
                                                            password TEXT NOT NULL,
                                                            role TEXT DEFAULT 'user'
                       )
                       ''')

        # 8️⃣ Таблица компании (для названия предприятия)
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS company (
                                                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                              name TEXT NOT NULL
                       )
                       ''')

        # Добавляем тестовые данные, если таблицы пустые
        self.add_test_data(cursor)

        conn.commit()
        conn.close()
        print("✅ База данных успешно создана/обновлена!")

    def add_test_data(self, cursor):
        """Добавление тестовых данных"""
        # Проверяем и добавляем филиалы
        cursor.execute("SELECT COUNT(*) FROM branches")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO branches (name, floors_count, address) VALUES (?, ?, ?)",
                ("Главный корпус", 5, "ул. Ленина, 1")
            )
            cursor.execute(
                "INSERT INTO branches (name, floors_count, address) VALUES (?, ?, ?)",
                ("Поликлиника №1", 3, "ул. Мира, 10")
            )
            print("  ✅ Добавлены тестовые филиалы")

        # Проверяем и добавляем сотрудников
        cursor.execute("SELECT COUNT(*) FROM employees")
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                           INSERT INTO employees (name_id, job_title, report_count, date_of_work, branch_id)
                           VALUES (?, ?, ?, ?, ?)
                           """, ("Иванов Иван Иванович", "Заведующий отделением", 0, "2020-01-15", 1))

            cursor.execute("""
                           INSERT INTO employees (name_id, job_title, report_count, date_of_work, branch_id)
                           VALUES (?, ?, ?, ?, ?)
                           """, ("Петров Петр Петрович", "Старший лаборант", 0, "2021-03-20", 1))

            cursor.execute("""
                           INSERT INTO employees (name_id, job_title, report_count, date_of_work, branch_id)
                           VALUES (?, ?, ?, ?, ?)
                           """, ("Сидорова Анна Сергеевна", "Медсестра", 0, "2022-05-10", 2))
            print("  ✅ Добавлены тестовые сотрудники")

        # Проверяем и добавляем комнаты
        cursor.execute("SELECT COUNT(*) FROM room")
        if cursor.fetchone()[0] == 0:
            # Комнаты для главного корпуса
            cursor.execute("""
                           INSERT INTO room (
                               room_number, room_name, branch_id, floor, capacity,
                               desks_count, chairs_count, sockets_count, area,
                               responsible_employee_id, notes
                           ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                           """, ("101", "Кабинет заведующего", 1, 1, 5, 2, 5, 4, 25.5, 1, "Угловой кабинет"))

            cursor.execute("""
                           INSERT INTO room (
                               room_number, room_name, branch_id, floor, capacity,
                               desks_count, chairs_count, sockets_count, area, notes
                           ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                           """, ("102", "Процедурная", 1, 1, 8, 1, 8, 6, 30.0, "Требуется ремонт"))

            cursor.execute("""
                           INSERT INTO room (
                               room_number, room_name, branch_id, floor, capacity,
                               desks_count, chairs_count, sockets_count, area
                           ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                           """, ("201", "Палата №1", 1, 2, 4, 4, 4, 2, 20.0))

            # Комнаты для поликлиники
            cursor.execute("""
                           INSERT INTO room (
                               room_number, room_name, branch_id, floor, capacity,
                               desks_count, chairs_count, sockets_count, area
                           ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                           """, ("1", "Кабинет терапевта", 2, 1, 6, 2, 6, 4, 22.0))

            print("  ✅ Добавлены тестовые комнаты")

        # Добавляем пользователя admin
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                ('admin', 'admin', 'admin')
            )
            print("  ✅ Добавлен пользователь admin")

        # Добавляем компанию
        cursor.execute("SELECT COUNT(*) FROM company")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO company (name) VALUES (?)",
                ("ГБОУ Больница 2 г. Апшеронск",)
            )
            print("  ✅ Добавлено название предприятия")

    # ========== МЕТОДЫ ДЛЯ КОМНАТ (ОБНОВЛЕННЫЕ) ==========

    def get_rooms(self, branch_id=None):
        """Получение комнат с полной информацией"""
        conn = self.get_connection()
        cursor = conn.cursor()

        if branch_id:
            cursor.execute("""
                           SELECT
                               r.room_id, r.room_number, r.room_name, r.floor,
                               r.capacity, r.desks_count, r.chairs_count,
                               r.sockets_count, r.area, r.responsible_employee_id,
                               r.notes, e.name_id as responsible_name
                           FROM room r
                                    LEFT JOIN employees e ON r.responsible_employee_id = e.worker_id
                           WHERE r.branch_id = ?
                           ORDER BY r.floor, r.room_number
                           """, (branch_id,))
        else:
            cursor.execute("""
                           SELECT
                               r.room_id, r.room_number, r.room_name, r.floor,
                               r.capacity, r.desks_count, r.chairs_count,
                               r.sockets_count, r.area, r.responsible_employee_id,
                               r.notes, e.name_id as responsible_name
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
        """Добавление комнаты со всеми параметрами"""
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
                                       room_number = ?, room_name = ?, floor = ?,
                                       capacity = ?, desks_count = ?, chairs_count = ?,
                                       sockets_count = ?, area = ?, responsible_employee_id = ?,
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

        # Сначала обновляем оборудование (снимаем привязку к комнате)
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
                           r.room_id, r.room_number, r.room_name, r.floor,
                           r.capacity, r.desks_count, r.chairs_count,
                           r.sockets_count, r.area, r.responsible_employee_id,
                           r.notes, e.name_id as responsible_name, r.branch_id
                       FROM room r
                                LEFT JOIN employees e ON r.responsible_employee_id = e.worker_id
                       WHERE r.room_id = ?
                       """, (room_id,))

        room = cursor.fetchone()
        conn.close()
        return room


if __name__ == "__main__":
    db = DatabaseHandler()
    print("\n🔍 Проверка создания БД:")

    # Проверяем, создались ли таблицы
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("\nСозданные таблицы:")
    for table in tables:
        # Проверяем структуру таблицы room
        if table[0] == 'room':
            cursor.execute("PRAGMA table_info(room)")
            columns = cursor.fetchall()
            print(f"  📋 Таблица '{table[0]}' имеет колонки:")
            for col in columns:
                print(f"     - {col[1]}: {col[2]}")
        else:
            print(f"  - {table[0]}")

    # Показываем тестовые данные
    print("\n📊 Тестовые данные:")

    rooms = db.get_rooms(1)
    print(f"  Комнат в филиале 1: {len(rooms)}")
    if rooms:
        print("  Первая комната:")
        room = rooms[0]
        print(f"    Номер: {room[1]}, Название: {room[2]}, Этаж: {room[3]}")
        print(f"    Вместимость: {room[4]} чел, Столов: {room[5]}, Стульев: {room[6]}")
        print(f"    Розеток: {room[7]}, Площадь: {room[8]} м²")
        print(f"    Ответственный: {room[11] if len(room) > 11 else 'Не назначен'}")

    conn.close()
    print("\n✅ Готово! Файл company.db создан и заполнен тестовыми данными.")