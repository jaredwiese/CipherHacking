# Detect English module
# http://inventwithpython.com/hacking (BSD Licensed)
# * Forked by Jared Wiese

# To use, type this code:
# import detectEnglish
# detectEnglish.isEnglish(someString) # returns True or False
# There must be a "words.txt" file in this directory with all English
# words in it, one word per line. You can download this from
# http://invpy.com/words.txt

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadWords():
    wordsFile = open('words.txt')
    englishWords = {}
    for word in wordsFile.read().split('\n'):
        englishWords[word] = None
    wordsFile.close()
    return englishWords

ENGLISH_WORDS = loadWords()


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0 # no words at all, so return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the words file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
