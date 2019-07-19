# -*- coding: utf-8 -*-
# File  : mysql.py
# Date  : 2019/5/17

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost:3306",
    user ="root",
    password = "678268"
)
print(mydb)