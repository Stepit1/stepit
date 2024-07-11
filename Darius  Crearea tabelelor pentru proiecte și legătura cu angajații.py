import sqlite3

# Funcție pentru crearea și popularea tabelelor
def create_and_populate_database():
    try:
        # Conectarea la baza de date sau crearea uneia noi (company.db)
        conn = sqlite3.connect('company.db')
        cursor = conn.cursor()

        # Crearea tabelului projects
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT
        )
        ''')

        # Popularea tabelului projects
        projects_data = [
            (1, 'Project A', '2023-01-01', '2023-06-30'),
            (2, 'Project B', '2023-02-01', '2023-07-31'),
            (3, 'Project C', '2023-03-01', '2023-08-31'),
            (4, 'Project D', '2023-04-01', '2023-09-30'),
            (5, 'Project E', '2023-05-01', '2023-10-31')
        ]
        cursor.executemany('''
        INSERT INTO projects (project_id, name, start_date, end_date)
        VALUES (?, ?, ?, ?)
        ''', projects_data)

        # Crearea tabelului employee_projects
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee_projects (
            emp_id INTEGER NOT NULL,
            project_id INTEGER NOT NULL,
            FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
            FOREIGN KEY (project_id) REFERENCES projects(project_id),
            PRIMARY KEY (emp_id, project_id)
        )
        ''')

        # Popularea tabelului employee_projects
        employee_projects_data = [
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 3),
            (3, 4),
            (3, 5),
            (4, 2),
            (4, 5),
            (5, 3),
            (5, 4)
        ]
        cursor.executemany('''
        INSERT INTO employee_projects (emp_id, project_id)
        VALUES (?, ?)
        ''', employee_projects_data)

        # Salvarea modificărilor și închiderea conexiunii
        conn.commit()
        conn.close()

        print("Baza de date a fost creată și populată cu succes!")

    except sqlite3.Error as e:
        print(f"Eroare SQLite: {e}")

# Apelarea funcției pentru crearea și popularea bazei de date
create_and_populate_database()