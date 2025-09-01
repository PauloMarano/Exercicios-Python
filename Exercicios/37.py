#conversor de numero
nm = int(input('digite um numero inteiro: ')) 
print ('''escolha uma das bases para a conversão: 
       [1] para converter para Binario 
       [2] para converter para Octal
       [3] para converter para Hexadecimal''') 
res = str(input('digite pra oque voce quer converter: '))
if res == '1':
    print('seu numero {} para numero binario é {}'.format(nm, bin(nm)[2:]))
elif res == '2':    
    print('seu numero {} para um numero Octal é {}'.format(nm, oct(nm)[2:]))
elif res == '3':
    print('seu numero {} para um numero Hexadecimal é {}'.format(nm, hex(nm)[2:]))
else:
    print('Não existe essa opção')