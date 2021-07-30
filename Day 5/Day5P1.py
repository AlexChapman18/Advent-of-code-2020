#Adds every number in the file to a list
with open(".\Day 5\input.txt") as f:
    content = f.readlines()
List = [x.strip() for x in content] 
List = [x.replace("F","0").replace("B","1").replace("R","1").replace("L","0") for x in List]

Ids = []
for Seat in List:
    Calc = int(Seat[:7], 2) * 8 + int(Seat[7:], 2)
    Ids.append(Calc)

print(sorted(Ids)[-1])