#escrever um numero em metro e mostrar ele convertido para mm e cm 
n1 = float(input('digite um numero em metros: '))
cm = n1*100
mm = n1*1000
print ('{} para centimetros é {} e para milimetro é {}'.format (n1,cm,mm))