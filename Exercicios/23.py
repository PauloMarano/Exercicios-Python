numero = int(input('digite um numero de 0 até 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10 
c = numero // 100 % 10
m = numero // 1000 % 10
print ('unidades: {}'.format(u))
print ('dezena: {}'.format(d))
print ('centena: {}'.format(c))
print ('milhar: {}'.format(m))