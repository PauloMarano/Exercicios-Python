#jogo Par ou impar]
import random
import time
nm=cont=pc=res=soma=0
es=''
print('JOGO PAR OU IMPAR')
time.sleep(1)
while True: 
    pc = random.randint(1,10) 
    nm = int(input('digite o valor: '))
    time.sleep(1)
    es= str(input('Voce Escolhe Par ou Impar(P/I): ')).upper()
    time.sleep(1)
    print(f'O computador escolheu {pc} e voce escolheu {nm}')
    soma = nm + pc
    res = 'P' if soma %2==0 else 'I'
    time.sleep(1) 
    if soma %2 == 0: 
            print (f'A Soma deu {soma} então deu Par')
    else: 
            print(f'A soma deu {soma} então deu impar')
    if res == es: 
            cont +=1
            print(f'VOCE GANHOU, vamos de novo......')
    else:
            print(f'Voce Perdeu, Voce Ganhou {cont} Vezes')
            break
print('Finalizado')