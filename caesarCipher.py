# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# * forked by Jared Wiese

import pyperclip

# the string to be encrypted/decrypted
# message = "Cry 'Havoc', and let slip the dogs of war;" # test message
# message = message.upper() # uncomment this line also for test
message = raw_input('Enter Text ').upper()

# the encryption/decryption key
while True:
    key = raw_input('Enter key: ')
    if key.isdigit():
        key = int(key)
        break

# tells the program to encrypt or decrypt
while True:
    mode = raw_input('Encrypt or Decrypt? ').lower()
    if mode.strip() == 'encrypt' or mode.strip() == 'decrypt':
        break

# every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted/decrypted number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
            
        # handle the wrap-around if num is larger than the length of 
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num -len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        
        # add encrypted/decrypted numbers's symbol at the end of translated
        translated += LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated += symbol
        
# print the encrypted/decrypted string to the screen
print translated

# copy the encrypted/decrypted string to the clipboard
pyperclip.copy(translated)
