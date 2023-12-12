import os, requests, sys

# --------------------------------------------------
# Requisitando os dados no servidor
strURL = 'https://viacep.com.br/ws/RN/Natal/Salgado/xml/'
retRequisicao = requests.get(strURL)

if retRequisicao.status_code != 200:
    print(f'ERRO: Erro ao obter os dados...\nCÓDIGO ERRO = {retRequisicao.status_code}')
    sys.exit()

try:
    lstCursos = retRequisicao.json()
except:
    print(f'ERRO: {sys.exc_info()}')
else:
    print(lstCursos)