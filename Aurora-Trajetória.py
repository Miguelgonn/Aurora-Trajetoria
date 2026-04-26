# =============================================================================
# MGPEB - Módulo de Gerenciamento de Pouso e Estabilização de Base
# Missão Aurora Siger - Pouso em Marte
# =============================================================================

from collections import deque

# =============================================================================
# 1. DEFINIÇÃO DOS MÓDULOS DE POUSO
# Cada módulo é um dicionário com os atributos da missão.
# Prioridade: 1 = mais urgente, 5 = menos urgente
# =============================================================================

modulos = [
    {
        "nome": "Habitação",
        "prioridade": 1,
        "combustivel": 75,
        "massa": 12,
        "criticidade": "Alta",
        "chegada": "08:00"
    },
    {
        "nome": "Energia",
        "prioridade": 2,
        "combustivel": 60,
        "massa": 8,
        "criticidade": "Alta",
        "chegada": "09:30"
    },
    {
        "nome": "Suporte Médico",
        "prioridade": 2,
        "combustivel": 20,
        "massa": 4,
        "criticidade": "Alta",
        "chegada": "10:00"
    },
    {
        "nome": "Lab. Científico",
        "prioridade": 3,
        "combustivel": 45,
        "massa": 6,
        "criticidade": "Média",
        "chegada": "11:00"
    },
    {
        "nome": "Logística",
        "prioridade": 4,
        "combustivel": 30,
        "massa": 10,
        "criticidade": "Média",
        "chegada": "13:00"
    },
]

# =============================================================================
# 2. ESTRUTURAS DE DADOS LINEARES
#
# LISTA: armazena todos os módulos cadastrados
# FILA (deque): módulos aguardando autorização de pouso (FIFO)
# PILHA (list): histórico de eventos do sistema (LIFO)
# =============================================================================

lista_modulos = modulos.copy()           # Lista geral de todos os módulos
fila_pouso = deque(modulos.copy())       # Fila de espera para pouso
pilha_eventos = []                       # Pilha de histórico de eventos
lista_pousados = []                      # Lista de módulos já pousados
lista_alertas = []                       # Lista de módulos em situação de alerta

# =============================================================================
# 3. CONDIÇÕES AMBIENTAIS DA MISSÃO
# Variáveis booleanas que representam o estado atual do ambiente em Marte
# =============================================================================

TEMPESTADE_DE_AREIA = False   # True = há tempestade de areia ativa
AREA_DISPONIVEL = True        # True = área de pouso está livre
ERRO_SENSORES = False         # True = sensores do módulo com falha
LIMITE_COMBUSTIVEL = 25       # Percentual mínimo de combustível para pouso normal

# =============================================================================
# 4. ALGORITMOS DE BUSCA
# =============================================================================

def buscar_menor_combustivel(lista):
    """
    Busca sequencial: percorre toda a lista e retorna
    o módulo com o menor nível de combustível.
    Complexidade: O(n)
    """
    if not lista:
        return None
    menor = lista[0]
    for modulo in lista:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor


def buscar_por_criticidade(lista, nivel):
    """
    Busca sequencial: retorna todos os módulos com
    o nível de criticidade especificado ("Alta" ou "Média").
    Complexidade: O(n)
    """
    resultado = []
    for modulo in lista:
        if modulo["criticidade"] == nivel:
            resultado.append(modulo)
    return resultado


def buscar_por_nome(lista, nome):
    """
    Busca sequencial: localiza um módulo específico pelo nome.
    Complexidade: O(n)
    """
    for modulo in lista:
        if modulo["nome"].lower() == nome.lower():
            return modulo
    return None

# =============================================================================
# 5. ALGORITMO DE ORDENAÇÃO — SELECTION SORT (Ordenação por Seleção)
# Ordena a lista de módulos por prioridade de pouso (menor número = mais urgente)
# Complexidade: O(n²) — adequado para listas pequenas em sistemas embarcados
# =============================================================================

