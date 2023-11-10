listaUF = list()

while True:
    sigla = input('Digite a Sigla: ').upper()[:2]

    if sigla == 'S': break

    nome = input('Digite o Nome do Estado: ').upper()    
    
    listaUF.append([sigla, nome])
    
print(listaUF)