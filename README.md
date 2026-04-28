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

## 🌌 Sobre a Missão Aurora Siger

A missão **Aurora Siger** representa a primeira tentativa sustentada de estabelecer uma colônia permanente em Marte.

O local escolhido para implantação da base foi a regiao **Isidis Planitia**, no hemisfério norte marciano, selecionado por apresentar:

- topografia relativamente plana;
- menor incidência de ventos extremos;
- baixa altitude favorável ao pouso;
- indícios geológicos de água no subsolo;
- potencial para futuras operações de mineração e produção de água potável.

A área principal de aterrissagem foi denominada **Plataforma Alpha**.

Todos os pousos são gerenciados de forma autônoma pelo **MGPEB**, sem dependência de comunicação imediata com a Terra.

## 🎯 Objetivo do MGPEB

O sistema foi projetado para:

✅ Organizar a fila de módulos em órbita  
✅ Priorizar aterrissagens críticas  
✅ Verificar segurança antes do pouso  
✅ Autorizar, adiar ou cancelar operações  
✅ Registrar histórico operacional  
✅ Auxiliar a sobrevivência inicial da colônia  

## 🛰️ Módulos da Fase Inicial

### HAB-01 — Habitação

Módulo de maior criticidade humana da missão.

- dormitórios pressurizados;
- controle atmosférico interno;
- suporte à vida;
- áreas de convivência.

### ENE-01 — Energia

Responsável pelo fornecimento elétrico da base.

- painéis solares;
- baterias;
- gerador de backup.

### LAB-01 — Laboratório Científico

Voltado para pesquisas geológicas, climáticas e bioquímicas.

Também auxilia no monitoramento ambiental.

### LOG-01 — Logística

- veículos de superfície;
- ferramentas;
- peças;
- suprimentos gerais.

### MED-01 — Suporte Médico

- equipamentos cirúrgicos;
- farmácia;
- diagnóstico;
- apoio psicológico.


## 🧠 Estruturas de Dados Utilizadas

### Fila Principal (FIFO)

Gerencia módulos aguardando pouso.

Exemplo:

HAB-01 pousa → ENE-01 torna-se o próximo.

### Lista de Pousados

Armazena módulos já instalados na superfície.

### Lista de Espera

Módulos temporariamente impedidos.

Exemplo:

- pista ocupada;
- combustível em alerta;
- clima desfavorável.

### Lista de Alerta

Módulos em condição crítica.

Exemplo:

LOG-01 com combustível crítico.

### Pilha de Decisões (LIFO)

Permite desfazer a última decisão operacional via override manual.


## 🔌 Regras Lógicas de Pouso

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
```
## 💻 Contextualização Histórica e Arquitetural do Sistema

### Dos Computadores de Propósito Geral aos Sistemas Embarcados

O desenvolvimento do **MGPEB** está diretamente relacionado à evolução histórica da computação. As primeiras ideias de máquinas programáveis surgiram no século XIX com **Charles Babbage**, por meio da Máquina Diferencial e da Máquina Analítica.

Na década de 1940, o **ENIAC (1945)** marcou o início dos computadores eletrônicos de propósito geral. Embora enorme e energeticamente ineficiente, abriu caminho para sistemas capazes de realizar cálculos complexos automaticamente.

Em seguida, a **Arquitetura de Von Neumann** revolucionou a computação ao permitir que programas e dados fossem armazenados na mesma memória, criando a base dos computadores modernos.

Com a evolução dos **transistores** e dos **circuitos integrados**, tornou-se possível miniaturizar computadores, reduzir consumo energético e aumentar confiabilidade. Esse avanço permitiu o surgimento dos **sistemas embarcados**, projetados para executar funções específicas em ambientes críticos.

### Aplicações Espaciais

O projeto se inspira em sistemas históricos utilizados em missões reais, como:

- **Apollo Guidance Computer (AGC)** — responsável pela navegação das missões Apollo;
- **Viking (1976)** e **Pathfinder (1997)**;
- **Curiosity (2012)**, equipado com processador **RAD750**, resistente à radiação.

Esses sistemas priorizam confiabilidade acima de desempenho bruto.

### Limitações de Hardware em Marte

O MGPEB considera desafios reais de uma missão marciana:

- **Radiação ionizante**, capaz de corromper memória eletrônica;
- **Memória limitada**, exigindo estruturas simples e eficientes;
- **Baixo poder de processamento**, comum em computadores espaciais;
- **Energia escassa**, especialmente durante tempestades de poeira;
- **Latência Terra-Marte**, inviabilizando controle humano em tempo real.

### Impacto no Projeto MGPEB

Essas restrições justificam as escolhas adotadas no sistema:

- uso de algoritmos simples e auditáveis;
- estruturas lineares como filas, listas e pilhas;
- lógica booleana explícita;
- código modular em Python;
- autonomia operacional para decisões críticas.

### Conclusão

O MGPEB não representa apenas um exercício acadêmico, mas uma simulação coerente dos desafios reais enfrentados por engenheiros de software espacial. Cada decisão tomada no projeto reflete princípios utilizados em missões históricas e futuras operações humanas em Marte.

## Print De Execução

### Diagrama 


<img width="596" height="843" alt="image" src="https://github.com/user-attachments/assets/19413fb9-3d01-4dfb-a6ea-25aaaff70210" />


<img width="539" height="756" alt="image" src="https://github.com/user-attachments/assets/6182b9a8-0122-4f5f-8f0c-6fc6cb660c69" />

----------

### Tabela Verdade 

<img width="1123" height="793" alt="image" src="https://github.com/user-attachments/assets/acb664b4-0ee2-4aae-a523-9a88c4358b89" />


<img width="1122" height="798" alt="image" src="https://github.com/user-attachments/assets/3da39199-9bf9-49c9-ba1c-ecc92c17e78e" />

---------------

### Pouso Aprovado

<img width="1296" height="766" alt="image" src="https://github.com/user-attachments/assets/9f3ca1f7-8b4b-4148-a71b-12a411650b11" />


<img width="1332" height="777" alt="image" src="https://github.com/user-attachments/assets/c8819199-5e80-4415-ad45-ed9ed6e3356f" />

----------
### Pouso Liberado Com Emergência

<img width="1296" height="769" alt="image" src="https://github.com/user-attachments/assets/cd5a3cb1-636a-462e-8d9d-c3dcf2ce4b66" />



<img width="1299" height="772" alt="image" src="https://github.com/user-attachments/assets/35b2e1d5-38db-4a02-948a-9326d6992345" />

-----------

### Pouso Interrompido

<img width="1306" height="766" alt="image" src="https://github.com/user-attachments/assets/b24ecc1f-683d-4d78-9b6e-68ed4be1d637" />



<img width="1294" height="775" alt="image" src="https://github.com/user-attachments/assets/ee1e9f4c-2f0e-4efc-a670-d2e24921a0a3" />

