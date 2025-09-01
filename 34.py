#aumento de salario
sl = float(input('digite o valor do salario: '))
if sl >= 1251: 
    print ('voce vai ter um aumento de 10% no seu salario')
    print('seu salario vai ter um aumento de R${:.1f} e vai ficar no total de R${:.1f}'.format(sl*0.10, sl*0.10 + sl))
else: 
    print('voce vai ter um aumento de 15% no seu salario')
    print('seu sa;ario vai ter um aumento de R${:.1f} e vai ficar no total em R${:.1f}'.format(sl *0.15, sl*0.15 + sl))