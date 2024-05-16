from  sys import argv

asmCode ="M= D-1; JLT"

def assemblyParser(asmCode):
    def decTo15bin(num):
        b = str(bin(num))[2:]
        b = "0"*(15-len(b)) + b
        return b
    machineCode = "oxxAccccccdddj1j2j3"
    asmCode = asmCode.replace(" ","")
    #check if comment
    if(asmCode[0:2] == "//" or asmCode==""):
        return False

    if(asmCode[0] == "@"):
        #A-instruction
        machineCode = "0"+decTo15bin(int(asmCode[1:]))
    else:
        #C-instruction
        machineCode = machineCode.replace("oxx","111")
        if("=" in asmCode):
            dest = asmCode.split("=")[0]
        else:
            dest=""
            asmCode = "n="+asmCode
        if(";" in asmCode):
            jump = asmCode.split(";")[1]
        else:
            jump = ""
            asmCode = asmCode+";n"

        comp = asmCode.split("=")[1].split(";")[0]


        #destination
        d1 = "1" if("A" in dest) else "0"
        d2 = "1" if("D" in dest) else "0"
        d3 = "1" if("M" in dest) else "0"
        machineCode = machineCode.replace("ddd",d1+d2+d3)

        #jump
        if(jump == "JMP"):
            machineCode = machineCode.replace("j1j2j3","111")
        elif(jump == "JNE"):
            machineCode = machineCode.replace("j1j2j3","101")
        else:
            jumpGT = "1" if ("G" in jump) else "0"
            jumpLT = "1" if ("L" in jump) else "0"
            jumpEQ = "1" if ("E" in jump) else "0"
            machineCode = machineCode.replace("j3",jumpGT)
            machineCode = machineCode.replace("j2",jumpEQ)
            machineCode = machineCode.replace("j1",jumpLT)
        
        #A or M
        am = "1" if("M" in comp) else "0"
        machineCode = machineCode.replace("A",am)

        #comp bits
        comp = comp.replace("M","A")
        commandBitDict = {
            "0"  :'101010',
            "1"  :'111111',
            "-1" :'111010',
            "D"  :'001100',
            "A"  :'110000',
            "!D" :'001101',
            "!A" :'110001',
            "-D" :'001111',
            "-A" :'110011',
            "D+1":'011111',
            "A+1":'110111',
            "D-1":'001110',
            "A-1":'110010',
            "D+A":'000010',
            "D-A":'010011',
            "A-D":'000111',
            "D&A":'000000',
            "D|A":'010101'
        }
        compBit = commandBitDict[comp]
        machineCode = machineCode.replace("cccccc",compBit)
    return machineCode



with open (argv[1],"r") as asmFile:
    for asmc in asmFile.readlines():
        asmc = asmc.replace("\n","")
        print(assemblyParser(asmc))

