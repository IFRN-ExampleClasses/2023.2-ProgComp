texto = input('Digite algo: ')

print(f'{texto} = {len(texto)} caracteres')

posicao = 0
cripto  = ''
while posicao < len(texto):
    letra    = texto[posicao]
    v_asc    = ord(letra) + 5
    cripto  += chr(v_asc)
    posicao += 1

print(f'{texto} = {cripto}')
# Natal/RN = Sfyfq4WS