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

possibilities = []


for index,letter in enumerate(starting):
    if letter == target[index]:
        found[index] = letter
        foundIndices.append(index)
    elif letter in target:
        container.append(letter)
    else:
        deadLetters.append(letter)


def gameState():
    possibilities = []
    for word in wordList:
        for num in foundIndices:
            if found[num] == target[num]:
                for letter in container:
                    if letter in target:
                        for letter in deadLetters:
                            if letter in target:
                                break
                            else:
                                possibilities[len(possibilities)] = word

gameState()

for word in possibilities:
    print(word)
            










