#sorteador de ordem
import random
nomes1 = str(input('digite o nome do alunos: '))
nomes2 = str(input('digite o nome do alunos: '))
nomes3 = str(input('digite o nome do alunos: '))
nomes4 = str(input('digite o nome do alunos: '))
alunos = [nomes1,nomes2,nomes3,nomes4]
random.shuffle(alunos)
print ('a ordem escolhida de apresentação é: {}'.format (alunos))alunos