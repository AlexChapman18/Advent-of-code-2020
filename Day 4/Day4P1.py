#Adds every number in the file to a list
with open(".\Day 4\input2.txt") as f:
    content = f.readlines()
List = [x.strip() for x in content] 

Identifiers = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #cid
Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
colour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

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

Dictionaries = []
for Person in RawPeople:
    Dictionary = {}
    Person = Person.split(" ")
    for bit in Person:
        Dictionary[bit.split(":")[0]] = bit.split(":")[1]
    Dictionaries.append(Dictionary)


ValidIshDictionaries =[]
Valid = 0
for Dictionary in Dictionaries:
    if all( item in Dictionary for item in Identifiers):
        Valid += 1
        ValidIshDictionaries.append(Dictionary)

print("PreValid",Valid)
all_valid = -1

for Dictionary in ValidIshDictionaries:
    Valid = True
    #byr
    if len(Dictionary["byr"]) != 4:
        Valid = False
    if int(Dictionary["byr"]) < 1920 or  int(Dictionary["byr"]) > 2002:
        Valid = False
    #iyr
    if len(Dictionary["iyr"]) != 4:
        Valid = False
    if int(Dictionary["iyr"]) < 2010 or  int(Dictionary["iyr"]) > 2020:
        Valid = False
    #eyr
    if len(Dictionary["eyr"]) != 4:
        Valid = False
    if int(Dictionary["eyr"]) < 2020 or  int(Dictionary["byr"]) > 2030:
        Valid = False
    #hgt
    if ''.join([i for i in Dictionary["hgt"] if not i.isdigit()]) == "cm":
        if int(''.join([i for i in Dictionary["hgt"] if i.isdigit()])) < 150 or int(''.join([i for i in Dictionary["hgt"] if i.isdigit()])) > 193:
            Valid = False
    elif ''.join([i for i in Dictionary["hgt"] if not i.isdigit()]) == "in":
        if int(''.join([i for i in Dictionary["hgt"] if i.isdigit()])) < 59 or int(''.join([i for i in Dictionary["hgt"] if i.isdigit()])) > 76:
            Valid = False
    else:
        Valid = False
    #hcl
    if Dictionary["hcl"][0] != "#" or len(Dictionary["hcl"].replace("#","")) != 6 or not (i for i in (Dictionary["hcl"].replace("#","")) if i in Hex):
        Valid = False
    #ecl
    if Dictionary["ecl"] not in colour:
        Valid = False
    #pid
    if len(Dictionary["pid"]) != 9 or not (i for i in Dictionary["hgt"] if i.isdigit()):
        Valid = False

    if Valid == True:
        all_valid += 1
print(all_valid)

Set = ["abc", "abcd", "cheese"]

print([[i] for i in Set])

["abc"] ["abcd"] ["cheese"]