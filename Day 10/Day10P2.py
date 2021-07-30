with open(".\Day 10\input.txt") as f:
    content = f.readlines()
JoltageAdapterList = [int(x.strip()) for x in content]

sortedList = sorted(JoltageAdapterList)
print(sortedList)


#Find differences
DifferencesList = []
for i in range(0, len(sortedList)-1):
    DifferencesList.append(sortedList[i+1]-sortedList[i])


consecutive = []
ClusterLength = 0
for i in range(0, len(DifferencesList)):
    if DifferencesList[i] == 1:
        ClusterLength += 1
    else:
        consecutive.append(ClusterLength)
        ClusterLength = 0

print(sum(consecutive))
MagicNumber = 1
for Number in consecutive:
    if Number == 4:
        MagicNumber *= 7
    elif Number == 3:
        MagicNumber *= 4
    elif Number == 2:
        MagicNumber *= 2

print(MagicNumber)


# print(sortedList)
print(DifferencesList)
print(DifferencesList.count(1)+1)
print(DifferencesList.count(3)+1)