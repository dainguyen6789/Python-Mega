# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3
print ("Hello Spider Dai Nguyen")
print(7)

conn=sqlite3.connect("lite.db")
cur=conn.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
conn.commit()
conn.close()
print("1st Commit of Dai")
print("2nd Commit of Dai")

