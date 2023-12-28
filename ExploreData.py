import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("IWE_data.db")

# Write your SQL query to fetch data from the database
sql_query = "SELECT * FROM ho_thuy_dien"

# Use pandas to read the SQL query result into a DataFrame
df = pd.read_sql_query(sql_query, conn)

# Close the database connection
conn.close()

# Print the DataFrame
print(df.describe())
