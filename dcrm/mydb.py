# Install Mysql on your local computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "Frt_123456",
)

# prepare a cursor object using cursor() method

cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE dcrm")
print("Database created successfully")
