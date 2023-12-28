import requests
import sqlite3
from datetime import datetime
import re

# Function to create a SQLite database and table
def create_database():
    conn = sqlite3.connect('IWE_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS muc_nuoc_thuy_van (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mahieu TEXT,
            ten TEXT,
            kinhdo REAL,
            vido REAL,
            datetime DATETIME,
            mucnuoc REAL,
            thoigian TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to insert data into the SQLite database
def insert_data(data):
    conn = sqlite3.connect('IWE_data.db')
    cursor = conn.cursor()

    for entry in data:
        timestamp_match = re.search(r'/Date\((\d+)\)/', entry['datetime'])
        if timestamp_match:
            timestamp = int(timestamp_match.group(1))
            entry['datetime'] = datetime.utcfromtimestamp(timestamp / 1000.0).replace(tzinfo=None)

        cursor.execute('''
            INSERT INTO muc_nuoc_thuy_van (
                mahieu, ten, kinhdo, vido, datetime, mucnuoc, thoigian
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            entry['mahieu'], entry['ten'], entry['kinhdo'], entry['vido'],
            entry['datetime'], entry['mucnuoc'], entry['thoigian']
        ))

    conn.commit()
    conn.close()

# Function to fetch data from the API
def get_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main execution
api_url = 'http://qndnapi.vndss.com/service/getDataMucNuocThuyVan'
data = get_data_from_api(api_url)

if data:
    create_database()
    insert_data(data)
    print("Data successfully retrieved and stored in the SQLite database.")
else:
    print("Failed to retrieve data from the API.")
