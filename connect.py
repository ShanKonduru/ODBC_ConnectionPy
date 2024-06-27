import pyodbc

# Define the User DSN
dsn = 'PostgreSQL15'  # Replace with your User DSN name

# Create a connection string using only the DSN
conn_str = f'DSN={dsn}'

# Connect to the database
try:
    connection = pyodbc.connect(conn_str)
    print("Connection successful!")
    
    # Create a cursor object using the connection
    cursor = connection.cursor()

    userTablesQry = """SELECT table_schema, table_name  FROM information_schema.tables  WHERE table_type = 'BASE TABLE'"""
    # Sample query to test the connection
    cursor.execute(userTablesQry)  # Replace with your table name
    rows = cursor.fetchall()
    # Print the results
    for row in rows:
        print(row)
    
    print('--------------------------------------')
    
    # Update with the correct table name and schema
    table_name = "Src_Emp_Table"  # Replace with the correct table name
    schema_name = "public"  # Replace with the correct schema name

    cursor.execute(f'SELECT * FROM "{schema_name}"."{table_name}"')
    rows = cursor.fetchall()
    # Print the results
    for row in rows:
        print(row)

    print('--------------------------------------')

except pyodbc.Error as e:
    print("Error connecting to the database:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
