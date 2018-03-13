# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra;
# B) Quantos produtos custam MAIS de R$1000;
# C) Qual é o nome do produto mais barato.

# total das compras = contador mais de R$1000 = valor mais barato = contador de produtos
total = c_1000 = menor = c = 0

# Imprime o nome da loja com uma linha tracejada acima e abaixo
print('-' * 40)
print(f'{"HIPERMERCADO MURAKAMI":^40}')
print('-' * 40)

# Início do programa
while True:
    # Reinicia a variável preço com 0 e a variável opção com um espaço.
    price = 0
    opt = ' '

    # Recebe o nome do produto
    name = input('Digite o nome do produto: ')
    # Só aceita o preço se for um valor positivo:
    while price <= 0:
        price = float(input('Digite o valor do produto: R$'))
    # Se for o primeiro produto da lista ou se o preço for menor que o mais barato, atribui o preço como mais barato
    if c == 0 or price < menor:
        menor = price
        barato = name

    # Incrementa o contador de produtos
    c += 1
    # Soma o valor do produto ao total da compra
    total += price
    # Verifica se o valor é maior que R$1000
    if price > 1000:
        # Incrementa o contador de produtos com valor acima de R$1000
        c_1000 += 1
    # Testa se a opção é 'S' ou 'N':
    while opt not in 'SN':
        opt = input('Deseja continuar? [S/N] ').upper().replace(' ', '')
    # Se a opção for 'N', termina o programa.
    if opt == 'N':
        print(f'\n{" COMPRA FINALIZADA ":-^40}')
        break
print(f'''Total de produtos da compra: {c}
Valor total da compra: R${total:.2f}
Total de produtos acima de R$1000.00: {c_1000}
Produto mais barato: {barato}''')
