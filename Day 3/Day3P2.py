#Adds every number in the file to a list
with open(".\Day 3\input2.txt") as f:
    content = f.readlines()
Map = [x.strip() for x in content] 

MapArray = [list(Map[y]) for y in range(len(Map))]

Width, Drop = [1,3,5,7,1], [1,1,1,1,2]
Trees = 0
End_point = len(Map)

def numTrees(Width, Drop):
    Current_Y = 0
    Current_X = 0
    Trees = 0
    while Current_Y < End_point:
        if Current_X > (len(MapArray[0])-1):
            Current_X -= len(MapArray[0])
        if MapArray[Current_Y][Current_X] == "#":
            Trees += 1
        Current_Y += Drop
        Current_X += Width
    return Trees

print("Number of trees:",Trees)

Total = 1
for i in range(len(Width)):
    Total *= numTrees(Width[i], Drop[i])

print(Total)
# print(MapArray[2][3])
# print(MapArray[2][4])
# print(MapArray[2][5])