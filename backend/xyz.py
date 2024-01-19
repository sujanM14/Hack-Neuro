import sqlite3
import pandas as pd
data = pd.read_excel('C:/Users/Tushar/Desktop/chatbot-using-react-nodejs-chatgpt/backend/Mindspark_Sample data for Spend Chatbot.xlsx')
# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect("chatbot.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_table (
        Region TEXT,
        Month INTEGER,
        Year INTEGER,
        Plant_Name TEXT,
        Plant_Country TEXT,
        Vendor_Code INTEGER,
        Vendor_Name TEXT,
        Vendor_Country TEXT,
        Commodity TEXT,
        Buyer TEXT,
        Part_Code TEXT,
        Payment_Days INTEGER,
        Country_of_Origin TEXT,
        Quantity INTEGER,
        Unit_of_Measure TEXT,
        Price_per_unit REAL,
        PO_Currency TEXT,
        Exchange_Rate_in_USD REAL,
        Spend_USD REAL
    )
''')

# Convert the DataFrame to a list of tuples and insert data into the table
data_list = [tuple(row) for row in data.values]

insert_query = f'INSERT INTO data_table VALUES ({", ".join(["?"] * len(data.columns))})'

cursor.executemany(insert_query, data_list)

# Commit the changes and close the connection
conn.commit()
conn.close()


conn = sqlite3.connect("chatbot.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Retrieve and print the first 10 rows
query = "SELECT * FROM data_table LIMIT 10"
cursor.execute(query)

# Fetch and display the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Retrieve and print the description of the database
query = "PRAGMA table_info(data_table)"
cursor.execute(query)

# Fetch and display the table description
table_info = cursor.fetchall()
for info in table_info:
    print(info)

conn.close()