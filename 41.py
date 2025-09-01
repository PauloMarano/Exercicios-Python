#natação categoria 
from datetime import date 
real = date.today().year
ida = (int(input('qual é o ano do seu nascimento: ')))
atual = real - ida
print ('o nadador tem {} anos.'.format(atual))
if atual <= 9: 
     print('voce esta na categoria mirim')
elif atual <= 14: 
    print('voce esta na categoria infatil') 
elif atual <= 19: 
    print('voce esta na categoria junior') 
elif atual == 20: 
    print('voce esta na categoria Senior')
else: 
    print('voce esta na categoria master') 