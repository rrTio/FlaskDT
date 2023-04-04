import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711
import sqlite3
import datetime

delay = 2 #delay in seconds

# Force Python 3 ###########################################################

if sys.version_info[0] != 3:
    raise Exception("Python 3 is required.")

############################################################################


hx = HX711(5, 6)

def database(val1, val2, val3, cur_time, cur_date): 
    global conn, cursor
    conn = sqlite3.connect("DateTime.db")
    print ("Created Database")

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `dt` (grade1 VARCHAR(255), grade2 VARCHAR(255), grade3 VARCHAR(255), reg_date TEXT, reg_time TEXT)") #create database table

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `dt` VALUES(?,?,?,?,?)",(val1,val2,val3,cur_date,cur_time)) #inserting data into the database table
        conn.commit()
        print("Insert successful")

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()


def setup():
    """
    code run once
    """
    hx.set_offset(`Place offset here`)
    hx.set_scale(`Place ratio here`)


def loop():
    """
    code run continuosly
    """
    current = datetime.datetime.now() #instantiation of date and time

    cur_date = current.strftime("%m-%d-%Y") #current date formatting
    cur_time = current.strftime("%I:%M:%S %p") #current time formatting

    try:
        val = hx.get_grams()
        print(val)

        hx.power_down()
        time.sleep(.001)
        hx.power_up()

        database(val, val, val, cur_time, cur_date)
        time.sleep(delay)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


##################################

if __name__ == "__main__":

    setup()
    while True:
        loop()