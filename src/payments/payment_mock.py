# Importa biblioteca para geração aleatória
import random


# Função responsável por simular pagamento
def simular_pagamento():

    # Define respostas possíveis
    respostas = [
        "APROVADO",
        "RECUSADO"
    ]

    # Retorna resultado aleatório
    return random.choice(respostas)