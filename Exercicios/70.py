#Exercício 70 – Estatísticas em produtos
print ('{:=^40}'.format(' COMPRAS NA LOJA '))
conti=nmpr=nms=''
cal=cal1=calt=prec=precc=0
while True: 
    nmpr = str(input('digite o nome do produto: '))
    prec = float(input('digite o valor do produto: '))
    conti = str(input('Tem mais algum produto(S/N): ')).upper()
    cal1 += 1
    if prec >= 1000: 
        cal += 1
    calt += prec
    if cal1 ==1 or prec < precc:
        precc = prec
        nms = nmpr
    if conti == 'N': 
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print (f'O total da compra foi R${calt:.2f}')
print(f'voce comprou {cal} produtos a cima de R$1000')
print(f'O produto mais barato foi o {nms} que custou {precc:.2f}')