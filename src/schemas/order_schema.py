# Importa a classe BaseModel do Pydantic
from pydantic import BaseModel


# Schema utilizado para criação de pedidos
class OrderCreate(BaseModel):

    # Nome do cliente
    cliente: str

    # Canal do pedido
    canal_pedido: str

    # Valor total do pedido
    valor_total: float

    # Status do pedido
    status: str


# Schema utilizado para resposta dos pedidos
class OrderResponse(BaseModel):

    # ID do pedido
    id: int

    # Nome do cliente
    cliente: str

    # Canal do pedido
    canal_pedido: str

    # Valor total do pedido
    valor_total: float

    # Status do pedido
    status: str

    class Config:
        from_attributes = True