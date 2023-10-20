texto   = 'REDES DE COMPUTADORES'
texto_C = ''
pos     = 0

while pos < len(texto):
    letra = texto[pos]
    v_asc = ord(letra) + 10
    texto_C += chr(v_asc)
    pos += 1

print(texto_C)