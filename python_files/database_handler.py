import sqlite3
import os


class DatabaseHandler:
    def __init__(self, db_path="database/company.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self.create_tables()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                job_title TEXT NOT NULL
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS branches (
                branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipment (
                equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL
            )
        ''')


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                report_id INTEGER PRIMARY KEY AUTOINCREMENT,
                report_name TEXT NOT NULL,
                worker_id INTEGER REFERENCES employees(worker_id),
                branch_id INTEGER REFERENCES branches(branch_id),
                equipment_id INTEGER REFERENCES equipment(equipment_id)
            )
        ''')

        conn.commit()
        conn.close()
        print("✅ База данных создана!")


# ДЛЯ ПРОВЕРКИ
if __name__ == "__main__":
    db = DatabaseHandler()
    print("База данных успешно создана и готова к работе!")