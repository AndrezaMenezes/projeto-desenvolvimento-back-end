# Importa a função responsável por criar a conexão com o banco
from sqlalchemy import create_engine

# Importa a base utilizada para criação das tabelas do banco
from sqlalchemy.ext.declarative import declarative_base

# Importa o criador de sessões do SQLAlchemy
from sqlalchemy.orm import sessionmaker


# Define o banco de dados SQLite utilizado no projeto
DATABASE_URL = "sqlite:///./raizes_nordeste.db"


# Cria a conexão com o banco de dados
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Cria sessões para comunicação com o banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Classe base utilizada pelos modelos do sistema
Base = declarative_base()