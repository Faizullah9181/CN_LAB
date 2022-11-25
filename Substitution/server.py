#Program 5 :Substitution
#Server.py
import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 4500
def func(c, val):
    if c.islower():
        return chr((ord(c) - 97 - val + 26) % 26 + 97)
    return chr((ord(c) - 65 - val + 26) % 26 + 65)
skt.bind((host, port))
print('Socket in listening for incoming requests...')
skt.listen()
cl, addr = skt.accept()
print(f'Established connection with {cl}\n')
str = cl.recv(2048).decode('utf-8')
print('Recieved the encrypted string\nProvide the key for decryption')
val = int(input())
str1 = ''
for c in str:
    str1 += func(c, val)
cl.send(str1.encode('utf-8'))
skt.close()
