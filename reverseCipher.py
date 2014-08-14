# The reverse cipher encrypts a message by printing it in reverse order.

plainText = 'Three can keep a secret, if two of them are dead.'
cipherText = ''

i = len(plainText) - 1
while i >= 0:
    cipherText += plainText[i]
    i -= 1
	
print cipherText
