# Importa os recursos necessários do FastAPI
from fastapi import APIRouter, Depends

# Importa a sessão do banco
from sqlalchemy.orm import Session

# Importa conexão com banco de dados
from src.database.database import SessionLocal

# Importa modelo de pedidos
from src.models.order import Order

# Importa schemas de pedidos
from src.schemas.order_schema import (
    OrderCreate,
    OrderResponse
)

# Importa função de validação do token JWT
from src.services.auth_service import verificar_token

# Cria agrupamento de rotas relacionadas aos pedidos
router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)


# Função responsável pela conexão com banco
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Endpoint para criação de pedidos
@router.post("/", response_model=OrderResponse)
def criar_pedido(
    pedido: OrderCreate,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):

    # Cria objeto de pedido
    novo_pedido = Order(
        cliente=pedido.cliente,
        canal_pedido=pedido.canal_pedido,
        valor_total=pedido.valor_total,
        status=pedido.status
    )

    # Salva pedido no banco
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)

    # Retorna pedido criado
    return novo_pedido


# Endpoint para listagem de pedidos
@router.get("/", response_model=list[OrderResponse])
def listar_pedidos(
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):

    # Busca todos os pedidos cadastrados
    pedidos = db.query(Order).all()

    # Retorna lista de pedidos
    return pedidos

# Endpoint para atualizar status do pedido
@router.put("/{pedido_id}")
def atualizar_status_pedido(
    pedido_id: int,
    status: str,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):

    # Busca pedido pelo ID
    pedido = db.query(Order).filter(
        Order.id == pedido_id
    ).first()

    # Verifica se pedido existe
    if not pedido:

        return {
            "erro": "Pedido não encontrado"
        }

    # Atualiza status do pedido
    pedido.status = status

    # Salva alterações
    db.commit()
    db.refresh(pedido)

    # Retorna pedido atualizado
    return pedido

# Endpoint para remoção de pedidos
@router.delete("/{pedido_id}")
def deletar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db),
    usuario: str = Depends(verificar_token)
):

    # Busca pedido pelo ID
    pedido = db.query(Order).filter(
        Order.id == pedido_id
    ).first()

    # Verifica se pedido existe
    if not pedido:

        return {
            "erro": "Pedido não encontrado"
        }

    # Remove pedido do banco
    db.delete(pedido)

    # Salva alterações
    db.commit()

    # Retorna confirmação
    return {
        "mensagem": "Pedido removido com sucesso"
    }