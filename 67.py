nm=0
while True: 
    nm = int(input('digite o numero para saber a taboada (numero negativo para): '))
    if nm < 0:
        break 
    for tab in range(1,11):
        print(f'{nm} x {tab} = {tab*nm}')
print(' ok, volte sempre')
