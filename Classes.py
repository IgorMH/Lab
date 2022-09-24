#Classe do Usuario
class Usuario:
    def __init__(self, nome, sobrenome, email, bairro, nascimento):
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
        self._bairro = bairro
        self._nascimento = nascimento

#Getter Setter do nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

 #Getter Setter do sobrenome   
    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

#Getter Setter do email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

#Getter Setter do bairro
    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro

#Getter Setter da data de nascimento
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento




#Classe do Motorista
class Motorista:
    def __init__(self, numcnh, nome, sobrenome, nascimento):
        self._numcnh = numcnh
        self._nome = nome
        self._sobrenome = sobrenome
        self._nascimento = nascimento

#Getter Setter do numero da CNH
    @property
    def numcnh(self):
        return self._numcnh

    @numcnh.setter
    def numcnh(self, numcnh):
        self._numcnh = numcnh

#Getter Setter do nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

 #Getter Setter do sobrenome   
    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome


#Getter Setter da data de nascimento
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento




#Classe Cartão
class Cartao:
    def __init__(self, idUsuario, credito, categoria, emissao):
        self._idUsuario = idUsuario
        self._credito = credito
        self._categoria = categoria
        self._emissao = emissao

#Getter Setter idUsuario
    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, idUsuario):
        self._idUsuario = idUsuario

#Getter Setter do credito
    @property
    def credito(self):
        return self._credito

    @credito.setter
    def credito(self, credito):
        self._credito = credito

 #Getter Setter da categoria 
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

#Getter Setter da data de emissao
    @property
    def emissao(self):
        return self._emissao

    @emissao.setter
    def emissao(self, emissao):
        self._emissao = emissao




#Classe Onibus
class Onibus:
    def __init__(self, numplaca, numlinha, modelo, ano, idMotorista):
        self._numplaca = numplaca
        self._numlinha = numlinha
        self._modelo = modelo
        self._ano = ano
        self._idMotorista = idMotorista

#Getter Setter do numero da placa
    @property
    def numplaca(self):
        return self._numplaca

    @numplaca.setter
    def numplaca(self, numplaca):
        self._numplaca = numplaca

#Getter Setter do numero da linha
    @property
    def numlinha(self):
        return self._numlinha

    @numlinha.setter
    def numlinha(self, numlinha):
        self._numlinha = numlinha

 #Getter Setter do modelo 
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

#Getter Setter do ano do onibus
    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

#Getter Setter do id do motorista
    @property
    def idMotorista(self):
        return self._idMotorista

    @idMotorista.setter
    def idMotorista(self, idMotorista):
        self._idMotorista = idMotorista