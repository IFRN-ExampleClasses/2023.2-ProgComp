nome           = input('Digite o seu nome: ')
ano_nascimento = input('Informe o ano do seu nascimento: ')

ano_atual      = 2023
ano_nascimento = int(ano_nascimento)
idade          = ano_atual - ano_nascimento

print(f'{nome} \nVocê nasceu em {ano_nascimento} \ne tem {idade} anos')