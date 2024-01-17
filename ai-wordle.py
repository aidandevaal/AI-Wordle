### Wordle Solver
### Python Project

import random

myDict = open("wdict.txt","r")

wordList = [word for word in myDict]

targetIndex = random.randint(0,len(wordList)-1)
target = wordList[targetIndex]

starting = "trail"

found = "....."
container = []
containerIndex = 0

deadLetters = []
deadLettersIndex = 0


for index,letter in enumerate(starting):
    if letter == target[index]:
        found[index] = letter
    elif letter in target:
        container[containerIndex] = letter
        containerIndex+=1
    else:
        deadLetters[deadLettersIndex] = letter
        deadLettersIndex+=1









