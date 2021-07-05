import random
def randomLetter(excludedList = []):
    global letter
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
    return(random.choice(alphabet))
def randomLetters(excludedList = [],listLength = 1):
    global letter
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
    return(random.choices(alphabet,k=listLength))
print(randomLetters(listLength=3))