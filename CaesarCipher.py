#Program 1: Caesar Cipher
def encrypt_char(char, key):
    if char.isalpha():
        if char.isupper():
            return chr((ord(char) + key - 65) % 26 + 65)
        else:
            return chr((ord(char) + key - 97) % 26 + 97)
    else:
        return char
    
def encrypt(message, key):
    cipher = ''
    for char in message:
        cipher += encrypt_char(char, key)
    return cipher

def decrypt_char(char, key):
    if char.isalpha():
        if char.isupper():
            return chr((ord(char) - key - 65) % 26 + 65)
        else:
            return chr((ord(char) - key - 97) % 26 + 97)
    else:
        return char
    
def decrypt(message, key):
    decipher = ''
    for char in message:
        decipher += decrypt_char(char, key)
    return decipher

def main():
    s = input("Enter the message to be encrypted: ")
    key = int(input("Enter the key: "))
    result = encrypt(s, key)
    print(result)
    
    s = input("Enter the message to be decrypted: ")
    key = int(input("Enter the key: "))
    result = decrypt(s, key)
    print(result)

if __name__ == '__main__':
    main()
