from fastapi import FastAPI
from db import DB
from equipamentos import Equipamentos
from movimentacoes import Movimentacoes
from setores import Setores
from usuarios import Usuarios
import json

#FastAPI: Framework para criação de APIs
app = FastAPI()

#Conexão com o banco de dados
try:  
    db = DB()
    print(f"Iniciando Conexão...\nStatus: {db.conn.is_connected()}")
except ConnectionError as err:
    raise f"Falha na conexão. Erro: {err}"


#definição das rotas

@app.get("/")
async def root():
    return {"message": "Bem vindo ao Sistema de Gerenciamento de movimentações de equipamentos"}

@app.get("/setores")
async def listar_setores():
    lista_setores = Setores.getAll()
    return lista_setores

@app.get("/setores/{id}")
async def obter_setor(id: int):
    return Setores.getById(id)
    
@app.post("/setores")
async def inserir_setor(nome: str, local: str):
    return Setores.insert(nome, local)

@app.delete("/setores/{id}")
async def deletar_setor(id: int):
    return Setores.delete(id)

@app.put("/setores/{id}")  
async def atualizar_setor(id: int, nome: str, local: str):
    return Setores.update(id, nome, local)  