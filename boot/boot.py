def boot():
    for i in range(x):
        if (word_arrays[i][0] == 'ADA'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('000')
            
        if (word_arrays[i][0] == 'ADC'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('010')
        
        if (word_arrays[i][0] == 'ADZ'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('001')
            
        if (word_arrays[i][0] == 'AWC'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('011')
            
        if (word_arrays[i][0] == 'ACA'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('100')
            
        if (word_arrays[i][0] == 'ACC'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('110')
            
        if (word_arrays[i][0] == 'ACZ'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('101')
            
        if (word_arrays[i][0] == 'ACW'):
            output_arrays[i][0] = '0001'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('111')
            
        if (word_arrays[i][0] == 'NDU'):
            output_arrays[i][0] = '0010'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('000')
        
        if (word_arrays[i][0] == 'NDC'):
            output_arrays[i][0] = '0010'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('010')
            
        if (word_arrays[i][0] == 'NDZ'):
            output_arrays[i][0] = '0010'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('001')
            
        if (word_arrays[i][0] == 'NCU'):
            output_arrays[i][0] = '0010'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('100')
        
        if (word_arrays[i][0] == 'NCC'):
            output_arrays[i][0] = '0010'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('110')
            
        if (word_arrays[i][0] == 'NCZ'):
            output_arrays[i][0] = '0010'
            for j in range(3):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('101')
            
        
        if (word_arrays[i][0] == 'ADI'):
            output_arrays[i][0] = '0000'
            for j in range(2):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][3] = word_arrays[i][3]
        
        if (word_arrays[i][0] == 'LLI'):
            output_arrays[i][0] = '0011'
            for j in range(1):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][2] = word_arrays[i][2]
        
        if (word_arrays[i][0] == 'BEQ'):
            output_arrays[i][0] = '1000'
            for j in range(2):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][3] = word_arrays[i][3]
        
        if (word_arrays[i][0] == 'LW'):
            output_arrays[i][0] = '0100'
            for j in range(2):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][3] = word_arrays[i][3]
            
        if (word_arrays[i][0] == 'SW'):
            output_arrays[i][0] = '0101'
            for j in range(2):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][3] = word_arrays[i][3]
        
        if (word_arrays[i][0] == 'BLT'):
            output_arrays[i][0] = '1001'
            for j in range(2):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][3] = word_arrays[i][3]
            
        if (word_arrays[i][0] == 'BLE'):
            output_arrays[i][0] = '1011'
            for j in range(2):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][3] = word_arrays[i][3]
        
        if (word_arrays[i][0] == 'LM'):
            output_arrays[i][0] = '0110'
            for j in range(1):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][2] = word_arrays[i][2]
        if (word_arrays[i][0] == 'SM'):
            output_arrays[i][0] = '0111'
            for j in range(1):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][2] = word_arrays[i][2]

        
        if (word_arrays[i][0] == 'JAL'):
            output_arrays[i][0] = '1100'
            for j in range(1):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][2] = word_arrays[i][2]

        if (word_arrays[i][0] == 'JRI'):
            output_arrays[i][0] = '1111'
            for j in range(1):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i][2] = word_arrays[i][2]
        
        if (word_arrays[i][0] == 'JLR'):
            output_arrays[i][0] = '1101'
            for j in range(2):
                if (word_arrays[i][j+1] == 'R0'):
                    output_arrays[i][j+1] = '000'
                if (word_arrays[i][j+1] == 'R1'):
                    output_arrays[i][j+1] = '001'
                if (word_arrays[i][j+1] == 'R2'):
                    output_arrays[i][j+1] = '010'
                if (word_arrays[i][j+1] == 'R3'):
                    output_arrays[i][j+1] = '011'
                if (word_arrays[i][j+1] == 'R4'):
                    output_arrays[i][j+1] = '100'
                if (word_arrays[i][j+1] == 'R5'):
                    output_arrays[i][j+1] = '101'
                if (word_arrays[i][j+1] == 'R6'):
                    output_arrays[i][j+1] = '110'
                if (word_arrays[i][j+1] == 'R7'):
                    output_arrays[i][j+1] = '111'
            output_arrays[i].append('000000')
    
    # print(output_arrays)

    # Open the file for writing
    with open('boot/output.txt', 'w') as f:
        # Iterate over each row in the array
        for row in output_arrays:
            # Convert each element in the row to a string and join them with spaces
            line = ''.join(str(elem) for elem in row)
            # Write the line to the file followed by a newline character
            f.write(f'b"{line}", ')


with open('boot/input.txt', 'r') as f:
    lines = f.readlines()

# Convert each line to an array of words
output_arrays = []
word_arrays = []
for line in lines:
    words = line.split()
    word_arrays.append(words)

# Print the word arrays
# print(word_arrays)
output_arrays = word_arrays
x = len(word_arrays)
print("Compiling ....")
boot()
print("Successfully Compiled (❁´◡`❁)")

import ast

with open('components/ir_memory.vhd', 'r') as file:
    code_lines = file.readlines()

with open('boot/output.txt', 'r') as file:
    instructions = file.readlines()

with open('components/ir_memory.vhd', 'w') as f:
        for line in code_lines:
            words = line.strip().split(" ")
            if len(words) > 3:
                if words[0] == 'signal' and words[1] == 'ir_mem' and  words[2] == ':' and words[3] == 'ir_array:=(':
                    line = f'signal ir_mem : ir_array:=( {instructions[0]} others => x"EFFF" );\n\t'
                    # print(line)
                    f.write(line)
                    continue
            f.write(line)

import os
import time
os.system('quartus_sh -t "c:/intelfpga_lite/20.1/quartus/common/tcl/internal/nativelink/qnativesim.tcl" --rtl_sim "IITB_RISC_23_Pipelined_Processor" "IITB_RISC_23_Pipelined_Processor" ')

time.sleep(15)

os.system('code simulation/output_values.txt')
os.system('code simulation/register_values.txt')