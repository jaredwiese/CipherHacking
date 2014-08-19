# This is a guess the number game.
# http://inventwithpython.com (BSD Licensed)
# * forked by Jared Wiese

import random

guessesTaken = 0

print '***** Guess The Number *****'
print ''
print 'Hello! What is your name?'
user = raw_input('> ' )
print ''

number = random.randint(1, 100)

print 'Well, ' + user + ', do you want to guess what number I am thinking of?'
game = raw_input('> ').lower()
if game == 'yes' or game == 'y':
    print ''
    print 'Great! I am thinking of a number between 1 and 100.' 
    print 'You have 6 guesses to figure out my number.'
    print 'I will tell you if you are too high or too low.'
    
    while guessesTaken < 6:
        print 'Take a guess.'
        guess = input()
        guess = int(guess)
        guessesTaken += 1
        if guess < number:
            print 'Your guess is too low.'
        elif guess > number:
            print 'Your guess is too high.'
        else:
            break
		
    if guess == number:
        guessesTaken = str(guessesTaken)
        print '****** Good job, ' + user + '! You guessed my number in ' + guessesTaken + ' guesses! ******'
        print ''
    else:
        number = str(number)
        print 'XXXXXX Nope. The number I was thinking of was ' + number + ' XXXXXX'
        print ''
elif game == 'no' or game == 'n':
    print 'Goodbye.'
    print ''
else:
    print "I'm sorry, I don't understand that."
    print ''

exit()
