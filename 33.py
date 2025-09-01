import time 
n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n3 = int(input('digite mais um numero: '))
menor = n1 #quem e menor 
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3 
#quen e  o maior
maior = n1
if n2>n1 and n2>n1:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print ('Analisando...')
time.sleep(2)
print ('o maior numero é {}, e o menor numero é o {}'.format(maior, menor))
