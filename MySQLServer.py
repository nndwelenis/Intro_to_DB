import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mulatshawe",
            port=3306
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        connection.commit()

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
