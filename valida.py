from curses.ascii import isalpha
import re
from datetime import datetime

def valida_nome():
    while True:
        nome = input('Digite o primeiro nome: ')
        if nome.isalpha():
            if len(nome) <= 35:
                nome = nome.title()
                break
            else:
                print('Limite de caracteres exedido, digite ate 35 caracteres.')
        else:
            print('Digite apenas letras.')
    return nome


def valida_sobrenome():
    while True:
        sobrenome = input('Digite o sobrenome: ')
        if sobrenome.isalpha():
            if len(sobrenome) <= 35:
                sobrenome = sobrenome.title()
                break
            else:
                print('Limite de caracteres exedido, digite ate 35 caracteres.')
        else:
            print('Digite apenas letras.')
    return sobrenome


def valida_categoria():
    categorias = ['Comum', 'Estudante', 'Vale-Transporte', 'Idoso']
    indice = 1
    for item in categorias:
        print(f'       [ {indice} ] - {item}')
        indice += 1
    opcao_cat = False
    while opcao_cat == False:
        categoria = input('Digite a categoria do cartão: ')
        if categoria not in range(1, 5):
            print('Digite uma opção de categoria valida.')
        else:
            if categoria == '1':
                opcao_cat = True
                return 'Comum'
            elif categoria == '2':
                opcao_cat = True
                return 'Estudante'
            elif categoria == '3':
                opcao_cat = True
                return 'Vale-Transporte'
            elif categoria == '4':
                opcao_cat = True
                return 'Idoso'


def valida_data_emissao():
    while True:
        try:
            data_emissao = input('Digite a data de emissão no formato "AAAA-MM-DD"')
            datetime.strptime(data_emissao, '%Y-%m-%d').date()
        except ValueError:
            print('Digite uma data valida')

        else:
            break
    return data_emissao


def checa_ano():
    while True:
        try:
            ano = input('Digite o ano de fabricação do onibus [AAAA]: ')
            datetime.strptime(ano, '%Y').date()
        except ValueError:
            print('Ano invalido. Digite no formato [AAAA]')
        else:
            break
    return ano


def valida_nascimento():
    while True:
        try:
            data_nascimento = input('Digite a data de nascimento no formato "AAAA-MM-DD"')
            datetime.strptime(data_nascimento, '%Y-%m-%d').date()
        except ValueError:
            print('Digite uma data valida')

        else:
            break
    return data_nascimento

