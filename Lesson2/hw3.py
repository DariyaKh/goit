
result = 0
i = 0
j = 0
while j == 0:
    i+=1
    if i%2 == 0 and i!=1:
        operation = input ('Insert operation: ')
        if operation.isdigit(): operation = input ('Insert operation once again: ')
        if operation == '=': j=1

    else:
        
            if i == 1: result = float(input('Insert operand: '))
            else: 
                try:
                  number = float(input('Insert operand: '))
                except ValueError: print ('Insert operand once again: ')
                    number = float(input)
                    if operation == '+': result = result + number
                    if operation == '-': result = result - number
                    if operation == '*': result = result * number
                    if operation == '/': result = result / number
          
print(result)     
    
