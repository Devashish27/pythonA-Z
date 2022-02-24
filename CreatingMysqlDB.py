import sqlite3
# improt os
# os.system('clear')

# Connecting to DB...
conn = sqlite3.connect('customer.db')

# Cursor for creating ..
c = conn.cursor()

# Using docstrings and creating table....!
'''
c.execute(""" CREATE TABLE customer (
			first_name text,
			last_name text,
			email text
			) """)
'''

# c.execute("INSERT INTO customer VALUES ('Vishn', 'Shiv', 'Vishn.Shiva27@gmail.com')")

c.execute("SELECT * FROM customer")

# print(c.fetchall()[0][0])

# Using loops..!
items = c.fetchall()

for item in items:
	
	print(item[0] + " " + item[1])

print("Data Added To Table..!")

# Commit our changes...
conn.commit()

# Close DB Connection..!
conn.close()
