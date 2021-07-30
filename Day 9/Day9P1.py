with open(".\Day 9\input.txt") as f:
    content = f.readlines()
NumberList = [x.strip() for x in content]

MagicNumber = False
PreambleLength = 25
CurrentAmble = 0

while MagicNumber == False:
    Amble = NumberList[CurrentAmble:(PreambleLength+CurrentAmble)]
    CurrentNumber = NumberList[(PreambleLength+CurrentAmble)]
    Found = False
    for i in range(0,len(Amble)):
        for j in range(0,len(Amble)):
            if int(Amble[i]) + int(Amble[j]) == int(CurrentNumber) and i != j:
                Found = True

    if Found == False:
        print(CurrentNumber)
        break

    CurrentAmble += 1
