texto = input('Digite algo: ')

print(f'{texto} = {len(texto)} caracteres')

posicao = 0
while posicao < len(texto):
    letra = texto[posicao]
    v_asc = ord(letra) + 5
    print(f'{letra} = {chr(v_asc)}')
    posicao += 1

