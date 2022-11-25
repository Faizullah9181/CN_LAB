# Client.py
import socket
import json
PORT = 4000
HEADER = 1024
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
# Vigenere cipher encryption


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("" . join(key))
# This function returns the
# encrypted text generated
# with the help of the key


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("" . join(cipher_text))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def sendMessage(msg):
    client.send(msg.encode(FORMAT))


user_name = input("Enter your name : ")
json_object = {'name': user_name, 'msg': '!FIRST_CONNECTION!'}
msg = json.dumps(json_object)
sendMessage(msg)
connected = True
while connected:
    msg = input("Enter a message : ")
    keyword = input("Enter a keyword : ")
    strings = msg.lower()
    key = generateKey(strings, keyword)
    if msg == DISCONNECT_MESSAGE:
        connected = False
    msg = cipherText(strings, key)
    json_object = {'name': user_name, 'msg': msg}
    msg = json.dumps(json_object)
    sendMessage(msg)
client.close()
