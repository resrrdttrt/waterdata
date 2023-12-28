import requests
import sqlite3
from datetime import datetime
import re

# Function to create a SQLite database and table
def create_database():
    conn = sqlite3.connect('IWE_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ho_thuy_loi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            maho TEXT,
            ten TEXT,
            diadiem TEXT,
            lat TEXT,
            lon TEXT,
            datetime DATETIME,
            thoigian TEXT,
            mucnuocho REAL,
            dungtich REAL,
            qden REAL,
            luuluongtrantudo REAL,
            qxa REAL,
            luuluongthuydien REAL,
            luuluongdongchaytoithieu REAL,
            luuluonghadu REAL,
            mucnuochodukien12gio REAL,
            dukienluuluonghadu REAL,
            dukienluuluongden REAL,
            luongmuataidap REAL
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
            INSERT INTO ho_thuy_loi (
                maho, ten, diadiem, lat, lon, datetime, thoigian, mucnuocho, dungtich, qden,
                luuluongtrantudo, qxa, luuluongthuydien, luuluongdongchaytoithieu, luuluonghadu,
                mucnuochodukien12gio, dukienluuluonghadu, dukienluuluongden, luongmuataidap
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            entry['maho'], entry['ten'], entry['diadiem'], entry['lat'], entry['lon'],
            entry['datetime'], entry['thoigian'], entry['mucnuocho'], entry['dungtich'],
            entry['qden'], entry['luuluongtrantudo'], entry['qxa'], entry['luuluongthuydien'],
            entry['luuluongdongchaytoithieu'], entry['luuluonghadu'], entry['mucnuochodukien12gio'],
            entry['dukienluuluonghadu'], entry['dukienluuluongden'], entry['luongmuataidap']
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
api_url = 'http://qndnapi.vndss.com/service/getDataHoThuyLoi'
data = get_data_from_api(api_url)

if data:
    create_database()
    insert_data(data)
    print("Data successfully retrieved and stored in the SQLite database.")
else:
    print("Failed to retrieve data from the API.")
