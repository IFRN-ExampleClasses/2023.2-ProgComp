listaUF = list()

sigla = input('Digite a UF: ').upper()[:2]

while sigla != 'S':
    if sigla not in listaUF:
        listaUF.append(sigla)
    sigla = input('Digite a UF: ').upper()[:2]
    
print(listaUF)