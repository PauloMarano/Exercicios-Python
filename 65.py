#menor/maior e media com while
maior = 0 
menor = 0
nm = 0
nmm = 0 
cont = 0
r = ''
while r != 'N': 
    nm = int(input('Digite o Valor: '))
    cont += 1 
    nmm += nm
    if cont == 1: 
        maior = menor = nm
    if nm > maior: 
        maior = nm
    if nm < menor:  
        menor = nm
    r = str(input('Deseja Continuar(S/N): ')).upper()
print('A media de todos os numeros é {:.2f}, sendo o maior {} e o menor {}'.format((nmm/cont), maior, menor))