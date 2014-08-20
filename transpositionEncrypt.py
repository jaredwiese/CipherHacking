# Transposition Cipher Encryption
# http://inventwithpython.com/hacking (BSD Licensed)
# * forked by Jared Wiese

import pyperclip

def main():
    # plainText = 'Security is not a product, but a process.' # test message
    plainText = raw_input('Enter Message: ')
    
    # key should NOT be more than twice the message length
    while True:
        key = raw_input('Enter key: ')
        if key.isdigit():
            key = int(key)
            break

    cipherText = encryptMessage(key, plainText)

    # Print the encrypted string in ciphertext to the screen, with
    # with a | (called "pipe" character) after it in case there are
    # spaces at the end of the encrypted message.
    print cipherText + '|'

    # Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(cipherText)


def encryptMessage(key, message):
    # Each string in cipherText represents a column in the grid.
    cipherText = [''] * key

    # Loop through each column in cipherText.
    for column in range(key):
        pointer = column

        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end
            # of the current column in the ciphertext list.
            cipherText[column] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(cipherText)


# If transpositionEncrypt.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
