import sqlite3
import datetime
import time

delay = 1

def database(cur_time, cur_date):
    global conn, cursor
    conn = sqlite3.connect("DateTime.db")
    print ("Created Database")

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `dt` (grade1 VARCHAR(255), grade2 VARCHAR(255), grade3 VARCHAR(255), reg_date TEXT, reg_time TEXT)")

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `dt` VALUES(?,?,?,?,?)",("TEST1","TEST2","TEST3",cur_date,cur_time))
        conn.commit()
        print("Insert successful")

while True:

    current = datetime.datetime.now()

    cur_date = current.strftime("%m-%d-%Y")
    cur_time = current.strftime("%H:%M:%S")

    print("DATE AND TIME")
    print("DATE: ", cur_date)
    print("TIME: ", cur_time)
    print(" ")
    
    database(cur_time, cur_date)
    time.sleep(delay) 
