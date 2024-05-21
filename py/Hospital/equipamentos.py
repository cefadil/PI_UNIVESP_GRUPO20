from db import DB

class Equipamentos:

    def __init__(self):
        self.id = 0
        self.descricao=''
        self.fabricante=''
        self.modelo=''
        self.numero_serie=''
        self.tag=''
        self.local=0
    
    def getAll():
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from equipamentos")
        result = cursor.fetchall()
        db.disconnect()
        lista_equipamentos = []
        for x in result:
            equipamento = Equipamentos()
            equipamento.id = x[0]
            equipamento.descricao = x[1]
            equipamento.fabricante = x[2]
            equipamento.modelo = x[3]
            equipamento.numero_serie = x[4]
            equipamento.tag = x[5]
            equipamento.local = x[6]
            lista_equipamentos.append(equipamento)
        return lista_equipamentos
    
    def getById(id):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from equipamentos where id = %s", (id,))
        result = cursor.fetchone()
        db.disconnect()
        try:
            equipamento = Equipamentos()
            equipamento.id = result[0]
            equipamento.descricao = result[1]
            equipamento.fabricante = result[2]
            equipamento.modelo = result[3]
            equipamento.numero_serie = result[4]
            equipamento.tag = result[5]
            equipamento.local = result[6]

            return equipamento
        except:
            return {"Erro": "Equipamento não encontrado"}
        
    def insert(fabricante, modelo, descricao, numero_serie, tag, local):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO equipamentos (fabricante, modelo, descricao, num_serie, tag, local) VALUES (%s, %s, %s, %s, %s, %s)", (fabricante, modelo, descricao, numero_serie, tag, local))
        db.commit()
        db.disconnect()
        return {"Mensagem": "Equipamento inserido com sucesso"}
    
    def delete(id):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("DELETE FROM equipamentos where id = %s", (id,))
        db.commit()    
        db.disconnect()
        if cursor.rowcount == 0:
            return {"Erro": "Equipamento não encontrado"}
        return {"Mensagem": "equipamento deletado com sucesso"}
    
    def update(id, fabricante, modelo, descricao, numero_serie, tag, local):    
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("UPDATE equipamentos set fabricante = %s, modelo = %s, descricao = %s, numero_serie = %s, tag = %s, local = %s where id = %s",
                        (fabricante, modelo, descricao, numero_serie, tag, local, id))
        db.commit()
        db.disconnect()
        return {"Mensagem": "Equipamento atualizado com sucesso"}