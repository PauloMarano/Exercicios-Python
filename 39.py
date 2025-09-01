from datetime import date 
ida = int (input('digite o ano em que voce nasceu: '))
ano = int (date.today().year)
real = ano - ida
sexo =  (input('Voce é Homem ou mulher ? ')).strip().lower()
if sexo == 'mulher': 
    print('voce não é obrigada a fazer o alistamento militar')
    es = int(input('mas se voce quiser participar digite 1 se não 2: '))
    if es == 1:
        if real <= 17: 
            print ('voce ainda não possui idade para se alista, ainda falta {} anos'.format(real - 18))
        elif real - ida == 18:
            print('voce esta na idade certa para se alistar')
        else:
            print ('ja passou do prazo de voce se alistar, voce esta atrasado a {} anos'.format(real - 18)) 
    else: 
        print('ok, muito obrigado') 
elif sexo == 'homem':
    if real <= 17:
        print ('voce ainda não possui idade para se alista, ainda falta {} anos'.format(real - 18))
    elif real - ida == 18:  
        print('voce esta na idade certa para se alistar')
    else:
        print ('ja passou do prazo de voce se alistar, voce esta atrasado a {} anos'.format(real - 18)) 
else: 
    print('ok, muito obrigado')