import sqlite3
import datetime
import time

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
    current_time = time.strftime("%H:%M:%S")
    current_date = datetime.date.today()

    cur_date = ("{}-{}-{}".format(current_date.month, current_date.day, current_date.year))
    print(current_time)
    time.sleep(1) 
    database(current_time, cur_date)
