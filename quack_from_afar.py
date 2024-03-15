import math

def distance_ducks(filename,distance):
    if type(filename) != str:
        raise ValueError("parameter filename is not a string")
    if type(distance) != int and type(distance) != float:
        raise TypeError("parameter distance is not a numeric type")

    try:
        fl = open(filename, 'r')
    
    except FileNotFoundError:
        raise FileNotFoundError(filename)

    lines = fl.readlines()
    coordinates = []
    for x in lines:
        x,y = x.split(",")
        x = float(x)
        y = float(y)
        
        too_close = False
        for i in coordinates:
            if round(math.sqrt((x-i[0])**2 +(y-i[1])**2),4) > distance:
                continue
            else:
                too_close = True
                break
        if too_close == False:
            coordinates.append((x,y))


    fl.close()
    outfl = open("filtered-" + filename, 'w')
    output_ls = []
    for x in coordinates:
        output_ls.append(str(x[0]) + "," + str(x[1])+"\n")

    output_ls[-1] = output_ls[-1].rstrip('\n')
    outfl.writelines(output_ls)

    outfl.close()
    return


distance_ducks("duck_loc.txt",1.5)

