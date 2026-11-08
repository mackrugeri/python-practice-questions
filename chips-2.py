import math
def function(a):
    chips = [100,50,25,10,5,1]
    numChips = 0
    for chip in chips:
        num = math.floor(a/chip)
        a = a - (chip*num)
        numChips +=num
        
    print(numChips)
    
function(226)