listaUF = list()

while True:
    sigla = input('Digite a UF: ').upper()[:2]

    if sigla == 'S': break
    
    if sigla not in listaUF:
        listaUF.append(sigla)
    
print(listaUF)