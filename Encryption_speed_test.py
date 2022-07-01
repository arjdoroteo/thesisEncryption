from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time


def encrypt_data(plainName, plainLocation):
    key = b'1234567890qwertyuiopasdfghjklzxc'
    iv = b'1q2w3e4r5t6y7u8i'

    plainName = plainName.encode('UTF-8')
    plainLocation = plainLocation.encode('UTF-8')
    plainData = plainName + b',' + plainLocation

    plainDataSize = plainData.decode('ascii')
    print(plainDataSize)
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

    encrypt_data(userNameSet[i], userLocSet[i])
