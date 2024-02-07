### Wordle Solver
### Python Project

import itertools
import random

myDict = open("wdict.txt","r")

wordList = [word for word in myDict]

targetIndex = random.randint(0,len(wordList)-1)
#target = wordList[targetIndex]

target = "steal"
starting = "trial"

found = []
foundIndices = []

container = []

deadLetters = []

possibilities = []


def start():
    choice = input("Enter a string for the AI to crack: ")
    gameState(choice)


def end(guess):
    print(guess)
    if(guess == target):
        print("ez")
        quit()


def xor(a, b):
    return ((a and not b) or (not a and b))


def gameState(guess):

    end(guess)

    if(guess in possibilities):
        possibilities.remove(guess)

    for index,letter in enumerate(guess):
        if(letter == target[index]):
            if(index not in foundIndices):
                found.insert(index, letter)
                foundIndices.append(index)
                container.append(letter)
        elif(letter in target):
            container.append(letter)
        else:
            deadLetters.append(letter)


    wordCheck()


def wordCheck():
    
    for word in wordList:
        count = 0
        for num in foundIndices:
            if((len(foundIndices) > 0) and (word[num] == target[num])):
                count+=1
        if(count == len(foundIndices)):
            possibilities.append(word)

    toRemove = []

    for word in possibilities:
        count = 0
        for letter in container:
            if(letter not in word):
                toRemove.append(word)
                break
        for letter in deadLetters:
            if(letter in word):
                toRemove.append(word)

    for word in possibilities:
        if word in toRemove:
            possibilities.remove(word)

    AI()


def AI():
    likelihoods = {}
    for word in possibilities:
        for letter in word:
            if(letter not in likelihoods):
                likelihoods[letter] = 1
            else:
                cur = likelihoods.get(letter)
                cur += 1
                likelihoods.update({letter:cur})
    likelihoods.pop("\n")

    likelihoods = dict(sorted(likelihoods.items(), key = lambda item: item[1], reverse = True))

    letters = ["entry"] * len(likelihoods)
    index = 0
    for letter in likelihoods:
        letters[index] = letter
        index += 1

    combos = []
    for letter in range(0, len(letters)):
        combos.extend(itertools.combinations(letters, 5))

    combinations = ["entry"] * len(combos)
    index = 0
    for combo in combos:
        word = ""
        for value in combo:
            word += value
        combinations[index] = word
        index += 1

    potentials = ["aaaaa"] * len(possibilities)
    index = 0
    for combo in combinations:
        word = ""
        for value in combo:
            word += value
        if word in possibilities:
            potentials[index] = word
            index += 1
            
    possibilities.remove(possibilities[0])

    gameState(possibilities[0].strip())

'''
    print(likelihoods.keys())
    print(likelihoods.values())
'''





def main():
    start()
    for word in possibilities:
        print(word)

    print("Container: ")

    for letter in container:
        print(letter)

    print("Found: ")
    for letter in found:
        print(letter)


if __name__ == '__main__':
    main()
            










