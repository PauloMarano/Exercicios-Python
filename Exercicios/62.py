num = int(input('Digite o primeiro termo da P.A.: '))
razão = int(input('Digite a razão da P.A.: '))
c = 1
n = 11
while c < n:
    print(num, end=' ')
    num += razão
    c += 1
    if c == n:
        s = int(input('\nQuantos termos a mais deseja ver? Digite 0 para sair.. '))
        n += s