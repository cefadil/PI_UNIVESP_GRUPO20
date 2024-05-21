from db import DB
import datetime
class Movimentacoes:
    def __init__(self):
        self.id = 0
        self.equipamento=0
        self.funcionario=0
        self.setor=0
        self.observacao=''
    
    def getAll():
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from movimentacoes")
        result = cursor.fetchall()
        db.disconnect()
        lista_movimentacoes = []
        for x in result:
            movimentacao = Movimentacoes()
            movimentacao.id = x[0]
            movimentacao.funcionario = x[1]
            movimentacao.setor = x[2]
            movimentacao.observacao = x[3]
            movimentacao.equipamento = x[4]
            movimentacao.data = x[5]
            lista_movimentacoes.append(movimentacao)
        return lista_movimentacoes
        
    
    def getById(id):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from movimentacoes where id = %s", (id,))
        result = cursor.fetchone()
        db.disconnect()
        try:
            movimentacao = Movimentacoes()
            movimentacao.id = result[0]
            movimentacao.funcionario = result[1]
            movimentacao.setor = result[2]
            movimentacao.observacao = result[3]
            movimentacao.equipamento = result[4]
            movimentacao.data = result[5]
            return movimentacao
        except:
            return {"Erro": "Movimentação não encontrada"}
        
    def insert(funcionario, setor, equipamento, observacao=''):
        agora = datetime.datetime.now()
        movimentacao = Movimentacoes()
        movimentacao.funcionario = funcionario
        movimentacao.setor = setor
        movimentacao.observacao = observacao
        movimentacao.equipamento = equipamento
        movimentacao.data = agora
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO movimentacoes (funcionario, setor, equipamento, datahora, observacao) VALUES (%s, %s, %s, %s, %s)", (movimentacao.funcionario, movimentacao.setor, movimentacao.equipamento, movimentacao.data ,movimentacao.observacao))
        db.commit()
        cursor.execute("UPDATE equipamentos SET local = %s WHERE id = %s", (movimentacao.setor, movimentacao.equipamento))
        db.commit()
        db.disconnect()
        return {"Mensagem": "Movimentação inserido com sucesso"}
    
    def getByEquipamento(id):
        db = DB().connect()
        cursor = db.cursor()
        cursor.execute("SELECT * from movimentacoes where equipamento = %s", (id,))
        result = cursor.fetchall()
        db.disconnect()
        lista_movimentacoes = []
        for x in result:
            movimentacao = Movimentacoes()
            movimentacao.id = x[0]
            movimentacao.funcionario = x[1]
            movimentacao.setor = x[2]
            movimentacao.observacao = x[3]
            movimentacao.equipamento = x[4]
            lista_movimentacoes.append(movimentacao)
        return lista_movimentacoes