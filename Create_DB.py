import sqlite3

# Create/Connect to sqlBase
conn = sqlite3.connect('chapters.db')
cursor = conn.cursor()

# Create the chapters table (QR_Code , Json_File)
cursor.execute('''
CREATE TABLE IF NOT EXISTS chapters (
    id INTEGER PRIMARY KEY,
    QR_Code TEXT UNIQUE,
    Json_File TEXT
)
''')


# Save the changes
conn.commit()
conn.close()