### Wordle Solver
### Python Project

import itertools

# -- Un-comment import below to use random function
#import random

# -- Read from dictionary file
myDict = open("wdict.txt","r")

# -- Create word list of all potential words
wordList = [word for word in myDict]

#  -- Code for random word generation from list -- testing purposes
#startIndex = random.randint(0,len(wordList)-1)
#startingWord = wordList[startIndex].strip

# -- Statistically best starting word
startingWord = "canoe"

# -- List for letters that are found in the correct position and to track their indices
found = []

# -- Stores indices of those letters to track positional appearances later
foundIndices = []

# -- Container to track letters that are contained within the word selected but are in the wrong position
container = []

# -- Dictionary form of container to track locations where a found letter ISN'T
containerDict = {}

# -- Stores letters that are not in the word
deadLetters = []

# -- Tracks all possible words after factoring from guesses
possibilities = []

# -- List to select all words that no longer apply as possiblities after a guess
toRemove = []

# -- Tracks all guessed words -- For curiosity's sake
guessed = []


# -- Allows user to choose the word for the bot to solve
def start():
    choice = input("Enter a string for the AI to crack: ")

    gameState(startingWord, choice)


# -- Checks end condition and outputs what the bot has selected as a guess (outputs what the user selected in the first instance)
def end(guess, choice):
    print(guess)
    if(guess == choice):
        print("ez")
        cont = input("Type 'Y' to continue: ").lower()
        if(cont == "y"):
            start()
        else:
            quit()

# -- xor function that did not end up being used but could still be handy
#def xor(a, b):
#    return ((a and not b) or (not a and b))


# -- gameState takes a guess and tracks the user's choice as parameters
def gameState(guess, choice):

    guessed.append(guess)

    # -- For looping it checks the endgame condition
    end(guess, choice)

    # -- Removes the guessed word from possible words since the game would have ended from the function above it the word was correct
    if(guess in possibilities):
        possibilities.remove(guess)

    # -- Tracks each letter in guess by letter but also numerical position
    for index,letter in enumerate(guess):
        # -- If the current letter from the guess matches the letter at the chosen word's matching index
        # -- And the index has not already been found (should be inherent but is used for error-checking)
        # -- And the letter is not already in the container (avoid mass duplication of letters in container list)
        if(letter == choice[index]):
            if(index not in foundIndices and letter not in container):
                # -- Add letter at index in list
                found.insert(index, letter)
                # -- Add index to found indices (for overlap error checking mentioned above)
                foundIndices.insert(index, index)
                # -- Add the letter to the container since the word contains the letter (avoid removal later) -> also checks for duplicates
                container.append(letter)
        # -- If the letter is not in the right spot but is in the word -> add it to the container
        elif(letter in choice):
            container.append(letter)
            # -- Add letter to container dictionary to track locations guessed 
            if(letter not in containerDict):
                containerDict[letter] = str(index)
            else:
                cur = containerDict.get(letter)
                cur += str(index)
                containerDict.update({letter:cur})
        # -- Any other case the letter is dead
        else:
            if(letter not in deadLetters):
                deadLetters.append(letter)

    #print(containerDict.keys())
    #print(containerDict.values())
                
    # -- Pass choice to wordCheck
    wordCheck(choice)


# -- wordCheck takes the parameter choice to tack the chosen word for comparison
def wordCheck(choice):
    
    # -- Cycle through each word
    for word in wordList:
        # -- Counter to track matching letter positions in words compared to the chosen word
        count = 0
        # -- For the number of found letters in the right spot
        for num in foundIndices:
            # -- If the word from the list has the same letters in the same positions, of the found letters and indices, as the chosen word 
            if((len(foundIndices) > 0) and (word[num] == choice[num])):
                count+=1
        # -- If all the found indices of letters match -> add that word to the possibilities
        if(count == len(foundIndices)):
            possibilities.append(word)
        else:
            toRemove.append(word)

    # -- Now that we have all the words with the right letters in the right positions
    # -- Loop the letters in those words and check that they're in the container
    for word in possibilities:
        for letter in container:
            # -- If a letter that IS in the word IS NOT in word in possibilities -> add it to the list of words to remove
            if((letter not in word)):
                toRemove.append(word)
                break
        index = 0
        for letter in word:
            if(letter in containerDict):
                indices = containerDict.get(letter)
                for num in indices:
                    if(int(num) == index):
                        toRemove.append(word)
                        break
            index += 1

    
    # -- Loop the words again checking for letters that are dead, in the possibilities. If found -> remove them
    for word in possibilities:
        for letter in deadLetters:
            if(letter in word):
                toRemove.append(word)
                break

    # -- Remove all those discrepancies from the possibilities
    for word in toRemove:
        if(word in possibilities):
            possibilities.remove(word)

    # -- Call the AI passing the user's chosen word
    AI(choice)


# -- AI function takes the parameter choice to once again track the user's chosen word
def AI(choice):
    # -- Dictionary to track letters and the number of their appearances in the possibilities
    likelihoods = {}
    # -- Once again cycle through the words in the possibilities (after they have been narrowed down by "wordCheck")
    for word in possibilities:
        # -- Cycle through the letters in the word
        for letter in word:
            # -- If the letter is not in the dictionary -> add it to the dictionary and track its appearance at 1
            if(letter not in likelihoods):
                likelihoods[letter] = 1
            # -- Otherwise find the letter's number of appearances, add 1, and update it
            else:
                cur = likelihoods.get(letter)
                cur += 1
                likelihoods.update({letter:cur})
    likelihoods.pop("\n")

    # -- Sorts letters by most commonly appearing
    likelihoods = dict(sorted(likelihoods.items(), key = lambda item: item[1], reverse = True))

    # -- Create a list for each of the letters that appear (store a string "entry" to be replaced)
    letters = ["entry"] * len(likelihoods)
    index = 0
    # -- Add each letter to this list
    for letter in likelihoods:
        letters[index] = letter
        index += 1

    # -- Create a list to every combination of the letters from likelihoods
    combos = []
    # -- For letter between 0 and the length of letters (since letters length will change often)
    for letter in range(0, len(letters)):
        # -- Itertools method to add all 5 letter combinations of the letters from likelihoods to the combos list
        combos.extend(itertools.combinations(letters, 5))

    # -- A new list to transfer character-separated combos into strings of the combinations
    combinations = ["entry"] * len(combos)
    index = 0
    for combo in combos:
        word = ""
        for value in combo:
            word += value
        combinations[index] = word
        index += 1

    # -- Double checking that guessed words are eliminated from possibilities
    for word in possibilities:
        if(word in guessed):
            possibilities.remove(word)

    # -- Remove top word so long as the last word isn't the correct word
    if(len(possibilities)>1):
        possibilities.remove(possibilities[0])
    # -- Run gameState again using the first word in possibilities since the entries are added in order of most commonly appearing letter...
    # -- ...from the itertools combinations and likelihoods dictionary sorting
    gameState(possibilities[0].strip(), choice)

'''
    print(likelihoods.keys())
    print(likelihoods.values())
'''





def main():
    start()


if __name__ == '__main__':
    main()
            










