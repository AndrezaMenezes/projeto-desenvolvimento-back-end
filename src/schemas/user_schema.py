# Importa a classe BaseModel do Pydantic
from pydantic import BaseModel, EmailStr


# Schema utilizado para criação de usuários
class UserCreate(BaseModel):

    # Nome do usuário
    nome: str

    # E-mail do usuário
    email: EmailStr

    # Senha do usuário
    senha: str

    # Perfil de acesso do usuário
    perfil: str


# Schema utilizado para resposta da API
class UserResponse(BaseModel):

    # ID do usuário
    id: int

    # Nome do usuário
    nome: str

    # E-mail do usuário
    email: EmailStr

    # Perfil do usuário
    perfil: str

    class Config:
        from_attributes = True

# Schema utilizado para login do usuário
class LoginSchema(BaseModel):

    # E-mail do usuário
    email: EmailStr

    # Senha do usuário
    senha: str