import pyodbc

server = 'svr-estudos-v2.database.windows.net'
database = 'adb-estudos-v2'
user = 'igor.morgado@blueshift.com.br'
drive = '{SQL Server}'
Authentication = 'ActiveDirectoryInteractive'
conexao = pyodbc.connect('DRIVE='+drive+';SERVER='+server+';AUTHENTICATION='+Authentication+';DATABASE='+database+';UID'+user)
cursor = conexao.cursor()
