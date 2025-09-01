#radar 
vl = int(input('digite a velocidade do carro que passou pelo radar: '))
vlr = ((vl-80)*7)
if vl >= 81:
    print('voce passou na velocidade a cima do permitido')
    print('Voce foi multado em R${}'.format(vlr))
else: 
    print('Voce passou no limite de velocidade permitida')