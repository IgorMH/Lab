import conexao

def select_usuario():
    query = f'SELECT * FROM [GRP-09/22].[igor_morgado_usuario]'
    conexao.cursor.execute(query)

    rows = conexao.cursor.fetchall()
    for row in rows:
        print(f'{row}')


def select_cartao():
    query = f'SELECT * FROM [GRP-09/22].[igor_morgado_cartao]'
    conexao.cursor.execute(query)

    rows = conexao.cursor.fetchall()
    for row in rows:
        print(f'{row}')


def select_motorista():
    query = f'SELECT * FROM [GRP-09/22].[igor_morgado_motorista]'
    conexao.cursor.execute(query)

    rows = conexao.cursor.fetchall()
    for row in rows:
        print(f'{row}')


def select_onibus():
    query = f'SELECT * FROM [GRP-09/22].[igor_morgado_onibus]'
    conexao.cursor.execute(query)

    rows = conexao.cursor.fetchall()
    for row in rows:
        print(f'{row}')