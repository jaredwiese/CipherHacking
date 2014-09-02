# Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese

import pyperclip, sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # message = """Few persons can be made to believe that it is not quite an easy thing to invent a method of secret writing which shall baffle investigation. Yet it may be roundly asserted that human ingenuity cannot concoct a cipher which human ingenuity cannot resolve...It may be observed, generally, that in such investigations the analytic ability is very forcibly called into action; and for this reason, cryptographical solutions might with great propriety be introduced into academies as the means of giving tone to the most important of the powers of the mind. -Edgar Allan Poe"""
    
    # the encryption/decryption key must contain all letters
    # key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ' # Test Key
        
    message = raw_input('Enter Text: ')
    
    while True:
        key = raw_input("Type 'R' to use Random Key or Enter Your Own Key: ")
        if key.lower() == 'r':
            key = getRandomKey()
            checkValidKey(key)
            break
        else:
            checkValidKey(key)
            break
    
    
    # Tells the program whether to encrypt or decrypt the message
    # mode = 'encrypt' # Test: Set to 'encrypt' or 'decrypt'
    while True:
        mode = raw_input('Encrypt or Decrypt? ').lower()
        if mode.strip() == 'encrypt' or mode.strip() == 'decrypt':
            break
    

    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)
    print 'Using key %s' % (key)
    print 'The %sed message is:' % (mode)
    print translated
    pyperclip.copy(translated)
    print ''
    print 'This message has been copied to the clipboard.'


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
