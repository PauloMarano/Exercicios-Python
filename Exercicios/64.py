nm = 0 
nmm = 0
cont = 0
while nm != 999: 
    nm = int(input('Digite um numero para somar[999 para]: '))
    nmm += nm
    cont += 1 
print ('voce somou {} numeros e todos somados dao {}'.format(cont - 1, nmm - 999))