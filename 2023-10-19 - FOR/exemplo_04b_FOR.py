texto   = 'REDES DE COMPUTADORES'
texto_C = ''

for letra in texto:
    v_asc = ord(letra) + 10
    texto_C += chr(v_asc)

print(texto_C)