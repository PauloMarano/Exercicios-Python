#ano bissexto ?
ano = int(input('digite o ano que voce esta: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('o ano de {} é um ano bissexto'.format(ano))
else:
    print('ele não é um ano bissexto')