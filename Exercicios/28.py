import random
import time
print ('jogo de adivinha')
start = str(input('podemos começar: '))
if start == 'sim':
    n = random.randint(0, 5)
    print ('ja escolhi o numero!')
    time.sleep(2)
    print ('escolha o numero de 0 a 5')
    nues = int(input('digite o numero que voce acha que eu escolhi: '))
    if nues == n:
        print (str('PARABENS VOCE ACERTOU O NUMERO'))
    else: 
        print (str('poxa voce errou, eu escolhi o numero {}'.format (n)))
else: 
    print ('ok')