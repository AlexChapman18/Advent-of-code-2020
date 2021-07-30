with open(".\Day 9\input.txt") as f:
    content = f.readlines()
NumberList = [int(x.strip()) for x in content]

MagicNumber = False
MagicSet = False
PreambleLength = 25
CurrentAmble = 0

while MagicNumber == False:
    Amble = NumberList[CurrentAmble:(PreambleLength+CurrentAmble)]
    CurrentNumber = NumberList[(PreambleLength+CurrentAmble)]
    Found = False
    for i in range(0,len(Amble)):
        for j in range(0,len(Amble)):
            if Amble[i] + Amble[j] == CurrentNumber and i != j:
                Found = True

    if Found == False:
        MagicNumber = CurrentNumber
    CurrentAmble += 1

print(MagicNumber)


CurrentAmble = 0
AmbleLength = 2
while MagicSet == False:
    while sum(Amble) <= MagicNumber:
        Amble = NumberList[CurrentAmble:(AmbleLength+CurrentAmble)]
        if sum(Amble) != MagicNumber:
            AmbleLength += 1
        else:
            MagicSet = sorted(Amble)
            MagicSum = MagicSet[0] + MagicSet[-1]
            print(MagicSum)
            break
    AmbleLength = 2
    Amble = []
    CurrentAmble += 1 


print(MagicSet)