# Importa biblioteca para criptografia de senha
from passlib.context import CryptContext

# Importa biblioteca JWT
from jose import jwt

# Importa recursos de data e hora
from datetime import datetime, timedelta

# Importa recursos de autenticação do FastAPI
from fastapi import Depends, HTTPException

# Importa esquema OAuth2
from fastapi.security import OAuth2PasswordBearer

# Importa tratamento de erro JWT
from jose import JWTError


# Configuração do algoritmo de criptografia
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Chave utilizada na geração do token
SECRET_KEY = "projeto_backend_uninter"

# Algoritmo de criptografia do token
ALGORITHM = "HS256"

# Tempo de expiração do token
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Define endpoint responsável pela autenticação
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/usuarios/login"
)


# Função para gerar hash da senha
def gerar_hash_senha(senha: str):

    return pwd_context.hash(senha)


# Função para verificar se a senha informada corresponde ao hash salvo
def verificar_senha(
    senha: str,
    hash_senha: str
):

    return pwd_context.verify(
        senha,
        hash_senha
    )


# Função responsável pela criação do token JWT
def criar_token(dados: dict):

    # Cria cópia dos dados enviados
    dados_token = dados.copy()

    # Define tempo de expiração do token
    expiracao = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Adiciona expiração no token
    dados_token.update({
        "exp": expiracao
    })

    # Retorna token gerado
    return jwt.encode(
        dados_token,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# Função responsável pela validação do token JWT
def verificar_token(
    token: str = Depends(oauth2_scheme)
):

    try:

        # Decodifica token JWT
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Obtém e-mail do usuário
        email = payload.get("sub")

        # Verifica se token possui usuário
        if email is None:

            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

        return email

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

