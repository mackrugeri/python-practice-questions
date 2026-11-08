
def barket_balance(string):
    barket_set = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    stack = []
    for i in string:
        if i in '[{(':
          stack.append(i)  

        elif i in ')}]' and  (not stack or barket_set[i] != stack.pop()):
           return False
    return True
            

print(barket_balance('[]})]'))