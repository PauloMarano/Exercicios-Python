fr = str(input('digite uma frase: ')).upper().strip() 
pl = fr.split() 
junto = ''.join(fr)
inverse = junto[::-1]
print('o inverso de {} é {}'.format(junto, inverse))
if inverse == junto: 
    print ('temos um palindromo')
else: 
    print('não é um palindromo') 
    