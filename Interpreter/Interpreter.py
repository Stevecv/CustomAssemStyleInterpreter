import re


program = "Data{0,1,false,10,0}Program{ADD 0, 1;PRNT 0;MOV 0, 2;EQL 2, 3;NOT 2;IF 2, 4;END;}".replace("\n", "")


dataSet = re.findall("Data{(.*?)}", program)[0].split(",")
instructions = re.findall("Program{(.*?)}", program)[0].split(";")
registers = []

def getData(address):
    if (address.isnumeric()):
        return dataSet[int(address)]
    else:
        print(address)
        return registers[ord(address)]


def saveData(address, data):
    if (address.isnumeric()):
        dataSet[int(address)] = data
    else:
        address =  address.lower()
        numericAddress = ord(address)-97
        if (len(registers) <= numericAddress):
            diff = numericAddress-len(registers)

            for i in range(0,diff+1):
                registers.append("")

            registers[numericAddress] = data
        else:
            registers[numericAddress] = data

def isNum(number):
    return re.match("^-?[0-9]\d*(\.\d+)?$", number)


runLen = len(instructions)
pc = 0
while pc < runLen:
    instruction = instructions[pc].strip()
    if (instruction == "END"):
        print("Exit code 0")
        break


    cmd = re.findall("^(.*?) ", instruction)[0].upper()
    instruction_data = re.sub(re.compile("^" + cmd), "", instruction).split(",")

    for i in range(0, len(instruction_data)):
        instruction_data[i] = instruction_data[i].strip()

    
    if (cmd == "ADD"):
        saveData(instruction_data[0], str(float(getData(instruction_data[0])) + float(getData(instruction_data[1]))))
    elif (cmd == "MIN"):
        saveData(instruction_data[0], str(float(getData(instruction_data[0])) - float(getData(instruction_data[1]))))
    elif (cmd == "MUL"):
        saveData(instruction_data[0], str(float(getData(instruction_data[0])) * float(getData(instruction_data[1]))))
    elif (cmd == "DIV"):
        saveData(instruction_data[0], str(float(getData(instruction_data[0])) / float(getData(instruction_data[1]))))

    elif (cmd == "JMP"):
        pc = int(instruction_data[0])-1

    elif (cmd == "MOV"):
        saveData(instruction_data[1], getData(instruction_data[0]))

    elif (cmd == "EQL"):
        data1 = getData(instruction_data[0])
        data2 = getData(instruction_data[1])

        if (isNum(data1) and isNum(data2)):
            data1 = float(data1)
            data2 = float(data2)
        elif (isNum(data1) != isNum(data2)):
            saveData(instruction_data[0], "false")

        if (data1 == data2):
            saveData(instruction_data[0], "true")
        else:
            saveData(instruction_data[0], "false")

    elif (cmd == "NOT"):
        if (getData(instruction_data[0]) == "true"):
            saveData(instruction_data[0], "false")
        else:
            saveData(instruction_data[0], "true")

    elif (cmd == "IF"):
        if (getData(instruction_data[0]) == "true"):
            pc = int(getData(instruction_data[1]))-1

    elif (cmd == "PRNT"):
        print(getData(instruction_data[0]))


    pc += 1