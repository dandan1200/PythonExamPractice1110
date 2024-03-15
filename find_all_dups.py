def find_duplicates(ls):
    if type(ls) == list:
        i = 0
        while i < len(ls):
            if ls[i] <= len(ls) and ls[i] >= 1:
                i+=1
            else:
                return -1

        i = 0
        while i < len(ls):
            j = 0
            while j < len(ls):
                if ls[i] == ls[j] and i != j:
                    return ls[i]
                j+=1            
            i+=1
                
        return 0
    else:
        return -1

print(find_duplicates([1, 2, 3, 2])) # 2
print(find_duplicates([1, 1, 2, 2])) # 1
print(find_duplicates([4, 3, 1, 2])) # 0
print(find_duplicates([1, 2, 2, 0])) # -1
print(find_duplicates([])) # 0
print(find_duplicates((1, 2, 3))) #-1