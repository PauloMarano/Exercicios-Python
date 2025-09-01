import time 
import random
iten = ('Pedra', 'Papel', 'tesoura')
esp = random.randint(0, 2)
print ('{:=^50}'.format(''' Jogo Pedra, Papel Ou Tesoura '''))
time.sleep(1)
es = int(input(('''Escolha oque voce vai jogar
        [0] Pedra 
        [1] Papel 
        [2] Tesoura
        Escolha: ''')))
print ('pedra')
time.sleep(1)
print ('papel')
time.sleep(1)
print ('ou Tesouraaaaaaaaaa')
time.sleep(0.5)
print ('-='* 12)
print ('Voce jogou {} e o computador jogou {}'.format(iten[es], iten[esp]))
if esp == 0:
    if es == 0:
        print('Voces empataram!')
    elif es == 1: 
        print('VOCE GANHOU! PARABENS')
    elif es == 2:
        print('poxaa, voce perdeu')
    else: 
        print('jogada invalida')
elif esp == 1:
    if es == 0:
        print('poxaa, voce perdeu')
    elif es == 1: 
        print('Voces empataram!')
    elif es == 2: 
        print('VOCE GANHOU! PARABENS')
    else: 
        print('jogada invalida')
elif esp == 2: 
    if es == 0:
        print('VOCE GANHOU! PARABENS')
    elif es == 1: 
        print('poxaa, voce perdeu')
    elif es == 2: 
        print('Voces empataram!')
    else: 
        print('jogada invalida')
else: 
    print('Jogada Invalida! Tente novamente')