# Declarando a lista
lstCapitais = [
                ['AL', 'Maceió', 1018948], 
                ['BA', 'Salvador', 2872347], 
                ['CE', 'Fortaleza', 2669342], 
                ['MA', 'São Luís', 1101884], 
                ['PB', 'João Pessoa', 809015], 
                ['PE', 'Recife', 1695727], 
                ['PI', 'Teresina', 868075], 
                ['RN', 'Natal', 890480], 
                ['SE', 'Aracaju', 657013]
            ]
# Ordenando as cidades pela população (decrescente)
lstOrdenada = sorted(lstCapitais, key=lambda c:c[2], reverse=True)

# Abrindo o arquivo no mode de escrita (w) e aceitando
# caracteres acentuados (utf-8)
arqCapitais = open('nordeste_2a.txt', 'w', encoding='utf-8')

# Escrevendo os itens da lista no arquivo
for cidade in lstCapitais:
    arqCapitais.write(f'{cidade[1]}/{cidade[0]}:{cidade[2]}\n')

# Escrevendo os dados do estado com a maior população
arqCapitais.write(f'\nCapital Mais Populosa: {lstOrdenada[0][1]}/{lstOrdenada[0][0]}\n')
arqCapitais.write(f'População: {lstOrdenada[0][2]}')

# Fechando o arquivo
arqCapitais.close()