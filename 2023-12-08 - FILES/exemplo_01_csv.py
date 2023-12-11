import os

# Obtendo o diretório corrente
strDiretorio = os.path.abspath(__file__)
strDiretorio = os.path.dirname(strDiretorio)

# --------------------------------------------------
# Abrindo o arquivo
strNomeArq = strDiretorio + '\\suap_componentes_curriculares.csv'
arqLeitura = open(strNomeArq, 'r', encoding='utf-8')

# Lendo a primeira linha - Cabecalho
strCabecalho = arqLeitura.readline()[:-1]

# Lendo o conteúdo do arquivo
lstComponentes = list()
while True:
    strLinha = arqLeitura.readline()[:-1]
    if not strLinha: break
    strLinha = strLinha.split(';')
    lstComponentes.append(strLinha)
    
# Fechando o arquivo
arqLeitura.close()

print(len(lstComponentes))

# --------------------------------------------------
# Extrair as disciplinas de graduação
filtro = lambda x:len(x)>2 and x[2].upper() == 'Graduação'.upper()
lstGraduacao = list(filter(filtro, lstComponentes))

print(len(lstGraduacao))

# --------------------------------------------------
# Salvar a lista filtrada em um novo arquivo
strNomeArq = strDiretorio + '\\suap_disciplinas_graduacao.csv'
arqEscrita = open(strNomeArq, 'w', encoding='utf-8')

arqEscrita.write(f'{strCabecalho}\n')

for disciplina in lstGraduacao:
    strLinha = ';'.join(disciplina)
    arqEscrita.write(f'{strLinha}\n')

arqEscrita.close()
