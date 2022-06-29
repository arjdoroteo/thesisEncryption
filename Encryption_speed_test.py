from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time


def encrypt_data():
    key = b'1234567890qwertyuiopasdfghjklzxc'
    iv = b'1q2w3e4r5t6y7u8i'

    plainName = b'Adrian Robert Doroteo'
    plainLocation = b'14.466762,120.974886'
    plainData = plainName + b',' + plainLocation

    plainDataSize = plainData.decode('ascii')
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


encrypt_data()
