import random

# Conjunto de terminais (notas)
notas = ['Dó', 'Ré', 'Mi', 'Sol', 'Lá']

# Regras de produção:
# S → D | D S
# D → Dó | Ré | Mi | Sol | Lá

def gerar_D():
    """Produção: D → Dó | Ré | Mi | Sol | Lá"""
    return random.choice(notas)

def gerar_S():
    """Produção: S → D | D S"""
    if random.choice([True, False]):  # Decide se continua a derivação
        return gerar_D() + " " + gerar_S()
    else:
        return gerar_D()

def gerar_composicao():
    """Símbolo inicial: S"""
    return gerar_S()

if __name__ == "__main__":
    composicao = gerar_composicao()
    print("Composição gerada:", composicao)

