s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 
        s = s + c
print('a soma de todos os numeros divisives por 3 é {} e foram somados {} numeros'.format(s, cont))