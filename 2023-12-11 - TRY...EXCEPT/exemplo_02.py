import os, json, sys

# Obtendo o diretório corrente
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

# --------------------------------------------------
# Abrindo o arquivo de input
#strNomeArq = strDiretorio + '\\suap_cursos_ofertados.json'
strNomeArq = strDiretorio + '\\brave_wallpaper.png'

try:
    arqLeitura = open(strNomeArq, 'r', encoding='utf-8')
except FileNotFoundError:
    print('\nERRO....: Arquivo não encontrado...')
    print(f'ARQUIVO..: {strNomeArq}')
    sys.exit()
except:
    print(f'ERRO: {sys.exc_info()[0]}')
    sys.exit()
else:
    try:
        # Lendo o conteúdo do arquivo
        strConteudo = arqLeitura.read()
    except:
        print(f'ERRO: {sys.exc_info()[0]}')
        sys.exit()
    # Fechando o arquivo
    arqLeitura.close()

# Convertendo o conteúdo lido (string) em uma lista
lstDados = json.loads(strConteudo)
print(len(lstDados))
