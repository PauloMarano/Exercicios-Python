#calculadora esperta 
n = int(input('digite o numero que voce quer ver a taboada: ')) 
print(''' a sua taboada de {} abaixo:'''.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n,c,((c*n))))