#Adds every number in the file to a list
with open(".\Day 5\input2.txt") as f:
    content = f.readlines()
List = [x.strip() for x in content] 
List = [x.replace("F","0").replace("B","1").replace("R","1").replace("L","0") for x in List]

Ids = []
for Seat in List:
    Calc = int(Seat[:7], 2) * 8 + int(Seat[7:], 2)
    Ids.append(Calc)

def missing_number(num_list):
    for i in range(0, num_list[len(num_list)-1]):
        if int(num_list[i]) != (i+num_list[0]):
            return int(num_list[i]-1)

print(missing_number(sorted(Ids)))
