### Wordle Solver
### Python Project

import random

myDict = open("wdict.txt","r")

wordList = [word for word in myDict]

targetIndex = random.randint(0,len(wordList)-1)
target = wordList[targetIndex]

starting = "trail"

found = "....."
foundIndices = []

container = []

deadLetters = []


for index,letter in enumerate(starting):
    if letter == target[index]:
        found[index] = letter
        foundIndices[len(foundIndices)] = index
    elif letter in target:
        container[len(container)] = letter
    else:
        deadLetters[len(deadLetters)] = letter

for word in wordList:
    for num in foundIndices:
        if found[num] == target[num]:
            for letter in deadLetters:
                for 







