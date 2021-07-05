import random
def randomLetter(excludedList = [],capital = False):
    excludedList = list(dict.fromkeys(excludedList))
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for listLetter in excludedList:
        letterIndex = excludedList.index(listLetter)
        listLetter = listLetter.lower()
        excludedList[letterIndex] = listLetter
    for listLetter in excludedList:
        try:
            alphabet.remove(listLetter)
        except ValueError:
            pass
    if not capital:
        return(random.choice(alphabet))
    else:
        return((random.choice(alphabet)).upper)
def randomLetters(excludedList = [],listLength = 1,capital = False):
    excludedList = list(dict.fromkeys(excludedList))
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for listLetter in excludedList:
        letterIndex = excludedList.index(listLetter)
        listLetter = listLetter.lower()
        excludedList[letterIndex] = listLetter
    for listLetter in excludedList:
        try:
            alphabet.remove(listLetter)
        except ValueError:
            pass
    returnedValue = (random.choices(alphabet,k=listLength))
    if capital:
        for i in range(len(returnedValue)):
            pass
    return(random.choices(alphabet,k=listLength))
def noRepRandomLetters(excludedList = [],listLength = 1,capital = False):
    returnedValue = []
    excludedList = list(dict.fromkeys(excludedList))
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for listLetter in excludedList:
        letterIndex = excludedList.index(listLetter)
        listLetter = listLetter.lower()
        excludedList[letterIndex] = listLetter
    for listLetter in excludedList:
        try:
            alphabet.remove(listLetter)
        except ValueError:
            pass
    for i in range(listLength):
        letterToAdd = random.choice(alphabet)
        alphabet.remove(letterToAdd)
        if not capital:
            returnedValue.append(letterToAdd)
        elif capital:
            returnedValue.append((letterToAdd).upper)
    print(len(returnedValue))
    return(returnedValue)
print(noRepRandomLetters(listLength=26))