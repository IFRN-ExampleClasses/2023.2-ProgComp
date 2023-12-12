import os, json, sys

# Obtendo o diretório corrente
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

# --------------------------------------------------
# Abrindo o arquivo de input
strNomeArq = strDiretorio + '\\suap_cursos_ofertados.json'

try:
    arqLeitura = open(strNomeArq, 'r', encoding='utf-8')
except:
    print(f'ERRO: {sys.exc_info()}')
else:
    # Lendo o conteúdo do arquivo
    strConteudo = arqLeitura.read()
    # Convertendo o conteúdo lido (string) em uma lista
    lstDados = json.loads(strConteudo)
    # Fechando o arquivo
    arqLeitura.close()