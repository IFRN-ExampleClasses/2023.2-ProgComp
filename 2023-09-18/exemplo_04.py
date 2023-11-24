'''
    FAZER UM PROGRAMA QUE SOLICITE O VALOR DA BASE MAIOR, 
    DA BASE MENOR E DA ALTURA DE UM TRAPÉZIO 
    E CALCULE A ÁREA DO TRAPÉZIO
'''

bMaior = float(input('Informe o valor da Base Maior: '))
bMenor = float(input('Informe o valor da Base Menor: '))
altura = float(input('Informe o valor da altura: '))

if bMaior>0 and bMenor>0 and altura>0:
    area = (bMaior + bMenor) * altura / 2
    print(f'O Trapézio possui área de {area:.2f}')
else:
    print('Valores Informados Inválidos...')