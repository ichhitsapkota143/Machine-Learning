import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
cursor = conn.cursor()

# CREATE TABLE
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    )
''')

# CREATE - Insert a user
def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()

# READ - Get all users
def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# UPDATE - Update user email
def update_user_email(user_id, new_email):
    cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))
    conn.commit()

# DELETE - Delete a user
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()

# Example Usage
create_user("Ram", "ram@example.com")
create_user("Sita", "sita@example.com")

print("Users:", read_users())

update_user_email(4, "sita@newdomain.com")
delete_user(4)

print("Updated Users:", read_users())

# Close connection
cursor.close()
conn.close()
