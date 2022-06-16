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
    sensorData = []

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        sensorData = line.split(",")
        print(sensorData)
        time.sleep(1)
