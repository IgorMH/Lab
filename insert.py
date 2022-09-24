from datetime import datetime
import validacoes
from Classes import *
import conexao
from os import system

def limpa():
    system('cls')

def insert_usuario():
    limpa()
    print('CADASTRO DE USUARIOS')
    nome = input('Digite o nome do usuario: ').strip().lower().capitalize()
    sobrenome = input('Digite o sobrenome do usuario: ').strip().lower().capitalize()
    while True:
        email = input('Digite o email do usuario: ').strip().lower().capitalize()
        if validacoes.validar_email(email) == True:
            break
    bairro = input('Digite o bairro do usuario: ').strip().lower().capitalize()
    while True:
        nascimento = input('Digite a data de nascimento no formato AAA-MM-DD: ')
        if validacoes.validar_data(nascimento) == True:
            break

    usuario = Usuario(nome, sobrenome, email, bairro, nascimento)

    query = f'''INSERT INTO [GRP-09/22].[igor_morgado_usuario](nome, sobrenome, email, bairro, nascimento)
                VALUES('{usuario._nome}', '{usuario._sobrenome}', '{usuario._email}', '{usuario._bairro}', '{usuario._nascimento}')
                '''
    conexao.cursor.execute(query)
    conexao.cursor.commit
    print('Usuario cadastrado com sucesso!')

def insert_cartao():
    limpa()
    print('CADASTRO DE CARTÕES')
    while True:
        idUsuario = int(input('Digite o id do usuario que deseja cadastrar o cartão ou [ 0 ] para cancelar: '))
        if idUsuario == 0:
            break
        else:
            query = f'SELECT * FROM [GRP-09/22].[igor_morgado_usuario] WHERE ID_USUARIO = {idUsuario}'
            conexao.cursor.execute(query)

            rows = conexao.cursor.fetchall()
            if rows == []:
                print(f'O usuario com id: {idUsuario} não existe. digite outro id.')
                break
            print(rows)

        credito = input('Digite a quantidade de creditos iniciais: ')
        categoria  = input('Digite a categoria do cartão:\n[ 1 ] - Comum\n[ 2 ] - Estudante\n[ 3 ] - Vale-Trasnporte\n[ 4 ] - Idoso\n')
        if categoria == '1':
            categoria = 'Comum'
        if categoria == '2':
            categoria = 'Estudante'
        if categoria == '3':
            categoria = 'Vale-Transporte'
        if categoria == '4':
            categoria = 'Idoso'
        else:
            print('Categoria invalide. Digite novamente.')
            break
        while True:
            emissao = input('Digite a data de emissao no formato AAA-MM-DD: ')
            if validacoes.validar_data(emissao) == True:
                break

        cartao = Cartao(idUsuario, credito, categoria, emissao)

        query = f'''INSERT INTO [GRP-09/22].[igor_morgado_cartao](idUsuario, credito, categoria, emissao)
                    VALUES ('{cartao._idUsuario}', '{cartao._credito}', '{cartao._categoria}', '{cartao._emissao}')
                    '''
        conexao.cursor.execute(query)
        conexao.cursor.commit
        print('Cartão cadastrado com sucesso!')


def insert_motorista():
    limpa()
    print('CADASTRO DE MOTORISTAS')
    numcnh = input('Digite o numero da CNH do motorista: ')
    nome = input('Digite o nome do motorista: ').strip().lower().capitalize()
    sobrenome = input('Digite o sobrenome do motorista: ').strip().lower().capitalize()
    while True:
        nascimento = input('Digite a data de nascimento no formato AAA-MM-DD: ')
        if validacoes.validar_data(nascimento) == True:
            break

    motorista = Motorista(numcnh, nome, sobrenome, nascimento)

    query = f'''INSERT INTO [GRP-09/22].[igor_morgado_motorista](numcnh, nome, sobrenome, nascimento)
                VALUES('{motorista._numcnh}', '{motorista._nome}', '{motorista._sobrenome}', '{motorista._nascimento}')
                '''
    conexao.cursor.execute(query)
    conexao.cursor.commit
    print('Motorista cadastrado com sucesso!')



def insert_onibus():
    limpa()
    print('CADASTRO DE ONIBUS')
    while True:
        idMotorista = int(input('Digite o id do motorista que deseja cadastrar no onibus ou [ 0 ] para cancelar: '))
        if idMotorista == 0:
            break
        else:
            query = f'SELECT * FROM [GRP-09/22].[igor_morgado_motorista] WHERE ID_MOTORISTA = {idMotorista}'
            conexao.cursor.execute(query)

            rows = conexao.cursor.fetchall()
            if rows == []:
                print(f'O usuario com id: {idMotorista} não existe. digite outro id.')
                break
            print(rows)

        numplaca = input('Digite o numero da placa: ')
        numlinha = input('Digite o numero da linha: ')
        modelo = input('Digite o modelo do onibus: ')
        ano = input('Digite o ano de fabricação do onibus: ')

        onibus = Onibus(numplaca, numlinha, modelo, ano, idMotorista)

        query = f'''INSERT INTO [GRP-09/22].[igor_morgado_onibus](numplaca, numlinha, modelo, ano, idMotorista)
                    VALUES ('{onibus._numplaca}', '{onibus._numlinha}', '{onibus._modelo}', '{onibus._ano}', '{onibus._idMotorista}')
                    '''
        conexao.cursor.execute(query)
        conexao.cursor.commit
        print('Onibus cadastrado com sucesso!')