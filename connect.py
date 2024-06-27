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

    # Query to get the list of all tables in the public schema
    userTablesQry = """
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public' 
        AND table_type = 'BASE TABLE'
    """
    cursor.execute(userTablesQry)
    tables = cursor.fetchall()

    # Iterate over each table and select all data
    for table in tables:
        table_name = table.table_name
        print(f"\nSelecting data from table: {table_name}")

        try:
            select_query = f'SELECT * FROM public."{table_name}"'
            cursor.execute(select_query)
            rows = cursor.fetchall()

            # Print the results for the current table
            for row in rows:
                print(row)
            print("------------------------------")
        except pyodbc.Error as e:
            print(f"Error querying table {table_name}: {e}")

except pyodbc.Error as e:
    print("Error connecting to the database:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
