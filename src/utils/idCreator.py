# Criar lógica para criação de ID's
import uuid
from src.utils.tempo import agora
import random


def gerar_inq_id():
    " Cria IDs para inquilinos "
    aleatorio = str(uuid.uuid4())[:4]
    return f"INQ-{aleatorio}"

    return f"{iniciais}-{aleatorio}"

def gerar_pay_id():
    " Cria IDs para pagamentos"
    return f"PAY-{agora.strptime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"

def gerar_imo_id():
    " Criar IDs para imóveis"
    aleatorio = str(uuid.uuid4())[:4]
    return f"IMO-{aleatorio}"




