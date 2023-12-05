# Declarando a lista
capitais = ['Maceió', 'Salvador', 'Fortaleza', 'São Luís', 'João Pessoa', 
            'Recife', 'Teresina', 'Natal', 'Aracaju']

# Abrindo o arquivo no mode de escrita (w) e aceitando
# caracteres acentuados (utf-8)
arqCapitais = open('nordeste_1.txt', 'w', encoding='utf-8')

# Escrevendo os itens da lista no arquivo
for c in capitais:
    arqCapitais.write(f'{c}\n')

# Fechando o arquivo
arqCapitais.close()