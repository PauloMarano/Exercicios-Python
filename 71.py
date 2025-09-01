#Exercício 71 – Simulador de Caixa Eletrônico
print ('{:=^40}'.format(' CAIXA ELETRONICO '))
cont1=cont2=cont3=cont4=0
sac = int(input('digite quanto voce quer sacar: '))

while True: 
    if sac >= 50: 
        sac -= 50
        cont1 += 1
    elif sac >= 20: 
        sac -=20
        cont2 +=1
    elif sac >= 10: 
        sac -= 10
        cont3 += 1
    else: 
        sac -=1 
        cont4 +=1
    if sac == 0:
        break
print(f'''foram sacadas:
      {cont1} NOTAS DE R$50
      {cont2} NOTAS DE R$20
      {cont3} NOTAS DE R$10
      {cont4} NOTAS DE R$1''')
print('='*15)