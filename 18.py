from math import radians, tan, cos, sin
angulo = float(input('digite o valor do angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print ('o valor do angulo é {:.2f} tem o seno de {:.2f} \n o angulo de {:.2f} tem o cosseno {:.2f} ' \
        '\n o angulo de {:.2f} tem a tangente de {:.2f}'.format (angulo, seno, angulo, cosseno, angulo, tangente))