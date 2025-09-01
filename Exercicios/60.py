#fatorial de um numero
n = int(input('digite o falor que voce queira fatorar: '))
c = n
f = 1
print (' o fatorial de {} é: '.format(n))
while c > 0: 
    print(c, end = '')
    print(' x ' if c > 1 else ' = ',end= '')
    f *= c
    c -= 1
print (f)