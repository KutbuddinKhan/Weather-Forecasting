import sqlite3

def create_table():
    connection = sqlite3.connect('weather_app.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   city_name TEXT NOT NULL,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()