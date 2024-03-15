def longest_consecutive_sequence(ls):
    if type(ls) != list:
        return -1
    
    i = 0
    longest = 0
    long_in = -1
    
    while i < len(ls):
        j = i
        while j < len(ls)-1:
            if type(ls[j]) == int:
                if ls[j] + 1 == ls[j+1]:
                    j+=1
                    if j-i > longest:
                        longest = j-i
                        long_in = i
                    continue
                else:
                    if j-i > longest:
                        longest = j-i
                        long_in = i
                        
                    break
                
            else:
                break
        i=j+1
    return long_in

print(longest_consecutive_sequence([7, 1, 2, 3, 6, 9, 2, 5, 6, 7])) # 1
print(longest_consecutive_sequence([8, 4, 3, 1, 5, 6])) # 4
print(longest_consecutive_sequence([9, 10, 11, 13, 14, 15, 16])) # 3
print(longest_consecutive_sequence([2, "a", 3, 4])) # 2
print(longest_consecutive_sequence([1, 1, 1, 1, 1])) # -1
print(longest_consecutive_sequence([0])) # -1