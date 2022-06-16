import serial
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time
import pymongo
from pymongo import MongoClient
import datetime
from datetime import datetime
import random

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()
x = True
while x == True:

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    line = ser.readline().decode('utf-8').rstrip()
    sensorData = line.split(",")

    temp = sensorData[0]
    co = sensorData[1]
    gas = sensorData[2]

    print(co)
