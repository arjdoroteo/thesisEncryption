from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


with open('speed_test_file', 'rb') as c_file:
    key = c_file.read(32)
    iv = c_file.read(16)
    cipherText = c_file.read()

cipher = AES.new(key, AES.MODE_CBC, iv)


plainText = unpad(cipher.decrypt(cipherText), AES.block_size)

print(plainText.decode('ascii'))
