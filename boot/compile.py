
with open('components/ir_memory.vhd', 'r') as file:
    code_lines = file.readlines()
    
with open('components/ir_memory.vhd', 'w') as f:
        for line in code_lines:
            words = line.strip().split(" ")
            if len(words) > 3:
                if words[0] == 'signal' and words[1] == 'ir_mem' and  words[2] == ':' and words[3] == 'ir_array:=(':
                    line = f'signal ir_mem : ir_array:=(  others => x"EFFF" );\n\t'
                    # print(line)
                    f.write(line)
                    continue
            f.write(line)

import os

os.system('quartus_map --read_settings_files=on --write_settings_files=off IITB_RISC_23_Pipelined_Processor -c IITB_RISC_23_Pipelined_Processor ')