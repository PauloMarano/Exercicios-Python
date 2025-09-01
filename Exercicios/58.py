#JOOGO DO ADVINHA V2
import time
import random
cont = 0
print('JOGO DE ADVINHA V2')
start = str(input('VOCE DESEJA INICIAR? (sim/nao): ')).lower()
if start == 'sim':
    print('pensando em um numero de 1 a 10........') 
    time.sleep(2)
    print('ja pensei em um numero!')
    time.sleep(1)
    n = random.randint(1,10) 
    es = ''
    while es != n:
        es= int(input('Adivinhe o Numero que eu escolhi: '))
        cont += 1
        if es > n: 
            print ('menos..... Tente novamente')
            time.sleep(1)
        elif es < n: 
            print('mais........Tente Novamente')
            time.sleep(1)
        if es == n and cont == 1:
            print('PARABENS VOCE ACERTOU DE PRIMEIRA!!!!')
        if es == n: 
            print('PARABENS VOCE ACERTOU!!! FORAM {} TENTATIVAS ATÉ VOCE CHEGAR NO RESULTADO'.format(cont)) 
else: 
    print('quando quiser é só iniciar')
