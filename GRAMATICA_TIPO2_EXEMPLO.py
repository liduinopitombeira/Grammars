import random

# Conjunto de notas possíveis (terminais)
NOTAS = ['Dó', 'Ré', 'Mi', 'Sol', 'Lá']

# ---- Produções ----
def gerar_N():
    return random.choice(NOTAS)

def gerar_M():
    # M → N  |  N N
    if random.choice([True, False]):
        return [gerar_N()]
    else:
        return [gerar_N(), gerar_N()]

def gerar_F():
    # F → M  |  M F
    if random.choice([True, False]):
        return gerar_M()
    else:
        return gerar_M() + gerar_F()

def gerar_S():
    # S → F  |  F S
    if random.choice([True, False]):
        return gerar_F()
    else:
        return gerar_F() + gerar_S()

def gerar_composicao():
    return gerar_S()

if __name__ == "__main__":
    composicao = gerar_composicao()
    print("Fragmento gerado:", " ".join(composicao))
