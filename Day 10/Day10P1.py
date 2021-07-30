with open(".\Day 10\input.txt") as f:
    content = f.readlines()
JoltageAdapterList = [int(x.strip()) for x in content]

sortedList = sorted(JoltageAdapterList)

#Find differences
DifferencesList = []
for i in range(0, len(sortedList)-1):
    DifferencesList.append(sortedList[i+1]-sortedList[i])


print(DifferencesList.count(1)+1)
print(DifferencesList.count(3)+1)