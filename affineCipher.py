# Affine Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese

import sys, pyperclip, cryptoMath, random
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front


def main():
    # message = """'There are two types of encryption: one that will prevent your sister from reading your diary and one that will prevent your government.' -Bruce Schneier""" # test message
    # key = 2014 # test key
    # mode = 'encrypt' # test: set to 'encrypt' or 'decrypt'

    message = raw_input('Enter Text: ')

    # the encryption/decryption key
    while True:
        key = raw_input("Type 'R' to use Random Key or Enter Your Own Key: ")
        if key.isdigit():
            key = int(key)
            break
        elif key.lower() == 'r':
            key = getRandomKey()
            break
        else:
            print "I'm sorry. I don't understand that."
            
    # tells the program to encrypt or decrypt
    while True:
        mode = raw_input('Encrypt or Decrypt? ').lower()
        if mode.strip() == 'encrypt' or mode.strip() == 'decrypt':
            break

    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)
    print 'Key: %s' % (key)
    print '%sed text:' % (mode.title())
    print translated
    pyperclip.copy(translated)
    print 'Full %sed text copied to clipboard.' % (mode)


def getKeyParts(key):
    # Splits a single integer for Key A and Key B
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if cryptoMath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    cipherText = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cipherText += symbol # just append this symbol unencrypted
    return cipherText


def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plainText = ''
    modInverseOfKeyA = cryptoMath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plainText += symbol # just append this symbol undecrypted
    return plainText


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


# If affineCipher.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