def ordenar_por_prioridade(lista):
    """
    Algoritmo de ordenação por seleção (Selection Sort).
    A cada iteração, encontra o menor elemento restante
    e o coloca na posição correta.
    """
    n = len(lista)
    lista_ord = lista.copy()
    for i in range(n):
        menor_idx = i
        for j in range(i + 1, n):
            if lista_ord[j]["prioridade"] < lista_ord[menor_idx]["prioridade"]:
                menor_idx = j
        # Troca os elementos de posição
        lista_ord[i], lista_ord[menor_idx] = lista_ord[menor_idx], lista_ord[i]
    return lista_ord


def ordenar_por_combustivel(lista):
    """
    Algoritmo de ordenação por inserção (Insertion Sort).
    Ordena do menor para o maior nível de combustível,
    priorizando módulos em situação mais crítica.
    Complexidade: O(n²)
    """
    lista_ord = lista.copy()
    for i in range(1, len(lista_ord)):
        chave = lista_ord[i]
        j = i - 1
        while j >= 0 and lista_ord[j]["combustivel"] > chave["combustivel"]:
            lista_ord[j + 1] = lista_ord[j]
            j -= 1
        lista_ord[j + 1] = chave
    return lista_ord

# =============================================================================
# 6. SIMULAÇÃO DE AUTORIZAÇÃO DE POUSO — REGRAS BOOLEANAS
#
# Regra principal:
# POUSO_AUTORIZADO = combustivel_ok AND area_ok AND sem_tempestade AND sem_erro
#
# Regra de emergência:
# POUSO_EMERGENCIA = NOT combustivel_ok AND criticidade_alta AND sem_erro
# =============================================================================

def autorizar_pouso(modulo):
    """
    Avalia as condições de pouso de um módulo usando lógica booleana.
    Retorna o status de autorização e registra o evento na pilha.

    Expressão booleana principal:
    AUTORIZADO = (comb > LIMITE) AND (AREA_DISPONIVEL) AND
                 (NOT TEMPESTADE_DE_AREIA) AND (NOT ERRO_SENSORES)
    """

    # Avaliação das variáveis booleanas
    combustivel_ok    = modulo["combustivel"] > LIMITE_COMBUSTIVEL
    area_ok           = AREA_DISPONIVEL
    sem_tempestade    = not TEMPESTADE_DE_AREIA
    sem_erro          = not ERRO_SENSORES
    carga_critica     = modulo["criticidade"] == "Alta"

    # Regra 1: Condições ideais → POUSO AUTORIZADO
    if combustivel_ok and area_ok and sem_tempestade and sem_erro:
        evento = f"[AUTORIZADO] {modulo['nome']}"
        pilha_eventos.append(evento)
        lista_pousados.append(modulo)
        return "✅ POUSO AUTORIZADO"

    # Regra 2: Combustível baixo + carga crítica + sem erros → EMERGÊNCIA
    elif not combustivel_ok and carga_critica and sem_erro and area_ok:
        evento = f"[EMERGÊNCIA] {modulo['nome']} — combustível crítico, carga prioritária"
        pilha_eventos.append(evento)
        lista_alertas.append(modulo)
        lista_pousados.append(modulo)
        return "⚠️  POUSO EM MODO DE EMERGÊNCIA (combustível crítico)"

    # Regra 3: Tempestade ativa → BLOQUEADO
    elif not sem_tempestade:
        evento = f"[BLOQUEADO] {modulo['nome']} — tempestade de areia ativa"
        pilha_eventos.append(evento)
        lista_alertas.append(modulo)
        return "❌ POUSO BLOQUEADO — aguardando fim da tempestade"

    # Regra 4: Erro nos sensores → BLOQUEADO
    elif not sem_erro:
        evento = f"[BLOQUEADO] {modulo['nome']} — erro nos sensores"
        pilha_eventos.append(evento)
        lista_alertas.append(modulo)
        return "❌ POUSO BLOQUEADO — falha nos sensores de navegação"

    # Regra 5: Área indisponível → AGUARDANDO
    elif not area_ok:
        evento = f"[AGUARDANDO] {modulo['nome']} — área de pouso ocupada"
        pilha_eventos.append(evento)
        return "🔄 AGUARDANDO — área de pouso indisponível"

    # Regra 6: Outros casos → BLOQUEADO
    else:
        evento = f"[BLOQUEADO] {modulo['nome']} — condições insuficientes"
        pilha_eventos.append(evento)
        return "❌ POUSO BLOQUEADO — condições insuficientes"

