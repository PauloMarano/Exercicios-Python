#valor a ser pago em um produto
print ('{:=^40}'.format('Loja do PPE'))
vl = float(input('digite o valor do produto: '))
frm = int(input('''escolha a baixo a forma de pagamento 
                [1] A Vista em Dinheiro ou Cheque 
                [2] A vista no cartão 
                [3] 2x no Cartão de credito
                [4] 3x ou mais no cartão com juros
                Escolha: '''))
if frm == 1: 
    print('sua compra no valor de R${:.2f} pagando a vista no dinheiro ou no cheque fica no valor de R${:.2f} ganhando 10% de desconto'.format(vl, (vl - (vl/10))))
elif frm == 2: 
    print('sua compra no valor de R${:.2f} pagando a vista no cartão fica no valor de R${:.2f} ganhando 5% de desconto '.format(vl, (vl-(vl * 0.05))))
elif frm == 3: 
    print ('sua compra vai sair no valor normal de R${:.2f}, vai ficar 2 parcelas de R${:.2f}'.format(vl, vl/2 ))
elif frm == 4: 
    pr= int(input('em quantas parcelas voce deseja pagar em até 10x ? '))
    print (' o valor da sua compra vai ficar em R${:.2f} total com o juros, parcelando em {} de R${:.2f} '.format((vl+vl*0.20), pr, ((vl + vl * 0.20) / pr )))
else: 
    print ('escolha invalida, tente novamente')