def DECORDER(program_inst):
        global memory
        global registor
        opreand2 = program_inst[9:13]
        operand1 = "0"+program_inst[6:9]
        print(program_inst)
        operand3 = "0"+program_inst[13:17]
        if program_inst[0] == "0":
            if program_inst[1:5] == '0000':
                registor[operand1] = ALU(str(operand3), 0, str(opreand2))
            elif program_inst[1:5] == '0001':
                registor[operand1] = ALU(str(operand3), 1, str(opreand2))
            elif program_inst[1:5] == '0010':
                registor[operand1] = ALU(str(operand3), 2, str(opreand2))
            elif program_inst[1:5] == '0011':
                registor[operand1] = ALU(str(operand3), 3, str(opreand2))
            elif program_inst[1:5] == '0100':
                registor[operand1] = ALU(str(operand3), 4, str(opreand2))
        else:
            if program_inst[1:5] == '0101':
                opreand2 = memory[program_inst[9:13]]
                registor[operand1] = opreand2
            else:
                memory[opreand2] = registor[operand1]


def IR(program_inst):
        global PC
        DECORDER(program_inst)
        PC += 1


def ALU(a, ctr, y='4'):
    a = '0' if a.lstrip('0') == "" else a.lstrip('0')
    y = '0' if y.lstrip('0') == "" else y.lstrip('0')
    if ctr == 0:
        return bin(int(a, 2) + int(y, 2))[2:]
    elif ctr == 1:

        return bin(int(a, 2) - int(y, 2))[2:]
    elif ctr == 2:

        return bin(int(a, 2) & int(y, 2))[2:]
    elif ctr == 3:

        return bin(int(a, 2) | int(y, 2))[2:]
    elif ctr == 4:

        return bin(int(a, 2) ^ int(y, 2))[2:]
   
if __name__ == "__main__":
    instruction = []
    memory = {}
    registor = {"0000": 0, "0001": 0, "0010": 0, "0011": 0, "0100": 0, "0101": 0, "0110": 0, "0111": 0}
    PC = 0
    # print("hi")
    with open('program.txt') as f:
        lines = f.readlines()
        for line in lines:
            instruction.append(line.split()[0])
    with open('data.txt') as g:
        lines = g.readlines()
        for line in lines:
            data = line.split()
            memory[data[0]] = data[1]
    while (PC != len(instruction)):
        IR(instruction[PC])
        print(memory)
        print(registor)
