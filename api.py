#!/usr/bin/env python3

# https://tinyurl.com/devsecops260326

from fastapi import FastAPI
from pydantic import BaseModel

class Tarefa(BaseModel):
    id: int
    titulo: str
    finalizado: bool = False

API = FastAPI()
TAREFAS = []

@API.get('/tarefas')
def tarefas():
    return TAREFAS

@API.post('/tarefas')
def criar_tarefa(titulo: str):
    tarefa_nova = Tarefa(id=len(TAREFAS), titulo=titulo)
    TAREFAS.append(tarefa_nova)
    return f"Tarefa '{titulo}' criada"

@API.delete('/tarefas/{id}')
def apagar_tarefa(id: int):
    if len(TAREFAS) > 0 and id < len(TAREFAS):
        t = TAREFAS.pop(id)

        return f"Tarefa '{t.titulo}' apagada"

    return "Tarefa não existe"

@API.put('/tarefas/{id}')
def atualizar_tarefa(id: int, titulo: str, estado: bool):
    if len(TAREFAS) > 0 and id < len(TAREFAS):
        TAREFAS[id].titulo = titulo
        TAREFAS[id].finalizado = estado
        return f"Tarefa '{id}' atualizada"
    return "Tarefa não existe"

@API.get('/')
def root():
    return 'ok'

@API.get('/autor')
def autor():
    return 'Vitor Hugo'
