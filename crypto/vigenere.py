# create vigenere square
def create_square():
    square = []
    for i in range(0, 26):
        row = []
        for j in range(0, 26):
            if 97 + j + i > 122:
                row.append(str(chr(97 + j + i - 26)))
            else:
                row.append(str(chr(97 + j + i)))
        square.append(row)
    return square


# extend keyword to the length of the plaintext
def extend_keyword(keyword, plaintext):
    return (keyword * (int(len(plaintext) / len(keyword)) + 1))[:len(plaintext)]


# vigenere encryption
def encrypt(keyword, plaintext):
    keyword = keyword.lower()
    plaintext = plaintext.lower()
    keyword = extend_keyword(keyword, plaintext)

    cipher = ""
    # parse the plaintext and build the ciphertext
    for i in range(0, len(plaintext)):
        column = ord(plaintext[i]) - 97    # get ASCII code of the letter and calculate the alphabet position of the
        # column letter
        row = ord(keyword[i])-97           # same
        cipher += square[column][row]      # append to the cipher the letter found at corresponding column and row

    return cipher


# vigenere decryption
def decrypt(keyword, ciphertext):
    keyword = keyword.lower()
    ciphertext = ciphertext.lower()
    keyword = extend_keyword(keyword, ciphertext)

    plaintext = ""
    # parse the ciphertext and build the plaintext
    for i in range(0, len(ciphertext)):
        row = ord(keyword[i]) - 97         # get alphabet position of the row letter
        column = square[row].index(ciphertext[i])  # find column letter from the square using the row and the letter
        plaintext += str(chr(column+97))

    return plaintext

square = create_square()


