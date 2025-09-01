#numero primo 
n = int(input('digite um numero: ')) 
tot = 0 
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ') 
        tot += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ') 
print ('\n\33[mo numero {} foi divisivel por {} vezes'.format(n, tot))
if tot <= 2: 
    print('e por isso seu numero é primo') 
else: 
    print('e por isso seu numero não é primo') 
