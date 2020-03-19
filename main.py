from crypto import porta
from crypto import vigenere

# Porta table encryption
print(porta.encrypt("texttobeencrypted", "cipher"))       # fvddegpvykrjklmus
print(porta.decrypt("fvddegpvykrjklmus", "cipher"))
print("\n")

# Vigenere Square encryption
print(vigenere.encrypt("securitatesicriptografie", "UNIVERSITATEADEVESTDINTIMISOARA"))
print(vigenere.decrypt("securitatesicriptografie", "oibpzkmdmuoxuyxpzlnybhobgdlivku"))
print("\n")
