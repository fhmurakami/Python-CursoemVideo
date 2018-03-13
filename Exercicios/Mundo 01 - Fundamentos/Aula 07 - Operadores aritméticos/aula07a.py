# nome = input('Qual é o seu nome: ')
# # {:20} reserva um espaço de 20 caracteres.
# # ^ - imprime centralizado.
# # < - alinha à esquerda.
# # > - alinha à direita.
# # = - preenche os espaços com o símbolo '='.
# print('Prazer em te conhecer {:=^20}'.format(nome))

n1 = 10
n2 = 3

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# {:.3f} -> 3 casas após a vírgula. 10/3 = 3.333
# {:.3} -> imprime o número com 3 algarismos. 10/3 = 3.33
# end = ' ', finaliza a linha com um espaço, sem quebra de linha.
# \n -> quebra a linha.
print('A soma é {}, o produto é {} \ne a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))
