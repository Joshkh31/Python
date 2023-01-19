
# Command above every line to ensure that code is easily understandable
#Continuous loop untill [ctrl][c]
while True:
    #Read the first byte if no byte loop
    byte1 = Serial_Port1.read(1)
    if len(byte1) <1:
        break
    if byte2 == b"\62":
        #Get the BBX class
        byte3 = Serial_Port1.read(1)
        