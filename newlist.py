
### -- Use of nltk library to create better word list

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('words')

from nltk.corpus import words

wordList = [word.lower() for word in words.words() if len(word) == 5]

newList = open('edict.txt', 'w')

newList.write('\n'.join(wordList))

newList.close()