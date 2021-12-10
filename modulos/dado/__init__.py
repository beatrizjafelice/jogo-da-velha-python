def validInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def validFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num


def escolha(msg, a, b, inteiro=True):
    """
    Delimita as opções de entrada do usuário em um intervalo numérico.
    :param msg: texto que antecede o input
    :param a: limite mínimo
    :param b: limite máximo
    :param inteiro: se aceita apenas números inteiros ou não
    :return: o número dentro do intervalo proposto (ou 0 em caso de exceção (KeyInterrupt))
    """
    while True:
        try:
            if inteiro:
                num = int(input(msg))
            else:
                num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            if a <= num <= b:
                break
            else:
                print('\033[31mOpção inválida!\033[m')
                continue
    return num






