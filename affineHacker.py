# Affine Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese

import pyperclip, affineCipher, detectEnglish, cryptoMath

# Prints out each tested encryption if False
# True obviously speeds up the program...
SILENT_MODE = False

def main():
    # You can copy & paste an alternate test text from the
    # source code at http://invpy.com/affineHacker.py
    # message = """gb+K?K3V?K3iI_3istKT3_`3KJ!?sti@_Jz3_JK3i+Vi3I@  3t?K4KJi3s_~?3T@TiK?3`?_53?KV6@Ju3s_~?36@V?s3VJ63_JK3i+Vi3I@  3t?K4KJi3s_~?3u_4K?J5KJi<g3'd?~!K3M!+JK@K?"""
    
    message = raw_input('Enter Text: ')
    
    hackedMessage = hackAffine(message)

    if hackedMessage != None:
        # The plaintext is displayed on the screen. For the convenience
        # of the user, we copy the text of the code to the clipboard.
        print 'Copying hacked message to clipboard:'
        print hackedMessage
        pyperclip.copy(hackedMessage)
    else:
        print 'Failed to hack encryption.'


def hackAffine(message):
    print 'Hacking...'

    # Python programs can be stopped at any time by pressing 
    # Ctrl-C (on Windows) or Ctrl-D (on Mac and Linux)
    print '(Press Ctrl-C or Ctrl-D to quit at any time.)'

    # brute-force by looping through every possible key
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print 'Tried Key %s: ... (%s)' % (key, decryptedText[:40])

        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print ''
            print 'Possible encryption hack:'
            print 'Key: %s' % (key)
            print 'Decrypted message: ' + decryptedText[:200]
            print ''
            print 'Enter D for done, or just press Enter to continue hacking:'
            response = raw_input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# If affineHacker.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
