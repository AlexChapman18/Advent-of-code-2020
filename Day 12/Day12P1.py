with open(".\Day 12\input.txt") as f:
    content = f.readlines()
Directions = [x.strip() for x in content] 


North = 0
East = 0
Angle = 3690
for Line in Directions:
    Char = Line[0]
    if Char == "N" or Char == "S":
        if Char == "N":
            North += int(Line[1:])
        else:
            North -= int(Line[1:])
    if Char == "E" or Char == "W":
        if Char == "E":
            East += int(Line[1:])
        else:
            East -= int(Line[1:])
    if Char == "L" or Char == "R":
        if Char == "L":
            Angle -= int(Line[1:])
        else:
            Angle += int(Line[1:])
    if Char == "F":
        UsefulAngle = int(Angle % 360)
        if UsefulAngle == 0:
            North += int(Line[1:])
        elif UsefulAngle == 90:
            East += int(Line[1:])
        elif UsefulAngle == 180:
            North -= int(Line[1:])
        else:
            East -= int(Line[1:])
    
print(abs(North) + abs(East))