#idade menor e  maior de idade= 
from datetime import date
atual = date.today().year
coma = 0
come = 0
for c in range(1,8):
    n = int(input('em que ano a {} pessoa nasceu? '.format(c)))
    at = atual - n
    if at <= 18:
        coma += 1 
    else:
        come += 1
print('tem {} pessoas menores de idade e {} pessoas maiores de idade'.format(come, coma))