print ('{:=^40}'.format(' Termos de uma pa V2 '))
pt = int(input('primeiro termo: '))
rz = int(input('digite a razao da pa: '))
cont = 1 
while cont <= 10: 
    print ('{} ='.format(pt), end= ' ')
    pt += rz
    cont += 1
print('fim')