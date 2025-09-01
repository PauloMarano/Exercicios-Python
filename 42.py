#analisador de triangulos part 2 
r1 = float(input('digite o valor do primeiro segmento: '))
r2 = float(input('digite o valor do segundo segmento: '))
r3 = float(input('digite o valor do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('os segmentos a cima podem formar um triangulo' end='')
    if r1 == r2 == r3:
        print ('equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else: 
        print ('Isoceles')
else: 
    print('os seguimentos a cima nao podem formar um triangulo')
    