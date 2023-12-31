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

# Abrindo o arquivo no mode de escrita (w) e aceitando
# caracteres acentuados (utf-8)
arqCapitais = open('nordeste_1.txt', 'w', encoding='utf-8')

# Escrevendo os itens da lista no arquivo
intPopTotal = 0
for cidade in lstCapitais:
    arqCapitais.write(f'{cidade[1]}/{cidade[0]}:{cidade[2]}\n')
    intPopTotal += cidade[2]

# Escrevendo a população total da região NE
arqCapitais.write(f'\nPopulação Total NE: {intPopTotal}')

# Fechando o arquivo
arqCapitais.close()