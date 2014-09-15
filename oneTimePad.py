# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese into a One Time Pad Cipher

import pyperclip, os, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    # message = """'Deciphering is, in my opinion, one of the most fascinating of arts, and I fear I have wasted upon it more time than it deserves. I practised it in its simplest form when I was at school. The bigger boys made ciphers, but if I got hold of a few words, I usually found out the key. The consequence of this ingenuity was occasionally painful: the owners of the detected ciphers sometimes thrashed me, though the fault really lay in their own stupidity. There is a kind of maxim amongst the craft of decipherers ..., that every cipher can be deciphered. I am myself inclined to think that deciphering is an affair of time, ingenuity, and patience; and that very few ciphers are worth the trouble of unravelling them.' -Charles Babbage"""
    
    # mode = 'decrypt' # test: set to 'encrypt' or 'decrypt'

    message = raw_input('Enter Text: ')
        
    while True:
        mode = raw_input('Encrypt or Decrypt? ').lower()
        if mode.strip() == 'encrypt' or mode.strip() == 'decrypt':
            break
    
    count = 0            
    for char in message.upper():
        if char in LETTERS:
            count += 1

    if mode == 'encrypt':
        print 'Type 'R' to use a Random Key or Enter Your Own Encryption Key.'
        print "(If using your own key it must be equal to the length of the message to be a 'One Time Pad.'",
        print 'Otherwise it is just a Vigenere Cipher...)'
        print 'Your message length is %r.' % count
        while True:
            key = raw_input('> ').upper()
            if len(key) == count:
                break
            elif key.lower() == 'r':
                key = randomChar(count)
                print key
                print ''
                print 'Your Key will be saved to a text file in this Folder.'
                keyFile = raw_input('Enter File Name for Key: ')
                try: 
                    file = open(keyFile, 'a')
                    file.write('%s' % (key))
                    file.close()
                except:
                    print 'Sorry. Writing Key to Text File failed.'
                break
            else:
                print "I'm sorry. That's not quite right."
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        key = raw_input('Enter your Decryption Key: ').upper()
        translated = decryptMessage(key, message)

    print '%sed Message:' % mode.title()
    print translated
    pyperclip.copy(translated)
    print ''
    print 'The message has been copied to the clipboard.'


def randomChar(j):
       return ''.join(random.choice(LETTERS) for x in range(j))


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)
    
    return ''.join(translated)


if __name__ == '__main__':
    main()
