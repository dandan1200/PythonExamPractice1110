def word_sum(string):
    if type(string) != str:
        raise TypeError("Input must be a string.")
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'

    i = 0
    total = 0
    while i < len(string):
        added = False
        j = 0
        while j < len(alphabet):
            if string[i] == alphabet[j]:
                total += j+1
                added = True
                
                break
            j+=1

        if added == False:
            j = 0
            while j < len(numbers):
                if string[i] == numbers[j]:
                    total += j
                    added = True
                    break
                j+=1
        i+=1

    return total

print(word_sum('abc')) # 6
print(word_sum('ab*c!')) # 6
print(word_sum('123ab')) # 9
print(word_sum('!@#0')) # 0
print(word_sum('')) # 0
print(word_sum(123)) # TypeError
        
