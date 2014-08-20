# Transposition Cipher Encrypt/Decrypt File
# http://inventwithpython.com/hacking (BSD Licensed)
# * forked by Jared Wiese

import time, os, sys, transpositionEncrypt, transpositionDecrypt


def main():
    # MUST be a Text File!
    # inputFilename = 'beowulf.txt'
    inputFilename = raw_input('Input File Name: ')
    # BE CAREFUL! If a file with the outputFilename name
    # already exists, this program will overwrite that file.
    #outputFilename = 'beowulf.encrypted.txt'
    outputFilename = raw_input('Output File Name: ')
    
    while True:
        key = raw_input('Enter Key: ')
        if key.isdigit():
            key = int(key)
            break
    
    while True:
        mode = raw_input('Encrypt or Decrypt? ').lower()
        if mode.strip() == 'encrypt' or mode.strip() == 'decrypt':
            break
    
    # If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFilename):
        print 'The file %s does not exist. Quitting...' % (inputFilename)
        sys.exit()
    
    # If the output file already exists, give the user a chance to quit.
    if os.path.exists(outputFilename):
        print 'This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename)
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    
    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    
    print'%sing...' % (mode.title())
    
    # Measure how long the encryption/decryption takes.
    startTime = time.time()
    if mode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(key, content)
    elif mode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(key, content)
    totalTime = round(time.time() - startTime, 2)
    print '%sion time: %s seconds' % (mode.title(), totalTime)
    
    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()
    print 'Done %sing %s (%s characters).' % (mode, inputFilename, len(content))
    print '%sed file is %s.' % (mode.title(), outputFilename)

# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
