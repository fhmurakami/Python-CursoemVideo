# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))

# print(13*'-')
# for i in range(11):
#     print('{:2} x {:2} = {:2}'.format(n, i, n*i))
# print(13*'-')

print('{}\n'
      '{} x  0 = {}\n{} x  1 = {}\n{} x  2 = {}\n{} x  3 = {}\n{} x  4 = {}\n{} x  5 = {}\n{} x  6 = {}\n{} x  7 = {}\n'
      '{} x  8 = {}\n{} x  9 = {}\n{} x 10 = {}\n{}'.format((12 * '-'), n, (n * 0), n, (n * 1), n, (n * 2), n, (n * 3),
                                                            n, (n * 4), n, (n * 5), n, (n * 6), n, (n * 7), n, (n * 8),
                                                            n, (n * 9), n, (n * 10), (12 * '-')))
