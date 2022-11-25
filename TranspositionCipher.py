#Program : 2 - Transposition Cipher
import math

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)

def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

def main():
    myMessage = input("Enter the message to be encrypted: ")
    myKey = int(input("Enter the key: "))
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext)

    myMessage = input("Enter the message to be decrypted: ")
    myKey = int(input("Enter the key: "))
    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext)

if __name__ == '__main__':
    main()
