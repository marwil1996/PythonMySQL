import mysql.connector

mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'feb2121996',
	)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE testdb")

my_cursor.execute("SHOW DATABASES")

my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INT(2), user_id INT AUTO_INCREMENT PRIMARY KEY)")

sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)

my_cursor.execute(sqlStuff, record1)
mydb.commit()

Insert Multiple Records
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [
	("Tim", "tim@tim.com", 32)
	("Mary", "mary@mary.com", 21)
	("Steve", "steve@steve.com", 57)
	("Tina", "tina@tina.com", 29)
]

my_cursor.executemany(sqlStuff, records)
mydb.commit([0])

Pull Data from Table, Format Results

my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("____\t_____\t\t\t___\t___")
or print("----\t-----\t---\t---")
for row in result:
	print(row[0] + "\t%s" %row[1] + "\t%s" %row[2] + "\t%s" %row[3])

Where clause
my_cursor.execute("SELECT * FROM users WHERE age > 30")
result = my_cursor.fetchall()
for row in result:
	print(row)

Where Like and Wildcards
my_cursor.execute("SELECT * FROM users WHERE name LIKE 'J%'")
result = my_cursor.fetchall()
for row in result:
	print(row)

Two wildcards to look for any string containing 'i'
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%'")
result = my_cursor.fetchall()
for row in result:
	print(row)

And Or

AND statement with both needing to be true
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i' AND age LIKE 29")
result = my_cursor.fetchall()
for row in result:
	print(row)

OR statement with only one needing to be true
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i' OR age LIKE 29")
result = my_cursor.fetchall()
for row in result:
	print(row)

Update Records
my_sql = "UPDATE users SET age = 41 WHERE name = 'John'"
my_cursor.execute(my_sql)
mydb.commit()

Use user ID to apply update to correct record
my_sql = "UPDATE users SET age = 40 WHERE user_id = 1"
my_cursor.execute(my_sql)
mydb.commit()

Example of setting name
my_sql = "UPDATE users SET name = 'Tom' WHERE user_id = 5"
my_cursor.execute(my_sql)
mydb.commit()

Limit Results
my_cursor.execute("SELECT * FROM users LIMIT 3")
result = my_cursor.fetchall()
for row in result:
	print(row)

ORDER BY ASC or DESC
my_cursor.execute("SELECT * FROM users ORDER BY name DESC")
my_cursor.execute("SELECT * FROM users ORDER BY name ASC")
result = my_cursor.fetchall()
for row in result:
	print(row)

Delete Records
my_sql = "DELETE FROM users WHERE user_id = 6"
my_cursor.execute(my_sql)
mydb.commit()


Drop Table and Backups
my_sql = "DROP TABLE users"
my_cursor.execute(my_sql)

my_sql = "DROP TABLE IF EXISTS users"
my_cursor.execute(my_sql)
