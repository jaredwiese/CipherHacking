# Transposition Cipher Decryption
# http://inventwithpython.com/hacking (BSD Licensed)
# * forked by Jared Wiese

import math, pyperclip

def main():
    # cipherText = 'Sytduoe  utcciac eus tasr p, sinr p.toobr' # test message
    # key = 7 # test key for test cipherText
    cipherText = raw_input('Enter Ciphertext: ')
    while True:
        key = raw_input('Enter Key: ')
        if key.isdigit():
            key = int(key)
            break

    plainText = decryptMessage(key, cipherText)

    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plainText + '|')

    pyperclip.copy(plainText)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns"
    # and "rows" of the grid that the plaintext is written on by using
    # a list of strings. First, we need to calculate a few values.
    
    # The number of "columns" in our transposition grid:
    # *Note* In Pytyon 2.x: Dividing two ints produces
    # another int which is rounded before the ceiling call. 
    # Making one value a float will yield the correct result.
    numOfcolumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfcolumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plainText = [''] * numOfcolumns

    # The column and row variables point to where in the grid
    # the next character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plainText[column] += symbol
        column += 1 # point to next column

        # If there are no more columns OR we're at a shaded box,
        # go back to the first column and the next row.
        if (column == numOfcolumns) or (column == numOfcolumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plainText)
    
    
# If transpositionDecrypt.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()

exit()
