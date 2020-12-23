a = input('Insert first number: ')
b = input('Insert second number: ')
c = input ('choose operation: "+" / "-" / "*" / "/": ')
#c = int(c)
a = float(a)
b = float(b)
while True:
    if c == '+':   result = (a + b)
    else:
        if c == '-':  result = (a - b)
        else:
            if c == '*': result = (a*b)
            else: result = (a/b)
    d = input()
    if d == '=':
       print(result)
       exit
       
