# Program 9:Vigenere Cipher
# Server.py
import socket
import threading
import json
PORT = 4000
HEADER = 1024
FORMAT = "utf-8"
MAX_CLIENT = 2
DISCONNECT_MESSAGE = "!DISCONNECTED!"
FIRST_CONNECTION = "!FIRST_CONNECTION!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
# creates a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
USERS_LIST = {}
USERS_LIST2 = {}
# vigener cipher decryption


def decryptVigenere(cipher_text, key):
    msg = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26 + ord(' ')

        msg.append(chr(x))
    return ("" . join(msg))


def decodeMessage(str, client_address):
    client_object = json.loads(str)
    global USERS_LIST
    global USERS_LIST2
    print(str)
    if client_object["msg"] == FIRST_CONNECTION:
        # for first connection stores the name of the user corresponding to the client address
        USERS_LIST[client_address] = client_object["name"]
        return f"joined the server."
    else:
        USERS_LIST2[client_address] = client_object["msg"]
        msg = decryptVigenere(
            client_object["msg"], USERS_LIST2[client_address])
        return msg


def handleClient(client_connection, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.\n")
    global USERS_LIST2
    global USERS_LIST
    connected = True
    while connected:
        str = client_connection.recv(HEADER).decode(FORMAT)
        if len(str) == 0:
            continue
        msg = decodeMessage(str, client_address)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            print(f"{USERS_LIST[client_address]} is offline now.")
            continue
        print(f"{msg}")
    client_connection.close()


def start():
    server.listen(MAX_CLIENT)
    print(f"[LISTENING]  server is listening on {SERVER}\n")
    connected = True
    while connected:
        client_connection, client_address = server.accept()
        thread = threading.Thread(target=handleClient, args=(
            client_connection, client_address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}\n")


print("[STARTING] server is starting...\n")
start()
