#Adds every number in the file to a list
with open(".\Day 2\input2.txt") as f:
    content = f.readlines()
List = [x.strip() for x in content] 

print(List[0])

#A function that check if a password is valid with the format "4-5 t: ftttttrvts"
def check_password(Input_Row):
    #Splits the input into a list of ["4-5","t:","ftttttrvts"]
    Input_Row = Input_Row.split(" ")
    #Splits it again to get the min and max number of the character
    Char1_pos = int(Input_Row[0].split("-")[0])
    Char2_pos = int(Input_Row[0].split("-")[1])
    #Find the letter that need to beck checked
    letter = list(Input_Row[1])[0]
    Password_Text = Input_Row[2]
    return (letter == list(Password_Text)[Char1_pos-1]) != (letter == list(Password_Text)[Char2_pos-1])



Good, Bad = 0, 0
for Password in List:
    is_valid = check_password(Password)
    if is_valid == True:
        Good += 1
    else:
        Bad += 1
print("Good Passwords:",Good,"Bad Passwords:",Bad)