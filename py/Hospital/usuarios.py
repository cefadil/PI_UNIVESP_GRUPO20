import random
import datetime
from db import DB 
class Usuarios:
    
    def __init__(self):
        self.id = 0
        self.nome=''
        self.login=''
        self.setor=''
        self.tipo_usuario='u'

    def getAll():
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from usuarios")
        result = cursor.fetchall()
        db.disconnect()
        lista_usuarios = []
        for x in result:
            usuario = Usuarios()
            usuario.id = x[0]
            usuario.login = x[3]
            usuario.nome = x[1]
            usuario.setor = x[4]
            usuario.tipo_usuario = x[5]
            lista_usuarios.append(usuario)
        return lista_usuarios
    
    def getById(id):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from usuarios where id = %s", (id,))
        result = cursor.fetchone()
        db.disconnect()
        try:
            usuario = Usuarios()
            usuario.id = result[0]
            usuario.nome = result[1]
            usuario.login = result[3]
            usuario.setor = result[4]
            usuario.tipo_usuario = result[5]
            return usuario
        except:
            return {"Erro": "Usuário não encontrado!"}
        
    def insert(nome, login, setor, tipo_usuario):
        usuario = Usuarios()
        usuario.nome = nome
        usuario.login = login
        usuario.setor = setor
        usuario.tipo_usuario = tipo_usuario
        usuario.senha = usuario.nome
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (nome, login, setor, tipo_usuario, senha) VALUES (%s, %s, %s, %s, %s)", (usuario.nome, usuario.login, usuario.setor, tipo_usuario, usuario.senha))
        db.commit()
        db.disconnect()
        return {"Mensagem": "Usuário inserido com sucesso"}
    
    def login(login, senha):
        token = []
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from usuarios where login = %s and senha = %s", (login, senha))
        result = cursor.fetchone()
        db.disconnect()
        try:
            token.append(result[0])
            token.append(random.randint(1, 50000000000))
            token.append(datetime.datetime.now())
            return token
        except:
            token.append(0)
            token.append(0)
            token.append(0)
            return token