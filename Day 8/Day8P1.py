with open(".\Day 8\input.txt") as f:
    content = f.readlines()
MachineCode = [x.strip().replace(" ", "") for x in content] 


for Line in range(0, len(MachineCode)-1):
    Pointer = 0
    Accumulator = 0
    RunLines = []
    if MachineCode[Line][:3] == "nop":
        MachineCode[Line] = MachineCode[Line].replace("nop", "jmp")
    elif MachineCode[Line][:3] == "jmp":
        MachineCode[Line] = MachineCode[Line].replace("jmp", "nop")


    while Pointer not in RunLines:
        RunLines.append(Pointer)
        if MachineCode[Pointer][:3] == "acc":
            if MachineCode[Pointer][3] == "+":
                Accumulator += int(MachineCode[Pointer][4:])
            else:
                Accumulator -= int(MachineCode[Pointer][4:])
        elif MachineCode[Pointer][:3] == "jmp":
            if MachineCode[Pointer][3] == "+":
                Pointer += int(MachineCode[Pointer][4:]) - 1
            else:
                Pointer -= int(MachineCode[Pointer][4:]) + 1
        Pointer += 1
        if Pointer == len(MachineCode):
            print(Accumulator)
        elif Pointer > len(MachineCode):
            break

    if MachineCode[Line][:3] == "nop":
        MachineCode[Line] = MachineCode[Line].replace("nop", "jmp")
    elif MachineCode[Line][:3] == "jmp":
        MachineCode[Line] = MachineCode[Line].replace("jmp", "nop")



        




