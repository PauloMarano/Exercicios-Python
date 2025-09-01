import random
nomes1 = str(input('digite o nome do alunos: '))
nomes2 = str(input('digite o nome do alunos: '))
nomes3 = str(input('digite o nome do alunos: '))
nomes4 = str(input('digite o nome do alunos: '))

lista = [nomes1,nomes2,nomes3,nomes4]
escolhido = random.choice (lista)

print ('o aluno escolhido foi o {}'.format(escolhido))