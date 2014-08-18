# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
# forked by Jared Wiese

# cipherText = 'The enemy knows the system.' # practice cipherText
cipherText = raw_input('cipherText: ')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):
    
    # It is important to set translated to the blank string so that
    # the previous iteration's value for translated is cleared.
    translated = ''
    
    # The rest of the program is the same as the original Caesar program:
    # run the encryption/decryption code on each symbol in the cipherText.
    for symbol in cipherText:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key
            
            if num < 0:
                num = num + len(LETTERS)
                
            # add number's symbol at the end of translated
            translated += LETTERS[num]
            
        else:
            # just add the symbol without encrypting/decrypting
            translated += symbol
            
    # display the current key being tested along with its decryption
    print 'Key ' + str(key) + ': ' + translated
    
exit()
