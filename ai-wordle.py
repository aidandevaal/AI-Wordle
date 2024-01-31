### Wordle Solver
### Python Project

import random

myDict = open("wdict.txt","r")

wordList = [word for word in myDict]

targetIndex = random.randint(0,len(wordList)-1)
#target = wordList[targetIndex]

target = "trade"
starting = "trial"

found = []
foundIndices = []

container = []

deadLetters = []

possibilities = []


#for index,letter in enumerate(starting):
#    if(letter == target[index]):
#        found.insert(index, letter)
#        foundIndices.append(index)
#        container.append(letter)
#    elif(letter in target):
#        container.append(letter)
#    else:
#        deadLetters.append(letter)

def start():
    choice = input("Enter a string for the AI to crack: ")
    end(choice)
    gameState(choice)
    AI()

def end(guess):
    if(guess == target):
        print("ez")
        quit()



def xor(a, b):
    return ((a and not b) or (not a and b))



def gameState(guess):

    for index,letter in enumerate(guess):
        if(letter == target[index]):
            found.insert(index, letter)
            foundIndices.append(index)
            container.append(letter)
        elif(letter in target):
            container.append(letter)
        else:
            deadLetters.append(letter)

    if(guess in possibilities):
        possibilities.remove(guess)
    wordCheck()



def wordCheck():
    for word in wordList:
        count = 0
        for num in foundIndices:
            if((len(found) > 0) and (word[foundIndices[num]] == target[foundIndices[num]])):
                count+=1
        if(count == len(foundIndices)):
            possibilities.append(word)

    toRemove = []

    for word in possibilities:
        count = 0
        for letter in container:
            if(letter not in word):
                toRemove.append(word)

    for word in toRemove:
        possibilities.remove(word)



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

    index = 0


    print(likelihoods.keys())
    print(likelihoods.values())





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
            










