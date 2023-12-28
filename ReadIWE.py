import sqlite3
from tabulate import tabulate

# Connect to the SQLite database (replace 'IWE_data.db' with your actual database file)
conn = sqlite3.connect('IWE_data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

while True:
    # Input query from the user
    user_input = input("Enter a SQL query (or 'exit' to quit): ")

    # Check exit condition
    if user_input.lower() == 'exit':
        break

    try:
        # Execute the query
        cursor.execute(user_input)

        # Fetch the results
        results = cursor.fetchall()

        # Check if there are results to display
        if results:
            # Get column names
            columns = [desc[0] for desc in cursor.description]

            # Display results using tabulate
            print(tabulate(results, headers=columns, tablefmt='grid'))
        else:
            print("No results.")

    except sqlite3.Error as e:
        print("SQLite Error:", e)

# Close the cursor and connection
cursor.close()
conn.close()


# db name: ho_thuy_dien, ho_thuy_loi, luong_mua, muc_nuoc_thuy_van