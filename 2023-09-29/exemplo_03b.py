nome = input('Digite um nome: ')

p_final = 1

while p_final <= len(nome):
    print(nome[0:p_final])
    p_final += 1

# variavel[p_inicial:p_final]
# nome[0:1] -> C
# nome[0:2] -> Ch
# nome[0:3] -> Cha
'''
C
Ch
Cha
Char
...
'''