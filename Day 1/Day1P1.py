TargetNum = 2020
Start_point = 0

#Adds every number in the file to a list
with open(".\Day 1\input.txt") as f:
    content = f.readlines()
Number_List = [int(x.strip()) for x in content] 

#Sorts the number list
Sorted_Number_List = sorted(Number_List)

print(Sorted_Number_List)

#Find number below half of target number
for Number in Sorted_Number_List:
    if Number < (TargetNum/2):
        Start_point += 1
    else:
        break

print(Start_point)
print(Sorted_Number_List[Start_point])

#Itterated through the Values below half of the target number beucase you cant have 2 values if 2 of them are above half of the target
for x in range(0, Start_point):
    for y in range(Start_point, (len(Sorted_Number_List)-1)):
        if (Sorted_Number_List[x] + Sorted_Number_List[y]) == TargetNum:
            print("Found Pair", Sorted_Number_List[x], Sorted_Number_List[y])
