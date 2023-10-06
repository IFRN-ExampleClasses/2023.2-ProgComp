texto = input('Digite algo: ')

print(f'{texto} = {len(texto)} caracteres')

posicao = 0
while posicao < len(texto):
    letra = texto[posicao]
    v_asc = ord(letra)
    print(f'{letra} = {v_asc} = {bin(v_asc)}')
    posicao += 1

'''
N = 78  = 0b1001110
a = 97  = 0b1100001
t = 116 = 0b1110100
a = 97  = 0b1100001
l = 108 = 0b1101100
/ = 47  = 0b101111
R = 82  = 0b1010010
N = 78  = 0b1001110
'''