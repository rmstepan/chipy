with open("crypto/porta_table", 'r') as pt:
    rows = pt.readlines()


def expand_to_length(string_to_expand,length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]


def get_value(row,ordinal):
    data = rows[row].replace("\n", "").split(" ")
    return data[ordinal]


def encrypt(text, key):
    # apply lowercase to both key and the text to be encrypted
    text = text.lower()
    key = key.lower()

    # expand key length to match the text's length
    cipherkey = expand_to_length(key, len(text))
    encrypted = ""
    for letter in range(0, len(text)):
        # get alphabet position of letters from the text to be encrypted
        alphabet_position = ord(text[letter]) - 97

        # calculate alphabet position of letters from key
        asc = ord(cipherkey[letter]) - 97
        # get row index of the group the letter is found in
        rownr = int(asc / 2)

        encrypted += (get_value(rownr, alphabet_position))

    return encrypted

