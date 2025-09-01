nome = str(input('digite o seu nome: ')).lower()
print ('seu nome tem {} letras a'.format(nome.count('a')))
print ('a primeira letra a apareceu na casa {}'.format(nome.find('a')+1))
print ('a ultima letra a apareceu na casa {}'.format (nome.rfind('a')-1))
