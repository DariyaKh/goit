result = 0
operation = ''
i = 0
j = 0
while j == 0:
    i+=1
    if i%2 == 0 and i!=1:
        operation = input ('Insert operation: ')
        if operation == '=': j=1
        if operation.isdigit():
          operation = print ('Insert operation once again: ')
          i-=1
    else:
        try: 
           number = float(input('Insert operand: '))
           if operation == '': result = number  
           if operation == '+': result += number
           if operation == '-': result -= number
           if operation == '*': result *= number
           if operation == '/': result/= number
        except ValueError:
            print ('Insert operand once again: ')
            i-=1

print(result)

