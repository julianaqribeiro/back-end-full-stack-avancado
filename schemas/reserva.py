from typing import List
from pydantic import BaseModel
from datetime import datetime

from model.reserva import Reserva


class ReservaSchema(BaseModel):
    """ 
    Define como uma reserva a ser inserida 
    deve ser representada
    """     
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"
    dataReserva: datetime = datetime.now()
    qtdPessoas: int = 1
       

class ReservaViewSchema(BaseModel):
    """ 
    Define como uma reserva será retornado na listagem 
    do Reservas
    """
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999" 
    dataReserva: datetime = datetime.now()
    qtdPessoas: int = 1   


class ReservaAddSchema(BaseModel):
    """ 
    Define como uma reserva a ser inserida
    deve ser representada
    """
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999" 
    dataReserva: datetime = datetime.now()
    qtdPessoas: int = 1             

def apresenta_nova_reserva(item: Reserva):
    """ 
    Retorna uma representação da nova Reserva
    """
    return {
        "id": item.id,
        "nome": item.nome,
        "email": item.email, 
        "telefone": item.telefone,
        "dataReserva": item.dataReserva,
        "qtdPessoas": item.qtdPessoas
    }

class ListagemReserva(BaseModel):
    """ 
    Define a representacao das
    Reservas
    """
    lojas: List[ReservaSchema] 

def apresenta_reserva(lista: List[Reserva]):
    """ Retorna uma representação da listagem das reservas
    """
    result = []
    for item in lista:
        result.append({
            "id": item.id,
            "nome": item.nome,
            "email": item.email, 
            "telefone": item.telefone, 
            "datareserva": item.dataReserva,
            "qtdpessoas": item.qtdPessoas 
        })        

    return {"mensagens": result}
