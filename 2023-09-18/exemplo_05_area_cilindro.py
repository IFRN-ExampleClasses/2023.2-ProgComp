'''
    FAZER UM PROGRAMA QUE SOLICITE O VALOR DO RAIO DA 
    DA BASE E A ALTURA DE CILINDRO E CALCULE A ÁREA DO 
    CILINDRO
'''

raio   = float(input('Informe o valor do Raio: '))
altura = float(input('Informe o valor da Altura: '))

if raio>0 and altura>0 :
    pi   = 3.1416
    area = 2 * pi * raio * (raio + altura)
    print(f'O cilindro de raio {raio} e altura {altura} tem área de {area:.4f}')
else:
    print('Dados Inválidos...')