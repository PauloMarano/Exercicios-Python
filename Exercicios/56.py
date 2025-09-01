#
idd = 0 
mam = 0
contm = 0
contmp = 0
nmv = ''
for d in range (1, 5):
    print('------- {} Pessoa --------'.format(d))
    nm = str(input('Qual o Nome: '))
    ida = int(input('Qual Idade: '))
    sx = str(input('Qual Sexo[M/F]: ')).upper()
    idd += ida
    if sx == 'F':
        contm += 1
    if sx == 'F' and ida <= 19: 
        contmp += 1 
    if d == 1 and sx == 'M':
        nmv = nm
        mam = ida
    if sx == 'M' and ida < mam:
        nm = nmv
        ida = mam
md = idd/d
print('A media de idades é {:.0f}'.format(md))
print('O Homem mais velho tem {} Anos, e se chama {} '.format(ida, nm))
if contm == 0:
    print ('Não tem mulheres na sua lista')
else:
    print('Ao todo São {} Mulheres, e {} tem abaixo de 20 anos'.format(contm, contmp))