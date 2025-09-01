#valor passagem onibus por km 
n = float(input('quantos kms até o local que voce quer chegar? '))
if n >= 201:
    print ('sua passagem vai ficar no valor de R${}'.format(n*0.45))
else: 
    print ('sua passagem vai ficar no valor de R${}'.format(n*0.50))