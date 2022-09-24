import insert
import visualizar
from Classes import *
from os import system
import colorama
colorama.init()

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[m'
BLUE = '\033[34m'
FUNDO = '\033[7;30;42m'

def limpa():
    system('cls')

while True:
    print(f'{FUNDO}+-------------------------------+{RESET}')
    print(f'{FUNDO}|    BANCO DE DADOS POCCOBUS    |{RESET}')
    print(f'{FUNDO}+-------------------------------+{RESET}')
    print(f'{FUNDO}| 1 - Cadastrar                 |{RESET}')
    print(f'{FUNDO}| 2 - Visualizar                |{RESET}')
    print(f'{FUNDO}| 3 - Sair do Sistema           |{RESET}')
    print(f'{FUNDO}+-------------------------------+{RESET}')
    opcao = input('Digite a opção: ')
    limpa()

    if opcao == '3':
        break

    if opcao == '1':
        while True:
            print(f'{FUNDO}+-------------------------------+{RESET}')
            print(f'{FUNDO}|       MENU DE CADASTRO        |{RESET}')
            print(f'{FUNDO}+-------------------------------+{RESET}')
            print(f'{FUNDO}| 1 - Cadastrar Usuario         |{RESET}')
            print(f'{FUNDO}| 2 - Cadastrar Cartão          |{RESET}')
            print(f'{FUNDO}| 3 - Cadastrar Motorista       |{RESET}')
            print(f'{FUNDO}| 4 - Cadastrar Onibus          |{RESET}')
            print(f'{FUNDO}| 5 - Voltar                    |{RESET}')
            print(f'{FUNDO}+-------------------------------+{RESET}')
            opc = input('Digite a opção: ')
            if opc == '5':
                break

            elif opc == '1':
                insert.insert_usuario()
                break

            elif opc == '2':
                insert.insert_cartao()
                break

            elif opc == '3':
                insert.insert_motorista()
                break

            elif opc == '4':
                insert.insert_onibus()
                break

    if opcao == '2':
        while True:
            print(f'{FUNDO}+-------------------------------+{RESET}')
            print(f'{FUNDO}|      MENU DE VISUALIZAR       |{RESET}')
            print(f'{FUNDO}+-------------------------------+{RESET}')
            print(f'{FUNDO}| 1 - Visualizar  Usuario       |{RESET}')
            print(f'{FUNDO}| 2 - Visualizar  Cartão        |{RESET}')
            print(f'{FUNDO}| 3 - Visualizar  Motorista     |{RESET}')
            print(f'{FUNDO}| 4 - Visualizar  Onibus        |{RESET}')
            print(f'{FUNDO}| 5 - Voltar                    |{RESET}')
            print(f'{FUNDO}+-------------------------------+{RESET}')
            opc = input('Digite a opção: ')
            if opc == '5':
                break

            elif opc == '1':
                visualizar.select_usuario()
                break

            elif opc == '2':
                visualizar.select_cartao()
                break

            elif opc == '3':
                visualizar.select_motorista()
                break

            elif opc == '4':
                visualizar.select_onibus()
                break

    if opcao == '3':
        break