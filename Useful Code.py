#Adds every number in the file to a list
with open(".\Day 1\input.txt") as f:
    content = f.readlines()
List = [x.strip() for x in content] 

#Sorts the number list
List = sorted(Number_List)

#Find commonanalities in lists
for Strings in List_of_List_of_strings:
    chars = set.intersection(*[set(i) for i in Strings])
    #Chars = common chars in strings

#For number Input List
with open(".\Day 9\input.txt") as f:
    content = f.readlines()
InputList = [int(x.strip()) for x in content]


#*star before list unpacks it


Use [ # : # ] to get set of letter

Keep in mind that python, as many other languages, starts to count from 0!!

word = "Hello World"

print word[0] #get one char of the word
print word[0:1] #get one char of the word (same as above)
print word[0:3] #get the first three char
print word[:3] #get the first three char
print word[-3:] #get the last three char
print word[3:] #get all but the three first char
print word[:-3] #get all but the three last character

word = "Hello World"

word[start:end] # items start through end-1
word[start:] # items start through the rest of the list
word[:end] # items from the beginning through end-1
word[:] # a copy of the whole list