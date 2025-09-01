#compardor de numeros 
import time 
nm1= int(input('digite um numero: '))
nm2= int(input('digite outro numero: '))
print ('vamos comparalos.......') 
time.sleep(2)
if nm1 > nm2: 
    print('o {} seu primeiro mumero é maior que o numero {}'.format(nm1, nm2))
elif nm2 > nm1: 
    print ('o {} seu segundo numero é maior que o numero {} seu primeiro'.format(nm2, nm1))
else: 
    print ('os dois numeros são iguais') 