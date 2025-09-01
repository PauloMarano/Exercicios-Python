#maior e menor
maior = 0
menor = 0
for p in range(1, 6):
    ps = float(input('Qual o peso da {p}ª pessoa (em Kg)? '))
    if p == 1:
        maior = ps
        menor = ps
    else:
        if ps > maior:
            maior = ps
        if ps < menor:
            menor = ps
print('A pessoa mais pesada pesa {:.2f} Kg'.format(maior))
print('A pessoa mais leve pesa {:.2f} Kg'.format(menor)) 