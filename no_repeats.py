inputs = []
repeated = False
inputs.append(input("Give me an input: "))
j = 1
while repeated == False:
    j+=1 
    new_in = input("Give me an input: ")
    i = 0
    while i < len(inputs):
        if new_in == inputs[i]:
            print("\nInput number {} is not unique!".format(j))
            repeated = True
            break
        i+=1
    inputs.append(new_in)
    
    