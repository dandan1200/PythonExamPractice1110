def count_siblings(filename,name):
    if type(filename) != str:
        raise ValueError("parameter filename is not a string")
    if type(name) != str:
        raise ValueError("parameter name is not a string")
    try:

        f = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError(filename)
    tree = f.readlines()
    name_in = False
    for x in tree:
        if name in x:
            name_in = True
            sib_tar = x.split(",")
            sib_tar_father = sib_tar[3]
            sib_tar_mother = sib_tar[4].rstrip("\n")
            break
    if name_in == False:
        raise ValueError("name parameter not found in file")
    else:
        siblings = []
        step_siblings = []
        for x in tree:
            i = x.split(",")
            i[4] = i[4].rstrip("\n")
            if i[0] == name:
                continue
            if i[3] == sib_tar_father and i[4] == sib_tar_mother:
                siblings.append(i[0])
            elif i[3] == sib_tar_father or i[4] == sib_tar_mother:
                step_siblings.append(i[0]+"(step)")
    
    total_sib = siblings + step_siblings
    siblings_print_string = ''
    for x in total_sib[:-1]:
        siblings_print_string += (x + ", ")
    
    siblings_print_string = siblings_print_string.rstrip(", ")

    ret_string = name + " has {} siblings: {} and {}.".format(len(siblings) + len(step_siblings), siblings_print_string ,total_sib[-1])
    return ret_string


print(count_siblings("siblings_fl.txt","Brian"))