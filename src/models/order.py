# Importa os tipos de colunas utilizados na tabela
from sqlalchemy import Column, Integer, String, Float

# Importa a classe Base utilizada pelos modelos
from src.database.database import Base


# Classe responsável pela estrutura da tabela de pedidos
class Order(Base):

    # Nome da tabela no banco de dados
    __tablename__ = "orders"

    # Identificador único do pedido
    id = Column(Integer, primary_key=True, index=True)

    # Nome do cliente
    cliente = Column(String, nullable=False)

    # Canal utilizado para realização do pedido
    canal_pedido = Column(String, nullable=False)

    # Valor total do pedido
    valor_total = Column(Float, nullable=False)

    # Status atual do pedido
    status = Column(String, nullable=False)