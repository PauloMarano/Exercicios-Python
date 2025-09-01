#menu de operações
import time 
es = 0
nm = 0
while es != 5:
    print('BEM VINDO AO MENU DE OPERÇÕES') 
    time.sleep(1)
    n = int(input('Digite o 1 Valor: '))
    n_2 = int(input('Digite o 2 Valor: '))
    time.sleep(2)
    print('''ESCOLHA UMA OPÇÃO
          [1] SOMAR NUMEROS 
          [2] MULTIPLICAR NUMEROS 
          [3] QUAL MAIOR 
          [4] NOVOS NUMEROS 
          [5] SAIR DO MENU''')
    es = int(input('escolha uma opção: '))
    if es == 1: 
        print('A Soma desses numeros fica {}'.format(n+n_2))
        time.sleep(2)
    elif es == 2: 
        print('A Multiplicação desses numeros da {}'.format(n*n_2))
        time.sleep(2)
    elif es == 3: 
        if n > n_2:
            nm = n 
        else: 
            nm = n_2
        print('O Numero maior é {}'.format(nm))
        time.sleep(2)
    elif es == 4: 
        print('ok, altere os numeros')
        time.sleep(2)
    elif es == 5: 
        print('Ta ok, Volte sempre') 
        time.sleep(2)
    else: 
        print('Opção incorreta, tente novamente')
        time.sleep(2)
