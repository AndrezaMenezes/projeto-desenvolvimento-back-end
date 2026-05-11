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

### Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar servidor

```bash
uvicorn main:app --reload
```

---

## Documentação Swagger

Após executar o servidor:

```text
http://127.0.0.1:8000/docs
```

---

## Estrutura do projeto

```text
src/
├── api/
├── database/
├── models/
├── schemas/
└── services/
```

---

## Autora

Andreza Menezes