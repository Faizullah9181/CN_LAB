#Program : 10: PlayFair Cipher
def generateKeyTable(key):
    key = key.upper()
    key = key.replace("J", "I")
    keytable = []
    for c in key:
        if c not in keytable:
            keytable.append(c)
    alphabets = [chr(i) for i in range(65, 91)]
    alphabets.remove("J")
    for c in alphabets:
        if c not in keytable:
            keytable.append(c)
    keytable = [keytable[i:i+5] for i in range(0, 25, 5)]
    return keytable
def getDimension(c):
    c = c.upper()
    if c == "J":
        c = "I"
    for i in range(5):
        for j in range(5):
            if keytable[i][j] == c:
                return i, j
def encrypt(plaintext):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace("J", "I")
    i = 0
    while i < len(plaintext)-1:
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + "X" + plaintext[i+1:]
        i += 2
    if len(plaintext) % 2 != 0:
        plaintext += "X"
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        c1 = plaintext[i]
        c2 = plaintext[i+1]
        r1, c1 = getDimension(c1)
        r2, c2 = getDimension(c2)
        if r1 == r2:
            ciphertext += keytable[r1][(c1+1) % 5] + keytable[r2][(c2+1) % 5]
        elif c1 == c2:
            ciphertext += keytable[(r1+1) % 5][c1] + keytable[(r2+1) % 5][c2]
        else:
            ciphertext += keytable[r1][c2] + keytable[r2][c1]
    return ciphertext
def decrypt(ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        c1 = ciphertext[i]
        c2 = ciphertext[i+1]
        r1, c1 = getDimension(c1)
        r2, c2 = getDimension(c2)
        if r1 == r2:
            plaintext += keytable[r1][(c1-1) % 5] + keytable[r2][(c2-1) % 5]
        elif c1 == c2:
            plaintext += keytable[(r1-1) % 5][c1] + keytable[(r2-1) % 5][c2]
        else:
            plaintext += keytable[r1][c2] + keytable[r2][c1]
    plaintext = plaintext.replace("X", "")
    return plaintext
def main():
    global keytable
    key = input("Enter the key: ")
    keytable = generateKeyTable(key)
    plaintext = input("Enter the plaintext: ")
    ciphertext = encrypt(plaintext)
    print("The ciphertext is: ", ciphertext)
    print("The plaintext is: ", decrypt(ciphertext))
if __name__ == '__main__':
    main()
