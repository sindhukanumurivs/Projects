import sqlite3

# Connect to the database
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Query to fetch all data from user_info table
c.execute('SELECT * FROM user_info')
rows = c.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()