'''
    FAZER UM PROGRAMA QUE SOLICITE O VALOR DO RAIO DA 
    DA BASE E A ALTURA CONE E CALCULE A ÁREA DO 
    CONE
'''

raio   = float(input('Informe o valor do Raio: '))
altura = float(input('Informe o valor da Altura: '))

if raio>0 and altura>0 :
    pi       = 3.1416
    geratriz = (raio**2 + altura**2)**(1/2)
    area     = (pi * raio ** 2) * (pi * raio * geratriz)
    print(f'O cone de raio {raio} e altura {altura} tem área de {area:.4f}')
else:
    print('Dados Inválidos...')