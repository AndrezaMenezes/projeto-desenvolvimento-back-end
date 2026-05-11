# Importa os tipos de colunas utilizados na tabela
from sqlalchemy import Column, Integer, String

# Importa a classe Base responsável pela criação das tabelas no banco
from src.database.database import Base


# Classe responsável pela estrutura da tabela de usuários
class User(Base):

    # Define o nome da tabela no banco de dados
    __tablename__ = "users"

    # Identificador único do usuário
    id = Column(Integer, primary_key=True, index=True)

    # Nome do usuário
    nome = Column(String, nullable=False)

    # E-mail único utilizado para autenticação
    email = Column(String, unique=True, nullable=False)

    # Senha do usuário
    senha = Column(String, nullable=False)

    # Perfil de acesso do usuário (ADMIN, CLIENTE, etc.)
    perfil = Column(String, nullable=False)