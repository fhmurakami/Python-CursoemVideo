# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

# Recebe o nome da cidade e elimina espaços antes e após as palavras:
cid = input('Digite o nome da cidade: ').strip()

# Transforma as palavras em letra maiúscula e  divide os nomes da cidade em uma lista:
lista_nome = cid.upper().split()

# Imprime se o primeiro nome começa com a palavra SANTO:
print('A cidade começa com SANTO? {}'.format('SANTO' in lista_nome[0]))
# print('A cidade começa com SANTO? {}'.format(lista_nome[0] == 'SANTO')) # Não mostra Santos como True.

# Resolução do professor:
# print('A cidade começa com SANTO? {}'.format(cid[:5].upper() == 'SANTO'))