import re
from  sys import argv

class AssemblyLine:

    def __init__(self, asmc):
        #destination=computation;jump;
        self.command = asmc
        self.is_a_inst = False
        self.is_c_inst = False
        if(asmc[0] == "@"):
            self.is_a_inst = True
        else:
            self.is_c_inst = True
    
    def decimal_to_15bit_binary(self, num):
        b = str(bin(num))[2:]
        b = "0"*(15-len(b)) + b
        return b

    def process_A_instruction(self):
        self.binary = "0"+self.decimal_to_15bit_binary(int(self.command[1:]))

    def process_C_instruction(self):
        pattern = r"^([ADM]+=)?(.*?)(;J[A-Z]+)?$"
        match = re.match(pattern, self.command)

        self.dest = match.group(1)[:-1] if match.group(1) else "null"
        self.comp = match.group(2)
        self.jump = match.group(3)[1:] if match.group(3) else "null"

        dest_dict = {
            "null"  :   "000",
            "M"     :   "001",
            "D"     :   "010",
            "DM"    :   "011",
            "A"     :   "100",
            "AM"    :   "101",
            "AD"    :   "110",
            "ADM"   :   "111"
        }
        
        comp_dict = {
            "0"     :   '101010',
            "1"     :   '111111',
            "-1"    :   '111010',
            "D"     :   '001100',
            "A"     :   '110000',
            "!D"    :   '001101',
            "!A"    :   '110001',
            "-D"    :   '001111',
            "-A"    :   '110011',
            "D+1"   :   '011111',
            "A+1"   :   '110111',
            "D-1"   :   '001110',
            "A-1"   :   '110010',
            "D+A"   :   '000010',
            "D-A"   :   '010011',
            "A-D"   :   '000111',
            "D&A"   :   '000000',
            "D|A"   :   '010101'
        }
                
        jump_dict = {
            "null"  :   "000",
            "JGT"   :   "001",
            "JEQ"   :   "010",
            "JGE"   :   "011",
            "JLT"   :   "100",
            "JNE"   :   "101",
            "JLE"   :   "110",
            "JMP"   :   "111"
        }

        self.dest = "".join(sorted(list(self.dest))) if(self.dest!="null") else self.dest       
        dest_bits = dest_dict[self.dest]
        comp_bits = comp_dict[(self.comp).replace("M","A")]
        jump_bits = jump_dict[self.jump]
        a_bit = "1" if("M" in self.comp) else "0"

        self.binary = "111"+a_bit+comp_bits+dest_bits+jump_bits


clean_commands = []
clean_commands_no_var = []
symbol_table = {
    "R0"        :   "0",
    "R1"        :   "1",
    "R2"        :   "2",
    "R3"        :   "3",
    "R4"        :   "4",
    "R5"        :   "5",
    "R6"        :   "6",
    "R7"        :   "7",
    "R8"        :   "8",
    "R9"        :   "9",
    "R10"       :   "10",
    "R11"       :   "11",
    "R12"       :   "12",
    "R13"       :   "13",
    "R14"       :   "14",
    "R15"       :   "15",
    "SCREEN"    :   "16384",
    "KBD"       :   "24576",
    "SP"        :   "0",
    "LCL"       :   "1",
    "ARG"       :   "2",
    "THIS"      :   "3",
    "THAT"      :   "4"
    }

variable_counter= 16
line_number= 0

#extracting and cleaning
with open (argv[1],"r") as asmFile:
    for asmc in asmFile.readlines():
        cmnd = asmc.replace("\n","")
        cmnd = cmnd.replace(" ","")
        
        #cleaning
        if(cmnd[:2] == "//" or cmnd==""):
            continue

        #labels
        if(cmnd[0]=="(" and cmnd[-1]==")"):
            symbol_table[cmnd[1:-1]] = str(line_number)
            continue
                
        line_number+=1
        clean_commands_no_var.append(cmnd)

for cmnd in clean_commands_no_var:
    #variables
    if(re.findall("@[A-Za-z]\w*",cmnd)):
        sym_key = cmnd[1:]
        if(sym_key not in symbol_table.keys()):
            symbol_table[sym_key] = str(variable_counter)
            variable_counter+=1
        cmnd = cmnd.replace(sym_key,symbol_table[sym_key])
    
    clean_commands.append(cmnd)

#processing commands
with open(argv[1].split("/")[-1].replace(".asm",".hack"),"w") as hack_file:
    for cmnd in clean_commands:
        line = AssemblyLine(cmnd)
        if(line.is_c_inst):
            line.process_C_instruction()
            binr = line.binary
        elif(line.is_a_inst):
            line.process_A_instruction()
            binr = line.binary
        else:
            continue
        hack_file.write(binr+"\n")