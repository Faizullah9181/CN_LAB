#Program:3 - Baconian Cipher
map = {
    'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
    'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
    'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
    'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
    'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'
}

def encrypt(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):
            cipher += map[letter]
        else:
            cipher += ' '

    return cipher
def  decrypt(message):
    decipher = ''
    i = 0
    while True:
        if(i < len(message) - 4):
            substr = message[i:i + 5]

            if(substr == ' '):
                decipher += ' '
                i += 1
            else:
                decipher += list(map.keys())[list(map.values()).index(substr)]
                i += 5
        else:
            break

    return decipher

def main():
    s = input("Enter the message to be encrypted: ")
    result = encrypt(s.upper())
    print(result)

    s = input("Enter the message to be decrypted: ")
    result = decrypt(s.lower())
    print(result)

if __name__ == '__main__':
    main()