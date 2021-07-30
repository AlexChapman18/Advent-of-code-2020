#Adds every number in the file to a list
from copy import deepcopy

with open(".\Day 11\input.txt") as f:
    content = f.readlines()
Grid = [list(x.strip()) for x in content] 

def ReturnAdjacents(Grid, Coords):
    AdjacentValues = []
    for x in range((Coords[0]-1), (Coords[0]+2)):
        for y in range((Coords[1]-1), (Coords[1]+2)):
            if [Coords[0], Coords[1]] != [x, y]:
                if x >= 0 and y >= 0 and x < len(Grid[0]) and y < len(Grid): 
                    AdjacentValues.append(Grid[y][x])
    return AdjacentValues

NewGrid = Grid[:]
while True:
    Grid = deepcopy(NewGrid)
    for x in range(0, len(Grid[0])):
        for y in range(0, len(Grid)):
            AdjacentValues = ReturnAdjacents(Grid, [x,y])
            if Grid[y][x] == "L" and AdjacentValues.count("#") == 0:
                NewGrid[y][x] = "#"
            elif  Grid[y][x] == "#" and AdjacentValues.count("#") >= 4:
                NewGrid[y][x] = "L"
    if Grid == NewGrid:
        TotalOccupied = 0
        for row in Grid:
            TotalOccupied += row.count("#")
        print(TotalOccupied)
        break
print(Grid)
