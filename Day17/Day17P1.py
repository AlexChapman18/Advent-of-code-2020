with open(".\Day 8\input.txt") as f:
    content = f.readlines()
InputFile = [x.strip() for x in content] 


n=100

BlankArray = [[[0 for x in range(n)] for y in range(n)] for z in range(n)]
print(BlankArray)

class Node:
    def __init__(self, active, NextActive):
        self.active = active
        self.NextActive = NextActive



