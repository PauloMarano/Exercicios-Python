#cadastro de uma pessoa
print ('{:=^40}'.format(' CADASTRO DE UMA PESSOA '))
es=sex='' 
ida=cont1=cont2=cont3=0
while es != 'N':
    ida = int(input('digite a idade da pessoa: ')) 
    sex = str(input('digite o sexo da pessoa(M/F): ')).upper()
    es = str(input('QUER CONTINUAR(S/N)? ').upper())
    if ida > 18: 
        cont1 += 1 
    if sex == 'M':
        cont2 += 1 
    if sex == 'F' and ida < 20: 
        cont3+=1
print(f'tem {cont1} pessoas maiores de 18 anos') 
print(f'foram cadastrados {cont2} Homens')
print(f'Foram cadastradas {cont3} mulheres com Menos de 20 anos')   