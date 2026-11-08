import math
def function(a):
    chips = [100,50,25,10,5,1]
    numChips = 0
    i = 0
    while a > 0:
        if a >= chips[i]:
            a = a - chips[i]
            numChips = numChips + 1
        else:
            i = i + 1
        
    print(numChips)
    
function(226)