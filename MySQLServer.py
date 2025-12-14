#!/usr/bin/env python3
"""
MySQLServer.py

Creates the database `alx_book_store` on a MySQL server.

Requirements satisfied:
- Uses CREATE DATABASE IF NOT EXISTS (script will not fail if DB already exists)
- Does not use SELECT or SHOW statements
- Prints: Database 'alx_book_store' created successfully! on success
- Prints an error message if connection or creation fails
- Properly opens and closes the database connection
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    # Connection settings:
    # Replace these values with your MySQL credentials.
    # If you are using MySQL Workbench "Local instance MySQL80", the host is usually localhost and port 3306.
    config = {
        "host": "localhost",
        "user": "root",
        "password": "Mulatshawe",
        "port": 3306,
    }

    connection = None
    cursor = None

    try:
        # 1) Connect to MySQL server (do not specify a database yet)
        connection = mysql.connector.connect(**config)

        # 2) Create a cursor for executing SQL statements
        cursor = connection.cursor()

        # 3) Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")

        # 4) Commit changes (some configurations require commit for DDL to persist cleanly)
        connection.commit()

        # 5) Required success message
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


    finally:
        # Always close cursor and connection to avoid resource leaks
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass

        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except Exception:
                pass


if __name__ == "__main__":
    create_database()
