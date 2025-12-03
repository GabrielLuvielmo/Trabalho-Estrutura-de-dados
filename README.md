# Trabalho – Estrutura de Dados

## 📌 Visão Geral
Este documento descreve a proposta completa do trabalho. O objetivo é entregar um projeto que envolva:

- Estruturas de dados básicas (pilha, fila, fila circular, lista, lista encadeada, dicionário/objetos)  
- Manipulação de CSV (leitura e escrita)  
- Árvores (BST e AVL)  
- Ordenação (pelo menos dois algoritmos: um O(n²) e outro O(n log n))  
- Busca linear e busca binária  
- Análise assintótica (complexidade Big O)

O trabalho foi projetado para ser realizado em **3 horas de aula**, em grupos de **5 alunos**.

---

## 📂 Dataset
Utilizar **apenas** o arquivo `results.csv` do dataset **Global Football Goalscorers Dataset (Kaggle)**.

Todas as tarefas, filtros e arquivos gerados deverão partir deste CSV.

### Campos:
- **date** — Data da partida  
- **home_team** — Seleção mandante  
- **away_team** — Seleção visitante  
- **home_score** — Gols do time da casa  
- **away_score** — Gols do time visitante  
- **tournament** — Torneio (World Cup, Friendly etc.)  
- **city** — Cidade da partida  
- **country** — País  
- **neutral** — Campo neutro (TRUE/FALSE)

---

## 📦 Entregáveis Esperados
- Código fonte organizado em módulos Python  
- Arquivo gerado: `matches_summary.csv`  
- Relatório (PDF ou MD) contendo:
  - arquitetura
  - complexidade Big O
  - evidências de execução
  - contribuição de cada membro

---

## 🧩 Etapa 1 — Modelagem: Classes `Match` e `Team`
### Objetivo:
Representar cada partida utilizando classes Python.

### O que implementar:
Arquivo `src/data_structs.py`:
- Classe **Team**  
  - `name: string`  
  - `score: int`

- Classe **Match**  
  - `date (datetime)`  
  - `home_team (Team)`  
  - `away_team (Team)`  
  - `tournament (string)`  
  - `city (string)`  
  - `country (string)`  
  - `neutral (bool)`

### Métodos:
- `total_goals()` → retorna a soma de gols do jogo  
- `to_list()` → retorna linha pronta para CSV (ano, país, times e placar)

### Avaliação:
- Uso correto das estruturas  
- Implementação dos algoritmos  
- Complexidade Big O

---

## 📥 Etapa 2 — Leitura do CSV e Criação das Estruturas
### Objetivo:
Ler `results.csv`, criar objetos Match e inserir em uma estrutura de dados escolhida.

### Tarefas:
- Abrir `data/results.csv` com `csv`  
- Para cada linha válida, criar `Match`  
- Inserir em uma ED: Lista, Pilha, Fila, Lista Encadeada etc.  
- Filtrar linhas com dados faltantes  
- Explicar no relatório como foram tratados  
- Exibir número total de jogos lidos

### Avaliação:
- Implementação e uso das EDs  
- Complexidade Big O

---

## 🌳 Etapa 3 — Implementar BSTs
### Objetivo:
Agrupar seleções por gols usando duas BSTs:

1. **BST ordenada pelo nome da Seleção**
2. **BST ordenada pelo total de gols da Seleção**

### Tarefas:
- Criar `src/bst.py`
- Funções:  
  - `insert(selecao)`  
  - `inorder()` → retorna seleções ordenadas por gols
- Somar os gols por seleção antes de montar a segunda árvore

### Avaliação:
- Implementação correta da árvore  
- Uso lógico da ED  
- Complexidade Big O

---

## 🔃 Etapa 4 — Ordenação
### Objetivo:
Implementar dois algoritmos:

- Um **O(n log n)** (ex.: Merge Sort)  
- Um **O(n²)** (ex.: Bubble Sort)

### Aplicação:
Ordenar seleções por **Pontos**, onde:
- Vitória = 3 pontos  
- Empate = 1 ponto  
- Derrota = 0

### Saídas obrigatórias:
- Top 10 seleções com mais pontos  
- Top 10 seleções com menos pontos

Arquivo: `src/sorting.py`

### Avaliação:
- Comparação dos métodos  
- Complexidade Big O

---

## ⚖️ Etapa 5 — AVL por Pontos
### Objetivo:
Organizar seleções com seus pontos em uma **árvore AVL**.

### Tarefas:
Arquivo `src/avl_points.py`:
- Implementar nó com Seleção + Pontos  
- Implementar rotações:
  - left
  - right
  - left-right
  - right-left
- Usar lista ordenada da etapa 4

### Funções:
- `insert(selecao)`
- `root()`
- `height()`

---

## 📝 Etapa 6 — Gerar `matches_summary.csv`
### Objetivo:
Criar CSV com resumo das partidas.

### Formato: year,country,home_team,away_team,score
Onde:
- score = `"home_score-away_score"`

### Tarefa:
Salvar em:  
`output/matches_summary.csv`

---

## 📊 Etapa 7 — Relatório e Análise Assintótica
### O relatório deve conter:
- Complexidades (inserção, remoção, busca) de todas as estruturas  
- Comparação teórica BST vs AVL  
- Justificativa das escolhas  
- Contribuição dos membros  

