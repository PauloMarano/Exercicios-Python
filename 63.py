print('---' * 10)
print('Sequência de Fibonacci')
print('---' * 10)
qtd_termo = int(input('Quantos termos você quer mostrar? '))
contador = 0
antecessor = 0
sucessor = 1
print('~~~~' * 10)
while contador < qtd_termo:
    print(f'{antecessor} ', end=' -> ')
    sucessor += antecessor
    antecessor = sucessor - antecessor
    contador += 1
print('FIM')
print('~~~~' * 10)