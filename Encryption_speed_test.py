from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time
from Crypto.Hash import SHA512
from Crypto.Cipher import DES3
from Crypto.Cipher import CAST


def encrypt_dataCast(plainName, plainLocation):
    key = b'1234567890qwerty'

    plainName = plainName.encode('UTF-8')
    plainLocation = plainLocation.encode('UTF-8')
    plainData = plainName + b',' + plainLocation

    plainDataSize = plainData.decode('ascii')

    print("User Data: ", plainDataSize)

    print("SHA512 Hash: ", createHash(plainData))

    print('Data size: ', len(plainDataSize.encode('utf-16-le')), 'bytes')

    st = time.process_time()

    cipher = CAST.new(key, CAST.MODE_CBC)
    msg = cipher.encrypt(pad(plainData, CAST.block_size))

    et = time.process_time()
    res = et - st
    print('CPU Execution time: ', res * 1000, 'milliseconds')


def encrypt_dataDes(plainName, plainLocation):
    while True:
        try:
            key = DES3.adjust_key_parity(b'1234567890qwertyuiopasdf')
            break
        except ValueError:
            pass

    plainName = plainName.encode('UTF-8')
    plainLocation = plainLocation.encode('UTF-8')
    plainData = plainName + b',' + plainLocation

    plainDataSize = plainData.decode('ascii')

    print("User Data: ", plainDataSize)

    print("SHA512 Hash: ", createHash(plainData))

    print('Data size: ', len(plainDataSize.encode('utf-16-le')), 'bytes')

    st = time.process_time()
    cipher = DES3.new(key, DES3.MODE_CBC)
    msg = cipher.iv + cipher.encrypt(pad(plainData, DES3.block_size))
    et = time.process_time()
    res = et - st
    print('CPU Execution time: ', res * 1000, 'milliseconds')


def encrypt_data(plainName, plainLocation):
    key = b'1234567890qwertyuiopasdfghjklzxc'
    iv = b'1q2w3e4r5t6y7u8i'

    plainName = plainName.encode('UTF-8')
    plainLocation = plainLocation.encode('UTF-8')
    plainData = plainName + b',' + plainLocation

    plainDataSize = plainData.decode('ascii')
    print("User Data: ", plainDataSize)

    print("SHA512 Hash: ", createHash(plainData))

    print('Data size: ', len(plainDataSize.encode('utf-16-le')), 'bytes')

    st = time.process_time()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipherText = cipher.encrypt(pad(plainData, AES.block_size))

    et = time.process_time()
    res = et - st
    print('CPU Execution time: ', res * 1000, 'milliseconds')

    # Writes the key, iv, and encrypted text to a local file
    with open('speed_test_file', 'wb') as c_file:
        c_file.write(key)
        c_file.write(iv)
        c_file.write(cipherText)


def createHash(plainText):
    h = SHA512.new(truncate="256")
    h.update(plainText)
    return h.hexdigest()


userNameSet = ['Adrian Robert Doroteo', 'Ericson Dimaunahan',
               'Darwin James Goling', 'Emman Paloma', 'Rave Puerto', 'Michael Ogue', 'Neil Isip']
userLocSet = ['14.466762,120.974886',
              '14.598563, 121.004054',
              '14.573361, 121.000544',
              '14.587021, 121.001485',
              '14.588568, 121.004253',
              '14.590987, 121.010368',
              '14.586865, 121.012600']


for i in range(len(userNameSet)):
    print("Encrypting Using AES256")
    encrypt_data(userNameSet[i], userLocSet[i])
    print("\n")


for i in range(len(userNameSet)):

    print("Encrypting Using Triple DES")
    encrypt_dataDes(userNameSet[i], userLocSet[i])
    print("\n")

for i in range(len(userNameSet)):

    print("Encrypting Using CAST-128")
    encrypt_dataCast(userNameSet[i], userLocSet[i])
    print("\n")
