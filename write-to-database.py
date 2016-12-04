#!/usr/bin/python

import MySQLdb
import cgi, cgitb
import os
import time
import datetime
import glob
import MySQLdb
from time import strftime
import urllib
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
gpio.init()

gpio.setup(port.PD14, gpio.IN)
state = gpio.input(port.PD14)


gpio.setcfg(port.PD14, gpio.OUTPUT)

gpio.output(port.PD14, gpio.HIGH)

if (state is True):
    shmer = 1
else:
    shmer = 0 



db = MySQLdb.connect(host="10.115.201.107",user="alice", db="mydb2")
curs=db.cursor()
timeWrite = time.strftime("%H:%M:%S")

try:
    curs.execute ("""INSERT INTO `LED` (`Time`, `POWER`) VALUES(%s,%s);""", (timeWrite, shmer))

    db.commit()
    print "Data committed"

except Exception as err:
    print "Error: the database is being rolled back"
    print err
    db.rollback()
