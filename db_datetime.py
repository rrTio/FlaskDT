import sqlite3
import datetime

def database(cur_time, cur_date):
    global conn, cursor
    conn = sqlite3.connect("DateTime.db")
    print ("Created Database")

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `dt` (reg_date TEXT, reg_time TEXT)")

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `dt` VALUES(?,?)",(cur_date, cur_time))
        conn.commit()
        print("Insert successful")

now = datetime.datetime.now()

cur_time = now.strftime("%H:%M:%S")
cur_date = now.strftime("%b-%d-%Y")

database(cur_time, cur_date)
