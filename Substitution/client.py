#Client.py
import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 4500
def encrypt(c, val):
    if c.islower():
        return chr((ord(c) - 97 + val) % 26 + 97)
    return chr((ord(c) - 65 + val) % 26 + 65)
str = input('Give the string for encryption\n')
val = int(input('Give the key for encryption\n'))
str1 = ''
for c in str:
    str1 += encrypt(c, val)
skt.connect((host, port))
print('Connection establised with server listening on port 4500\n')
print(f'encrypted string --> {str1}')
skt.send(str1.encode('utf-8'))
str1 = skt.recv(2048).decode('utf-8')
skt.close()
print(f'decrypted string recieved --> {str1}')
if str == str1:
    print('Server decrypted correclty')
else:
    print('Wrong decryption')
