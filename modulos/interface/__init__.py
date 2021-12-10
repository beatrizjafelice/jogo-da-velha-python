def title(msg, tam=50):
    print('\033[1m', end='')
    line(x=tam)
    print(msg.center(tam))
    line(x=tam)
    print('\033[m', end='')


def line(char='-', x=50):
    print(f'{char}' * x)


def menu(lst, x=50):
    title('MENU PRINCIPAL', tam=x)
    c = 1
    for item in lst:
        print(f'\033[32m{c} - \033[34m{item}\033[m')
        c += 1
    line()


def encerra():
    print('\033[31mEncerrando...\033[m')
    print('<' * 18, end='')
    print(' Volte Sempre ', end='')
    print('>' * 18, end='')
