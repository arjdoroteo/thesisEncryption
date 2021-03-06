# install the following libraries
# pip install pycryptodome
# pip install pymongo
# pip install "pymongo[srv]"

# import the needed libraries
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time
import pymongo
from pymongo import MongoClient
import datetime
from datetime import datetime
import random
import pathlib
from Crypto.Hash import SHA512
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
    enclist = []
    # User input of Name and Location
    # plainName = input('Enter Name: ').encode('ascii')
    # plaintLocation = input('Enter Location: ').encode('ascii')

    # predefined Name and Location
    plainName = b'Adrian Robert Doroteo'
    plainLocation = b'14.466762,120.974886'
    plainData = plainName + b',' + plainLocation

    cipher = AES.new(key, AES.MODE_CBC, iv)

    cipherText = cipher.encrypt(pad(plainData, AES.block_size))
    hash = createHash(plainData)
    enclist.append(cipherText)
    enclist.append(hash)
    # Writes the key, iv, and encrypted text to a local file
    with open('cipher_file', 'wb') as c_file:
        c_file.write(key)
        c_file.write(iv)
        c_file.write(cipherText)
    with open('hash_file', 'w') as c_file:
        c_file.write(hash)
    # returns the encrypted text
    return (enclist)


# Function to upload data to mongodb
def mongodbUpload(temp, co, gas, date_time, cipherText, hash):
    post = {'User Info': cipherText, 'Hash': hash, 'Date and Time': date_time,
            'Temperature': temp, 'CO': co, 'LPG': gas}
    collection.insert_one(post)
    print('Uploaded')


def saveLocal(date_time, temp, co, gas):
    now = datetime.now()
    pathsss = pathlib.Path().resolve()
    local_Date = str(pathsss) + "/" + now.strftime("%m-%d-%Y") + ".csv"

    f = open(local_Date, "a")
    f.write("{}, {}, {}, {}\n".format(date_time, temp, co, gas))


def createHash(plainText):
    h = SHA512.new(truncate="256")
    h.update(plainText)
    return h.hexdigest()


x = True

temp_limit = 125
co_limit = 100
gas_limit = 5000

# timer set to 5 seconds, will be replaced to 1 hour in final system
timer = 5

encList = aes_userdata()
cipherText = encList[0]
hash = encList[1]

while x == True:
    # random data will be replaced by data from sensors
    temp = random.randint(15, 125)
    co = random.randint(0, 100)
    gas = random.randint(0, 10000)

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    # saveLocal(date_time, temp, co, gas)

    if temp >= temp_limit or co >= co_limit or gas >= gas_limit:
        # mongodbUpload(temp, co, gas, date_time, cipherText, hash)
        print("Uploaded")
        if timer == 0:
            print('Timer Done!')
            timer = 5

    elif timer == 0:
        # mongodbUpload(temp, co, gas, date_time, cipherText, hash)
        print('Timer Done!')
        timer = 5

    timer -= 1
    time.sleep(1)
    print(timer)
    print('Temp: ' + str(temp) + ' CO: ' + str(co) + ' LPG: ' + str(gas))
