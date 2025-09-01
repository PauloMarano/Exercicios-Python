n=s=cont=0
while True: 
    n =int(input('digite o valor para somar(999) para: '))
    if n == 999: 
        break
    s+= n 
    cont +=1 
print(f'voce digitou {cont} numeros e a soma entre eles deu {s}')