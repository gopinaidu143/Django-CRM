import mysql.connector 

# Connect to MySQL database
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Gopi#143'
)

# Create a cursor object using the correct spelling
cursorObject = dataBase.cursor()

# Execute SQL command to create a new database
cursorObject.execute('CREATE DATABASE crmapp')

print("All Done!!")