# =============================================================================
# 7. EXECUÇÃO PRINCIPAL — SIMULAÇÃO COMPLETA
# =============================================================================

def separador(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)


def exibir_modulo(m):
    print(f"  • {m['nome']:<20} | Prioridade: {m['prioridade']} "
          f"| Combustível: {m['combustivel']:>3}% "
          f"| Criticidade: {m['criticidade']:<6} "
          f"| Chegada: {m['chegada']}")


# --- Exibe a fila original ---
separador("FILA DE POUSO — ORDEM DE CHEGADA À ÓRBITA")
for m in fila_pouso:
    exibir_modulo(m)

# --- Busca o módulo com menor combustível ---
separador("BUSCA: MÓDULO COM MENOR COMBUSTÍVEL")
critico = buscar_menor_combustivel(lista_modulos)
print(f"  ⚠️  Atenção: {critico['nome']} está com apenas {critico['combustivel']}% de combustível!")

# --- Busca por criticidade Alta ---
separador("BUSCA: MÓDULOS COM CRITICIDADE ALTA")
criticos = buscar_por_criticidade(lista_modulos, "Alta")
for m in criticos:
    exibir_modulo(m)

# --- Ordena por prioridade e reconstrói a fila ---
separador("ORDENAÇÃO POR PRIORIDADE (Selection Sort)")
modulos_por_prioridade = ordenar_por_prioridade(lista_modulos)
for m in modulos_por_prioridade:
    exibir_modulo(m)

# --- Ordena por combustível ---
separador("ORDENAÇÃO POR COMBUSTÍVEL (Insertion Sort — mais crítico primeiro)")
modulos_por_combustivel = ordenar_por_combustivel(lista_modulos)
for m in modulos_por_combustivel:
    exibir_modulo(m)

# --- Simulação de autorização de pouso (usando ordem por prioridade) ---
separador("SIMULAÇÃO DE AUTORIZAÇÃO DE POUSO")
print(f"  Condições ambientais:")
print(f"  • Tempestade de areia : {'SIM' if TEMPESTADE_DE_AREIA else 'NÃO'}")
print(f"  • Área disponível     : {'SIM' if AREA_DISPONIVEL else 'NÃO'}")
print(f"  • Erro nos sensores   : {'SIM' if ERRO_SENSORES else 'NÃO'}")
print(f"  • Limite combustível  : {LIMITE_COMBUSTIVEL}%\n")

for m in modulos_por_prioridade:
    resultado = autorizar_pouso(m)
    print(f"  {m['nome']:<20} → {resultado}")

# --- Exibe listas resultantes ---
separador("MÓDULOS JÁ POUSADOS")
if lista_pousados:
    for m in lista_pousados:
        print(f"  ✅ {m['nome']}")
else:
    print("  Nenhum módulo pousou ainda.")

separador("MÓDULOS EM SITUAÇÃO DE ALERTA")
if lista_alertas:
    for m in lista_alertas:
        print(f"  ⚠️  {m['nome']}")
else:
    print("  Nenhum módulo em alerta.")

# --- Exibe o histórico de eventos pela pilha (LIFO) ---
separador("HISTÓRICO DE EVENTOS — PILHA (último evento primeiro)")
eventos_temp = pilha_eventos.copy()
while eventos_temp:
    print(f"  {eventos_temp.pop()}")

separador("FIM DA SIMULAÇÃO MGPEB — AURORA SIGER")
