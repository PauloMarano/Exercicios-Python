#analisador de media 
n1 = float(input('primaira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
n4 = float(input('quarta nota: '))
media = (n1+n2+n3+n4)/4
if media >= 7: 
    print('parabens! Voce foi aprovado')
elif media <= 5: 
    print ('Voce esta reprovado')
else: 
    print ('voce esta de recuperação!')