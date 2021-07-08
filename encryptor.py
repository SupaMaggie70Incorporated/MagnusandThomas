import os
import _random
import random
directories = os.listdir()
seed = int.from_bytes(os.urandom(8),'big')
while seed == 0:
    seed = int.from_bytes(os.urandom(8),'big')
print(seed)
random.seed(0)
#try:
#    fileToManipulate = open((input("Please enter the name of the file you wish to encrypt: ")),"r")
#except FileNotFoundError:
#    print("Experienced FileNotFoundError. Make sure you used correct capitalization and have the file extension at the end.")
content = open("hietzer.txt","rt").read()
Key = []
outputFile = open("encrypted.supencrypt",'wt')
outputFile.write("[Seed="+str(seed)+"]")
for crap in content:
    crap = list(crap)
    Key.extend(crap)
Key = list(dict.fromkeys(Key))
random.shuffle(Key)
strKey = str(Key)
bytesLOL = bytes(strKey,'utf-8')
print(bytes(Key))