# RSA Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese

import sys, os

# IMPORTANT: The block size MUST be less than or equal to the key size!
# (Note: The block size is in bytes, the key size is in bits.
# There are 8 bits in 1 byte.)
DEFAULT_BLOCK_SIZE = 128 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

def main():
    # Runs a test that encrypts a message to a file or decrypts a message from a file.
    # filename = 'newtest.txt' # test: the file to write to/read from
    # mode = 'decrypt' # test: set to 'encrypt' or 'decrypt'

    filename = raw_input('Input File Name: ')

    while True:
        mode = raw_input('Encrypt or Decrypt? ').lower()
        if mode.strip() == 'encrypt' or mode.strip() == 'decrypt':
            break
    
    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(filename):
        print 'The file %s does not exist. Quitting...' % (filename)
        sys.exit()


    if mode == 'encrypt':
        # message = """RSA is one of the first practicable public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and differs from the decryption key which is kept secret. In RSA, this asymmetry is based on the practical difficulty of factoring the product of two large prime numbers, the factoring problem. RSA stands for Ron Rivest, Adi Shamir and Leonard Adleman, who first publicly described the algorithm in 1977. Clifford Cocks, an English mathematician, had developed an equivalent system in 1973, but it wasn't declassified until 1997. A user of RSA creates and then publishes a public key based on the two large prime numbers, along with an auxiliary value. The prime numbers must be kept secret. Anyone can use the public key to encrypt a message, but with currently published methods, if the public key is large enough, only someone with knowledge of the prime factors can feasibly decode the message. Breaking RSA encryption is known as the RSA problem. It is an open question whether it is as hard as the factoring problem."""
        
        message = raw_input('Enter Text: ')
        
        pubKeyFilename = 'jared_wiese_pubkey.txt'
        print 'Encrypting and writing to %s...' % (filename)
        encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)

        print 'Encrypted text: '
        print encryptedText 

    elif mode == 'decrypt':
        privKeyFilename = 'jared_wiese_privkey.txt'
        print 'Reading from %s and decrypting...' % (filename)
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)

        print 'Decrypted text: '
        print decryptedText


def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a string message to a list of block integers. Each integer
    # represents 128 (or whatever blockSize is set to) string characters.

    messageBytes = message.encode('ascii') # convert the string to bytes

    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        # Calculate the block integer for this block of text
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += ord(messageBytes[i]) * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a list of block integers to the original message string.
    # The original message length is needed to properly convert the last
    # block integer.
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer.
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts the message string into a list of block integers, and then
    # encrypts each block integer. Pass the PUBLIC key to encrypt.
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        # ciphertext = plaintext ^ e mod n
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
    # Decrypts a list of encrypted block ints into the original message
    # string. The original message length is required to properly decrypt
    # the last block. Be sure to pass the PRIVATE key to decrypt.
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
        # plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
    # Given the filename of a file that contains a public or private key,
    # return the key as a (n,e) or (n,d) tuple value.
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
    # Using a key from a key file, encrypt the message and save it to a
    # file. Returns the encrypted message string.
    keySize, n, e = readKeyFile(keyFilename)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Either decrease the block size or use different keys.' % (blockSize * 8, keySize))


    # Encrypt the message
    encryptedBlocks = encryptMessage(message, (n, e), blockSize)

    # Convert the large int values to one string value.
    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    # Write out the encrypted string to the output file.
    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    fo = open(messageFilename, 'w')
    fo.write(encryptedContent)
    fo.close()
    # Also return the encrypted string.
    return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
    # Using a key from a key file, read an encrypted message from a file
    # and then decrypt it. Returns the decrypted message string.
    keySize, n, d = readKeyFile(keyFilename)


    # Read in the message length and the encrypted message from the file.
    fo = open(messageFilename)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

    # Convert the encrypted message into large int values.
    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    # Decrypt the large int values.
    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)


if __name__ == '__main__':
    main()
