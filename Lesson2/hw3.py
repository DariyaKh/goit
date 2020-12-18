a = input('Insert first number: ')
b = input('Insert second number: ')
c = input ('choose operation: 1 for "+", 2 for "-", 3 for "*", 4 for "/"  ')
c = int(c)
a = float(a)
b = float(b)

if c == 1:   result = (a + b)
else:
    if c == 2:  result = (a - b)
    else:
        if c == 3: result = (a*b)
        else: result = (a/b)
     
print(result)
