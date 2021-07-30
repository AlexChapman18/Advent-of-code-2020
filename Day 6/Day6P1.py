#Adds every number in the file to a list
with open(".\Day 6\input.txt") as f:
    content = f.readlines()
List = [x.strip() for x in content] 

#Creates a list, with each item being all the data for 1 person
RawPeople = []
HolderString = ""
for row in List:
    if row != "":
        if HolderString == "":
            HolderString += row
        else:
            HolderString += " " + row
    else:
        RawPeople.append(HolderString)
        HolderString = ""
RawPeople.append(HolderString)

# print(RawPeople)
Count = 0
for Sets in RawPeople:
    Sets = Sets.split(" ")
    chars = set.intersection(Set1, Set2, Set3)
    # chars = set.intersection(*[set(i) for i in Sets])
    Count += len(chars)
print (Count)

#    print(Compare_values)







    # if Valid == True:
    #     Count += 1












    # [Sets.split(" ") for Sets in Group]





# Count = 0
# for Group in RawPeople:
#     Count += len(set(Group))

# print(Count)
