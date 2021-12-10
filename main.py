from modulos.dado import escolha
from modulos.interface import *


def tabInicio():
    """Mostra o tabuleiro na tela"""
    line()
    for l in tab:
        print(' ' * 16, end='')
        for c in l:
            print(f'[ {c} ] ', end='')
        print()
    line()


def jogada(p=0):
    """Substitui o número escolhido pelo jogador
       pelo respectivo símbolo (X ou O)"""
    for i, l in enumerate(tab):
        for j, num in enumerate(l):
            if p > 0 and p == num:
                tab[i][j] = icon


def verificaVelha():
    # linhas
    for l in tab:
        if l[0] == l[1] == l[2]:
            return True
    # colunas
    coluna = list() # cria uma lista para cada coluna...
    for i in range(0, 3):
        for j in range(0, 3):
            coluna.append(tab[j][i])
        if coluna[0] == coluna[1] == coluna[2]: # e compara os valores no final
            return True
        coluna.clear()
    # cruzado
    if tab[0][0] == tab[1][1] == tab[2][2]:
        return True
    elif tab[0][2] == tab[1][1] == tab[2][0]:
        return True
    return False


# alimentação do tabuleiro inicial (variável composta global)
tab = list()
linha = list()
cont = 0
for i in range(1, 4):
    for j in range(1, 4):
        cont += 1
        linha.append(cont)
    tab.append(linha[:])
    linha.clear()

# dicionário para registrar cada jogada
indices = {1: tab[0][0],
           2: tab[0][1],
           3: tab[0][2],
           4: tab[1][0],
           5: tab[1][1],
           6: tab[1][2],
           7: tab[2][0],
           8: tab[2][1],
           9: tab[2][2]}

title('JOGO DA VELHA')
partida = 1
while partida <= 9:
    tabInicio()
    if partida % 2 == 0:
        icon = 'O'
    else:
        icon = 'X'
    jog = escolha('Sua jogada: ', 1, 9)
    while indices[jog] == 'X' or indices[jog] == 'O':
        print('\033[31mEssa jogada já foi feita!\033[m')
        jog = escolha('Tente novamente: ', 1, 9)
    indices[jog] = icon
    jogada(jog)
    if verificaVelha():
        break
    else:
        partida += 1
        continue
tabInicio()
if partida < 9:
    print(f'Jogador {icon} venceu!')
else:
    print('Deu Velha!')




