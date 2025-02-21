import csv
import sqlite3

conn = sqlite3.connect("friday.db")
cursor = conn.cursor()

#for system applications

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'virtualbox', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Oracle VM VirtualBo\\x\\Oracle VM VirtualBox.lnk')"
#cursor.execute(query)
#conn.commit()


#for web serches

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'flipkart', 'https://www.flipkart.com/')"
#cursor.execute(query)
#conn.commit()


#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
#desired_columns_indices = [0, 31]

# Read data from CSV and insert into SQLite table for the desired columns
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#    csvreader = csv.reader(csvfile)
#    for row in csvreader:
#        selected_data = [row[i] for i in desired_columns_indices]
#        cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
#conn.commit()
#conn.close()




#delete command if need to delete any path and url
#query = "DELETE FROM sys_command WHERE id="
#### 4. Insert Single contacts (Optional)

'''
bash
query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890')"
cursor.execute(query)
conn.commit()


#### 5. Search Contacts from database

bash
query = 'kunal'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = cursor.fetchall()
print(results[0][0])
'''