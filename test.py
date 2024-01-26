import mysql.connector

# Replace these with your actual database credentials
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123123',
    'database': 'password_generation'
}

# Establish a connection to the database
connection = mysql.connector.connect(**db_config)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Example: Execute a simple query to fetch data from the 'user' table
query = "SELECT * FROM user"
cursor.execute(query)

# Fetch and print the results
result = cursor.fetchall()
for row in result:
    print(row)

# Don't forget to close the cursor and connection when you're done
cursor.close()
connection.close()