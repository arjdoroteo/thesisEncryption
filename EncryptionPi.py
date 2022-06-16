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

# Establishing the connection between the database and the program
cluster = MongoClient(
    'mongodb+srv://test1:123@cluster0.hfj9h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['Flame']
collection = db['arjdoroteo']


# Encrypts user's name and location, writes to file, and returns cipher

def aes_userdata():
    # For final testing, random keys and initialization vector would be generated and used.
    # key = get_random_bytes(32)
    # iv = get_random_bytes(16)

    # for testing purposes, predefined keys and initialization vector are used.
    key = b'1234567890qwertyuiopasdfghjklzxc'
    iv = b'1q2w3e4r5t6y7u8i'

    # User input of Name and Location
    # plainName = input('Enter Name: ').encode('ascii')
    # plaintLocation = input('Enter Location: ').encode('ascii')

    # predefined Name and Location
    plainName = b'Adrian Robert Doroteo'
    plainLocation = b'14.466762,120.974886'
    plainData = plainName + b',' + plainLocation

    cipher = AES.new(key, AES.MODE_CBC, iv)

    cipherText = cipher.encrypt(pad(plainData, AES.block_size))

    # Writes the key, iv, and encrypted text to a local file
    with open('cipher_file', 'wb') as c_file:
        c_file.write(key)
        c_file.write(iv)
        c_file.write(cipherText)

    # returns the encrypted text
    return (cipherText)


# Function to upload data to mongodb
def mongodbUpload(temp, co, gas, date_time, cipherText):
    post = {'User Info': cipherText, 'Date and Time': date_time,
            'Temperature': temp, 'CO': co, 'LPG': gas}
    collection.insert_one(post)
    print('Uploaded')


x = True

temp_limit = 125
co_limit = 100
gas_limit = 10000

# timer set to 5 seconds, will be replaced to 1 hour in final system
timer = 5

cipherText = aes_userdata()
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()

while x == True:

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        sensorData = line.split(",")

        temp = sensorData[0]
        co = sensorData[1]
        gas = sensorData[2]

        print('Temp: ' + str(temp) + ' CO: ' + str(co) + ' LPG: ' + str(gas))

        if temp >= temp_limit or co >= co_limit or gas >= gas_limit:
            mongodbUpload(temp, co, gas, date_time, cipherText)
            if timer == 0:
                print('Timer Done!')
                timer = 5

        elif timer == 0:
            mongodbUpload(temp, co, gas, date_time, cipherText)
            print('Timer Done!')
            timer = 5

    timer -= 1
    time.sleep(1)
    print(timer)
