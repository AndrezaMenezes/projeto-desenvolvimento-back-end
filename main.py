# Importa a biblioteca principal do FastAPI
from fastapi import FastAPI

# Importa a conexão com o banco de dados e a classe Base
from src.database.database import engine, Base

# Importa o modelo de usuário para criação da tabela no banco de dados
from src.models.user import User

# Importa o modelo de pedidos para criação da tabela no banco
from src.models.order import Order

# Importa as rotas relacionadas aos usuários
from src.api.user_api import router as user_router

# Importa as rotas relacionadas aos pedidos
from src.api.order_api import router as order_router

# Cria automaticamente as tabelas definidas nos models
Base.metadata.create_all(bind=engine)


# Configuração principal da API
app = FastAPI(
    title="Raízes do Nordeste API",
    description="API para gerenciamento de pedidos",
    version="1.0.0"
)


# Adiciona as rotas de usuários na aplicação
app.include_router(user_router)

# Adiciona as rotas de pedidos na aplicação
app.include_router(order_router)

# Endpoint inicial para verificar funcionamento da API
@app.get("/")
def root():
    return {"message": "API funcionando com sucesso"}