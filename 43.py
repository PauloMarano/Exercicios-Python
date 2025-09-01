#calculador de imc 
ps = float(input('qual é o seu peso atual: '))
al = float(input('qual é sua altura: ')) 
fr = ps/(al*al)
if fr < 18.5: 
    print ('seu imc é de {:.0f}, pra sua altura com {} voce esta abaixo do peso'.format(fr, al))
elif fr >= 18.5 and fr <= 25: 
    print ('seu imc é de {:.0f}, para a sua altura voce esta em um peso ideal'.format(fr))
elif fr >= 25.1 and fr <= 30: 
    print ('o seu imc é de {:.0f}, voce ja esta sobrepeso, procure um medico!'.format(fr))
elif fr >= 30.1 and fr <= 40: 
    print ('seu imc é de {:.0f}, voce esta obeso, procure um medico!'.format(fr))
else: 
    print('seu imc é de {:.0f}, VOCE JA ESTA EM OBESIDADE MORBITA, PROCURE UM MEDICO COM URGENCIA PARA PREVINIR RISCOS'.format(fr))