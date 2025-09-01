#calculador de aprovação de emprestimo para casa
vlcs = float(input('qual é o valor da casa que voce deseja comprar: '))
sl = float(input('qual é o valor do seu salario mensal atual: '))
anos = int(input('em quantos anos voce deseja parcelar este emprestimo: '))
vlcss = (vlcs/anos)/12
if vlcss <= (sl/10)*3: 
    print('o seu emprestimo pode ser aprovado')
    print('sua parcela vai ficar no valor de {:.2f} mensal'.format(vlcss))
else: 
    print ('infelizmente o seu emprestimo não foi aprovado')