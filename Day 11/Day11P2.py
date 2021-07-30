#Adds every number in the file to a list
from copy import deepcopy

with open(".\Day 11\input.txt") as f:
    content = f.readlines()
Grid = [list(x.strip()) for x in content] 

def ReturnAdjacents(Grid, Coords):
    # if Coords == [len(Grid[0])-1, 6]:
    #     print()
    AdjacentValues = []
    #CheckUp
    for y in range(Coords[1], -1, -1):
        if Grid[y][Coords[0]] != "." and y != Coords[1]:   
            AdjacentValues.append(Grid[y][Coords[0]])
            break
    for y in range(Coords[1], len(Grid)):
        if Grid[y][Coords[0]] != "." and y != Coords[1]:
            AdjacentValues.append(Grid[y][Coords[0]])
            break
    for x in range(Coords[0], -1, -1):
        if Grid[Coords[1]][x] != "." and x != Coords[0]:
            AdjacentValues.append(Grid[Coords[1]][x])
            break
    for x in range(Coords[0], len(Grid[0])):
        if Grid[Coords[1]][x] != "." and x != Coords[0]:
            AdjacentValues.append(Grid[Coords[1]][x])
            break

    n = 1
    while True:
        try:
            if Coords[1]+n >= 0 and Coords[0]+n >= 0 and Coords[1]+n < len(Grid) and Coords[0]+n < len(Grid[0]):
                if Grid[Coords[1]+n][Coords[0]+n] != ".": 
                    AdjacentValues.append(Grid[Coords[1]+n][Coords[0]+n])
                    break
            else:
                break
            n += 1
        except:
            break
    n = 1
    while True:
        try:
            if Coords[1]-n >= 0 and Coords[0]+n >= 0 and Coords[1]-n < len(Grid) and Coords[0]+n < len(Grid[0]):
                if Grid[Coords[1]-n][Coords[0]+n] != ".": 
                    AdjacentValues.append(Grid[Coords[1]-n][Coords[0]+n])
                    break
            else:
                break
            n += 1
        except:
            break
    n = 1
    while True:
        try:
            if Coords[1]-n >= 0 and Coords[0]-n >= 0 and Coords[1]-n < len(Grid) and Coords[0]-n < len(Grid[0]):
                if Grid[Coords[1]-n][Coords[0]-n] != ".": 
                    AdjacentValues.append(Grid[Coords[1]-n][Coords[0]-n])
                    break
            else:
                break
            n += 1
        except:
            break
    n = 1
    while True:
        try:
            if Coords[1]+n >= 0 and Coords[0]-n >= 0 and Coords[1]+n < len(Grid) and Coords[0]-n < len(Grid[0]):
                if Grid[Coords[1]+n][Coords[0]-n] != ".":
                    AdjacentValues.append(Grid[Coords[1]+n][Coords[0]-n])
                    break
            else:
                break
            n += 1
        except:
            break
    
    # print(AdjacentValues)
    return AdjacentValues




NewGrid = Grid[:]
while True:
    Grid = deepcopy(NewGrid)
    for x in range(0, len(Grid[0])):
        for y in range(0, len(Grid)):
            AdjacentValues = ReturnAdjacents(Grid, [x,y])
            if Grid[y][x] == "L" and AdjacentValues.count("#") == 0:
                NewGrid[y][x] = "#"
            elif  Grid[y][x] == "#" and AdjacentValues.count("#") >= 5:
                NewGrid[y][x] = "L"
    if Grid == NewGrid:
        TotalOccupied = 0
        for row in Grid:
            TotalOccupied += row.count("#")
        print(TotalOccupied)
        break
