import random

def GenerateRandomKey(NumberOfCharacters):
    data = ""
    while NumberOfCharacters > 0:
        list = [1,2,3]
        x = random.choice(list)
        if x == 1:
            data += str(GetRandomNumber())
        elif x == 2:
            data += GetRandomAlphabet()
        elif x == 3:
            data += GetRandomSpecialCharacter()
        NumberOfCharacters -= 1
    return data
  
def GetRandomNumber():
    list = [1,2,3,4,5,6,7,8,9,0]
    return random.choice(list)

def GetRandomAlphabet():
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return random.choice(list)

def GetRandomSpecialCharacter():
    list = ['@','#','_','=','$','!','&','+','-']
    return random.choice(list)
