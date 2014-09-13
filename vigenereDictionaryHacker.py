# Vigenere Cipher Dictionary Hacker
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese

import detectEnglish, vigenereCipher, pyperclip

def main():
    # cipherText = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    cipherText = raw_input('Enter CipherText: ')
    hackedMessage = hackVigenere(cipherText)

    if hackedMessage != None:
        print 'Copying hacked message to clipboard: '
        print hackedMessage
        pyperclip.copy(hackedMessage)
    else:
        print 'Failed to hack encryption.'


def hackVigenere(cipherText):
    # don't use a 'word' key to avoid this attack
    fo = open('words.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip() # remove the newline at the end
        decryptedText = vigenereCipher.decryptMessage(word, cipherText)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            # Check with user to see if the decrypted key has been found.
            print ''
            print 'Possible encryption break: '
            print 'Key ' + str(word) + ': ' + decryptedText[:100]
            print ''
            print 'Enter D for done, or just press Enter to continue breaking: '
            response = raw_input('> ')

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()
