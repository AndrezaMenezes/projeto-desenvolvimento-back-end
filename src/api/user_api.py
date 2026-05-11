# Importa os recursos necessários do FastAPI
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Importa a sessão do banco de dados
from src.database.database import SessionLocal

# Importa o modelo de usuário
from src.models.user import User

# Importa os schemas de validação e resposta
from src.schemas.user_schema import UserCreate, UserResponse

# Importa função de geração de hash de senha
from src.services.auth_service import gerar_hash_senha

# Importa schema de login
from src.schemas.user_schema import LoginSchema

# Importa formulário padrão OAuth2 utilizado no login com JWT
from fastapi.security import OAuth2PasswordRequestForm

# Importa funções de autenticação
from src.services.auth_service import (
    verificar_senha,
    criar_token
)

# Cria o agrupamento de rotas relacionadas aos usuários
router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


# Função responsável por abrir e fechar conexão com banco
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Endpoint para cadastro de usuários
@router.post("/", response_model=UserResponse)
def criar_usuario(
    usuario: UserCreate,
    db: Session = Depends(get_db)
):

    # Cria objeto de usuário
    novo_usuario = User(
        nome=usuario.nome,
        email=usuario.email,
        senha=gerar_hash_senha(usuario.senha),
        perfil=usuario.perfil
    )

    # Salva no banco
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    # Retorna usuário criado
    return novo_usuario

# Endpoint responsável pelo login do usuário
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # Busca usuário pelo e-mail
    usuario = db.query(User).filter(
        User.email == form_data.username
    ).first()

    # Verifica se usuário existe
    if not usuario:

        return {
            "erro": "Usuário não encontrado"
        }

    # Verifica senha
    senha_valida = verificar_senha(
        form_data.password,
        usuario.senha
    )

    # Retorna erro caso senha inválida
    if not senha_valida:

        return {
            "erro": "Senha inválida"
        }

    # Gera token JWT
    token = criar_token({
        "sub": usuario.email
    })

    # Retorna token
    return {
        "access_token": token,
        "token_type": "bearer"
    }