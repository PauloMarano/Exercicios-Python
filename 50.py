#sei numeros e somar só os pares 
s = 0 
co = 0
for c in range(1,7): 
    n = int(input('digite o {} valor: '.format(c)))
    if n %2 == 0:
        s += n
        co += 1
print ('''voce colocou {} numeros pares 
       o valor de todos os numeros pares é {}'''.format(co, s))
