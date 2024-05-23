from fastapi import Depends, FastAPI, HTTPException, Request
from db import DB
from equipamentos import Equipamentos
from movimentacoes import Movimentacoes
from setores import Setores
from usuarios import Usuarios
import json
import uvicorn
import datetime
import random
import sys

app = FastAPI()
#FastAPI: Framework para criação de APIs

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

#Conexão com o banco de dados
try:  
    db = DB()
    print(f"Iniciando Conexão...\nStatus: {db.conn.is_connected()}")
except ConnectionError as err:
    raise f"Falha na conexão. Erro: {err}"
tokens = []

#definição das rotas

def checklogin(request: Request):
    token=request.headers.get("authorization")
    for x in tokens:
        if str(token) == str(x[1]):
            #verificar periodo do token
            agora = datetime.datetime.now()
            diferenca = agora - x[2]
            delta = diferenca.total_seconds()
            print(x)
            if delta > 100:
                tokens.remove(x)
                raise HTTPException(status_code=401, detail="Token expirado. Faça login novamente!")
            
            revalidar_token(x)
            print(x)
            return True
    raise HTTPException(status_code=401, detail="Acesso negado. Autenticação Necessária!")

def revalidar_token(x):
    x[2] = datetime.datetime.now()

@app.get("/")
async def root():
    return {"message": "Bem vindo ao Sistema de Gerenciamento de movimentações de equipamentos"}

@app.get("/setores")
async def listar_setores(autenticado: bool = Depends(checklogin)):
    lista_setores = Setores.getAll()
    return lista_setores

@app.get("/setores/{id}")
async def obter_setor(id: int, autenticado:bool = Depends(checklogin)):
    return Setores.getById(id)
    
@app.post("/setores")
async def inserir_setor(nome, local, autenticado: bool = Depends(checklogin)):
    return Setores.insert(nome, local)

@app.delete("/setores/{id}")
async def deletar_setor(id: int, autenticado: bool = Depends(checklogin)):
    return Setores.delete(id)

@app.put("/setores/{id}")  
async def atualizar_setor(id: int, nome: str, local: str, autenticado: bool = Depends(checklogin)):
    return Setores.update(id, nome, local)  

@app.get("/equipamentos")
async def listar_equipamentos(autenticado: bool = Depends(checklogin)):
    lista_equipamentos = Equipamentos.getAll()
    return lista_equipamentos

@app.get("/equipamentos/{id}")
async def obter_equipamento(id: int, autenticado: bool = Depends(checklogin)):
    return Equipamentos.getById(id)

@app.post("/equipamentos")
async def inserir_equipamento(fabricante: str, modelo: str, descricao: str, numero_serie: str, tag: str, local: int, autenticado: bool = Depends(checklogin)):
    return Equipamentos.insert(fabricante, modelo, descricao, numero_serie, tag, local)

@app.delete("/equipamentos/{id}")
async def deletar_equipamento(id: int, autenticado: bool = Depends(checklogin)):
    return Equipamentos.delete(id)

@app.put("/equipamentos/{id}")
async def atualizar_equipamento(id: int, fabricante: str, modelo: str, descricao: str, numero_serie: str, tag: str, local: int, autenticado: bool = Depends(checklogin)):
    return Equipamentos.update(id, fabricante, modelo, descricao, numero_serie, tag, local)

@app.get("/movimentacoes")
async def listar_movimentacoes(autenticado: bool = Depends(checklogin)):
    lista_movimentacoes = Movimentacoes.getAll()
    return lista_movimentacoes

@app.get("/movimentacoes/{id}")
async def obter_movimentacao(id: int, autenticado: bool = Depends(checklogin)):
    return Movimentacoes.getById(id)

@app.post("/movimentacoes")
async def inserir_movimentacao(funcionario: int, setor: int, equipamento: int, observacao: str, autenticado: bool = Depends(checklogin)):
    return Movimentacoes.insert(funcionario, setor, equipamento, observacao)

@app.get("/movimentacoes/equipamento/{id}")
async def obter_movimentacao_por_equipamento(id: int, autenticado: bool = Depends(checklogin)):
    return Movimentacoes.getByEquipamento(id)

@app.get("/usuarios")
async def listar_usuarios(autenticado: bool = Depends(checklogin)):
    lista_usuarios = Usuarios.getAll()
    return lista_usuarios

@app.get("/usuarios/{id}")
async def obter_usuario(id: int, autenticado: bool = Depends(checklogin)):
    return Usuarios.getById(id)

@app.post("/usuarios")
async def inserir_usuario(nome: str, login: str, setor: int, tipo_usuario: str, autenticado: bool = Depends(checklogin)):
    return Usuarios.insert(nome, login, setor, tipo_usuario)

@app.post("/usuarios/login")
async def login(login, senha):
    token = Usuarios.login(login, senha)
    if token[0]==0:
        return {"Erro": "Usuário ou senha incorretos. Tente novamente!"}
    for x in tokens:
        if x[0] == token[0]:
            tokens.remove(x)
    tokens.append(token)
    return token[1]
