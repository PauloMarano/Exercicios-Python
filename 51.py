print ('{:=^40}'.format(' Termos de uma pa '))
pt = int(input('primeiro termo: '))
rz = int(input('digite a razao da pa: '))
dc = pt+ (10-1) * rz
for c in range(pt, dc + rz, rz):
    print ('{}'.format(c), end=' -> ')
print ('acabou')