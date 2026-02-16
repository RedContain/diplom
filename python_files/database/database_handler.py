import os
import sqlite3

class DatabaseHandler:
    def __init__(self, db_path="database/company.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self.create_tables()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def create_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        # 1️⃣ Сначала создаем таблицы, на которые будут ссылаться другие
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS branches (
                                                               branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                               name TEXT NOT NULL,
                                                               floors_count INTEGER NOT NULL,
                                                               address TEXT NOT NULL
                       )
                       ''')

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS room (
                                                           room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           room_number TEXT NOT NULL,
                                                           room_name TEXT NOT NULL
                       )
                       ''')

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS employees (
                                                                worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                name_id TEXT NOT NULL,
                                                                job_title TEXT NOT NULL,
                                                                report_count INTEGER NOT NULL,
                                                                date_of_work TEXT NOT NULL
                       )
                       ''')

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS environment (
                                                                  environment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                  environment_name TEXT NOT NULL,
                                                                  branch_id INTEGER NOT NULL
                       )
                       ''')

        # 2️⃣ Потом таблицы с внешними ключами
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS equipment (
                                                                equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                quantity INTEGER NOT NULL,
                                                                category TEXT NOT NULL,
                                                                type TEXT NOT NULL,
                                                                name TEXT NOT NULL,
                                                                date_incoming INTEGER NOT NULL,
                                                                state_incoming INTEGER NOT NULL,
                                                                serial_number TEXT NOT NULL,
                                                                supplier TEXT NOT NULL,
                                                                price INTEGER NOT NULL,
                                                                phone_supplier TEXT NOT NULL,
                                                                email_supplier TEXT NOT NULL,
                                                                room_id INTEGER,
                                                                branch_id INTEGER,
                                                                status TEXT DEFAULT 'in_use',
                                                                last_inventory_date TEXT,
                                                                notes TEXT,
                                                                FOREIGN KEY (room_id) REFERENCES room(room_id)
                           )
                       ''')

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
                                                              FOREIGN KEY (worker_id) REFERENCES employees(worker_id),
                           FOREIGN KEY (environment_id) REFERENCES environment(environment_id),
                           FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
                           )
                       ''')

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
                                                                    FOREIGN KEY (report_id) REFERENCES reports(report_id),
                           FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
                           FOREIGN KEY (worker_id) REFERENCES employees(worker_id)
                           )
                       ''')

        conn.commit()
        conn.close()
        print("✅ База данных создана/обновлена!")

if __name__ == "__main__":
    db = DatabaseHandler()
    print("База данных успешно создана и готова к работе!")