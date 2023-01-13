#!/usr/bin/env python

import sys
import mysql.connector
from mysql.connector import Error

# pip install mysql-connector-python

host = sys.argv[1]
userlist = open(sys.argv[2].read().splitlines())
pw = sys.argv[3]

for user in userlist:
    try:
        connection = mysql.connector.connect(host=host,
                                             database='information_schema',
                                             user='user',
                                             password='pw')
        if connection.is_connected():
            mysql_server_info = connection.get_server_info()
            print("Username exists", mysql_server_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Success - connected to db: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
