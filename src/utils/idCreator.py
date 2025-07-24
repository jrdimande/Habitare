# Criar lógica para criação de ID's
import uuid
from src.utils.tempo import agora
import random


def gerar_id(nome):
    partes = nome.strip().upper().split()
    iniciais = ''.join(p[0] for p in partes)
    aleatorio = str(uuid.uuid4())[:4]

    return f"{iniciais}-{aleatorio}"

def gerar_pay_id():
    return f"PAY-{agora.strptime('%Y%m%d%H%M')}-{random.randint(100, 999)}"




