# Raízes do Nordeste API

API desenvolvida em FastAPI para gerenciamento de usuários e pedidos.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLite
- SQLAlchemy
- JWT Authentication
- OAuth2
- Swagger/OpenAPI

---

## Funcionalidades

### Usuários
- Cadastro de usuários
- Login com autenticação JWT
- Criptografia de senha com bcrypt

### Pedidos
- Criar pedidos
- Listar pedidos
- Atualizar status do pedido
- Remover pedidos

---

## Segurança

A API utiliza:
- JWT (JSON Web Token)
- OAuth2PasswordBearer
- Rotas protegidas

---

## Como executar o projeto

### Criar ambiente virtual

```bash
python -m venv venv