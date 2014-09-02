# Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese

import pyperclip, sys, random


LETTERS = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note space at the front
# This version encrypts spaces and punctuation and is immune to my simpleSubHacker.py


def main():
    message = r"""Few persons can be made to believe that it is not quite an easy thing to invent a method of secret writing which shall baffle investigation. Yet it may be roundly asserted that human ingenuity cannot concoct a cipher which human ingenuity cannot resolve...It may be observed, generally, that in such investigations the analytic ability is very forcibly called into action; and for this reason, cryptographical solutions might with great propriety be introduced into academies as the means of giving tone to the most important of the powers of the mind. -Edgar Allan Poe"""
    # the encryption/decryption key must contain all letters
    # key = r"""/{9@6hUf:q?_)^eTi|W1,NLD7xk(-SF>Iz0E=d;Bu#c]w~'VvHKmpJ+}s8y& XtP43.b[OA!*\Q<M%$ZgG52YloaRCn"`rj""" # Test Key
    # checkValidKey(key)
    
    # message = raw_input('Enter Text: ')
    
    while True:
        key = raw_input("Type 'R' to use Random Key or Enter Your Own Key: ")
        if key.lower() == 'r':
            key = getRandomKey()
            checkValidKey(key)
            break
        else:
            checkValidKey(key)
            break
    
    
    # tells the program to encrypt or decrypt
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
            symIndex = charsA.find(symbol)
            translated += charsB[symIndex]            
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
