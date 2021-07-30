#Adds every number in the file to a list
with open(".\Day 3\input.txt") as f:
    content = f.readlines()
Map = [x.strip() for x in content] 

MapArray = [list(Map[y]) for y in range(len(Map))]

Width, Drop = 3, 1
Trees = 0
NoTrees = 0
Current_X = 0
Current_Y = 0
End_point = len(Map)

while Current_X != End_point:
    if Current_Y > (len(MapArray[0])-1):
        Current_Y -= len(MapArray[0])
    if MapArray[Current_X][Current_Y] == "#":
        Trees += 1
    else:
        NoTrees += 1
    Current_X += 1
    Current_Y += 3

print("Number of trees:",Trees,"Number of no trees:",NoTrees)

# print(MapArray[2][3])
# print(MapArray[2][4])
# print(MapArray[2][5])