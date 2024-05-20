from db import DB
class Setores:
    def __init__(self):
        self.id = 0
        self.nome=''
        self.local=''
    
    def getAll():
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from setores")
        result = cursor.fetchall()
        db.disconnect()
        lista_setores = []
        for x in result:
            setor = Setores()
            setor.id = x[0]
            setor.nome = x[1]
            setor.local = x[2]
            lista_setores.append(setor)
        return lista_setores
    
    def getById(id):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from setores where id = %s", (id,))
        result = cursor.fetchone()
        db.disconnect()
        try:
            setor = Setores()
            setor.id = result[0]
            setor.nome = result[1]
            setor.local = result[2]
            return setor
        except:
            return {"Erro": "Setor não encontrado"}
        
    def insert(nome, local):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO setores (nome, local) VALUES (%s, %s)", (nome, local))
        db.commit()
        db.disconnect()
        return {"Mensagem": "Setor inserido com sucesso"}
    
    def delete(id):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM setores where id = %s", (id,))
        db.commit()
        db.disconnect()
        if cursor.rowcount == 0:
            return {"Erro": "Setor não encontrado"}
        
    
        return {"Mensagem": "Setor deletado com sucesso"}
    
    def update(id, nome, local):    
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("UPDATE setores set nome = %s, local = %s where id = %s", (nome, local, id))
        db.commit()
        db.disconnect()
        return {"Mensagem": "Setor atualizado com sucesso"}