# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases de conversão:')
option = int(
    input('[ 1 ] converter para BINÁRIO;\n[ 2 ] converter para OCTAL;\n[ 3 ] converter para HEXADECIMAL.\nOpção: '))

# if option == 1:
#     binario = bin(num)
#     print('O número {} em binário é {}'.format(num, binario[2:]))
# elif option == 2:
#     octal = oct(num)
#     print('O número {} em octal é {}'.format(num, octal[2:]))
# elif option == 3:
#     hexa = hex(num)
#     print('O número {} em hexadecimal é {}'.format(num, hexa[2:].upper()))
# else:
#     print('Opção inválida.')

if option == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:].upper()))
else:
    print('Opção inválida.')