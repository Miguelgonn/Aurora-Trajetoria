## 🚀 Aurora Siger | MGPEB

### Módulo de Gerenciamento de Pouso e Estabilização de Base

Projeto acadêmico desenvolvido para simular uma **missão interplanetária de colonização em Marte**, com foco no gerenciamento inteligente da fase de pouso e da implantação inicial da base.

O sistema **MGPEB** controla pousos autônomos de módulos essenciais, utilizando conceitos de:

- Lógica computacional  
- Programação em Python  
- Estruturas de dados lineares  
- Algoritmos de busca e ordenação  
- Funções matemáticas aplicadas  
- Sistemas embarcados  
- História da computação  
- ESG e governança tecnológica  

# 🌌 Sobre a Missão Aurora Siger

A missão **Aurora Siger** representa a primeira tentativa sustentada de estabelecer uma colônia permanente em Marte.

O local escolhido para implantação da base foi a regiao **Isidis Planitia**, no hemisfério norte marciano, selecionado por apresentar:

- topografia relativamente plana;
- menor incidência de ventos extremos;
- baixa altitude favorável ao pouso;
- indícios geológicos de água no subsolo;
- potencial para futuras operações de mineração e produção de água potável.

A área principal de aterrissagem foi denominada **Plataforma Alpha**.

Todos os pousos são gerenciados de forma autônoma pelo **MGPEB**, sem dependência de comunicação imediata com a Terra.

# 🎯 Objetivo do MGPEB

O sistema foi projetado para:

✅ Organizar a fila de módulos em órbita  
✅ Priorizar aterrissagens críticas  
✅ Verificar segurança antes do pouso  
✅ Autorizar, adiar ou cancelar operações  
✅ Registrar histórico operacional  
✅ Auxiliar a sobrevivência inicial da colônia  

# 🛰️ Módulos da Fase Inicial

## HAB-01 — Habitação

Módulo de maior criticidade humana da missão.

- dormitórios pressurizados;
- controle atmosférico interno;
- suporte à vida;
- áreas de convivência.

## ENE-01 — Energia

Responsável pelo fornecimento elétrico da base.

- painéis solares;
- baterias;
- gerador de backup.

## LAB-01 — Laboratório Científico

Voltado para pesquisas geológicas, climáticas e bioquímicas.

Também auxilia no monitoramento ambiental.

## LOG-01 — Logística

- veículos de superfície;
- ferramentas;
- peças;
- suprimentos gerais.

## MED-01 — Suporte Médico

- equipamentos cirúrgicos;
- farmácia;
- diagnóstico;
- apoio psicológico.


# 🧠 Estruturas de Dados Utilizadas

## Fila Principal (FIFO)

Gerencia módulos aguardando pouso.

Exemplo:

HAB-01 pousa → ENE-01 torna-se o próximo.

## Lista de Pousados

Armazena módulos já instalados na superfície.

## Lista de Espera

Módulos temporariamente impedidos.

Exemplo:

- pista ocupada;
- combustível em alerta;
- clima desfavorável.

## Lista de Alerta

Módulos em condição crítica.

Exemplo:

LOG-01 com combustível crítico.

## Pilha de Decisões (LIFO)

Permite desfazer a última decisão operacional via override manual.


# 🔌 Regras Lógicas de Pouso

O sistema só autoriza pouso se todas as condições forem verdadeiras:

- combustível suficiente;
- clima favorável;
- pista livre;
- sensores íntegros.

```python
if combustivel_ok and clima_ok and pista_livre and sensores_ok:
    print("Pouso autorizado")
else:
    print("Pouso adiado")
