# Caesar Cipher Encryption

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = "Let's Encrypt XYZ!"
ciphertext = ''

for letter in plaintext.upper():
    if letter in alphabet:
        pos = alphabet.index(letter)
        #print(alphabet[(pos + 3) % 26])
        ciphertext += alphabet[(pos + 3) % 26]
    else:
        ciphertext += letter
print("Plaintext:", plaintext, "\n", "Ciphertext: ", ciphertext)