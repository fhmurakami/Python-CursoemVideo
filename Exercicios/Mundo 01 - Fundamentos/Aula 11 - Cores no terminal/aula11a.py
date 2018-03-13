# Adicionando cor no terminal.
# Código ANSI Escape Sequence
# Cor -> \033['código'm
# 'código' -> style; text; background
# style -> negrito, sublinhado etc.
# 0: Sem estilo nenhum; 1: Negrito; 4: Sublinhado; 7: Inverte as configurações de letra e fundo.
# text -> cor do texto
# 3[0-7]: branco; vermelho; verde; amarelo; azul; roxo; ciano; cinza
# background -> cor do fundo
# 4[0-7]: branco; vermelho; verde; amarelo; azul; roxo; ciano; cinza
# Ex.: \033[0;33;44m

print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')
