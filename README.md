# Trabalho-Estrutura-de-dados

##Visão Geral
Este documento contém a proposta completa do trabalho. O objetivo é entregar um trabalho que cubra:
Estruturas de dados básicas (pilha, fila, fila circular, lista, lista encadeada, dicionário/objetos)
Manipulação de CSV (leitura e escrita)
Árvores (BST e AVL)
Ordenação (Pelo menos dois Algoritmos, um O(n²) e outro O(nlogn)
Busca linear e busca binária
Análise assintótica (complexidade Big O)
O trabalho foi projetado para execução em 3 horas de aula, em grupos de 5 alunos.



##Dataset
Usar apenas o arquivo results.csv do dataset Global Football Goalscorers Dataset (Kaggle). Todas as tarefas, filtros e arquivos gerados devem partir desse CSV.
date — A data em que a partida internacional de futebol foi disputada.
home_team — A seleção nacional listada como time da casa ou equipe anfitriã da partida.
away_team — A seleção nacional que jogou como visitante ou equipe de fora.
home_score — O número de gols marcados pelo time da casa durante a partida.
away_score — O número de gols marcados pelo time visitante durante a partida.
tournament — O nome da competição ou evento ao qual a partida pertence (World Cup, Friendly, Asian Cup, Copa América)
city — A cidade onde a partida foi realizada.
country — O país no qual a partida ocorreu.
neutral — Indica se a partida foi disputada em um campo neutro.





##Entregáveis Esperados
Código fonte (módulos Python) organizado como indicado.
matches_summary.csv gerado pelo programa (formato descrito abaixo).
Relatório (PDF ou MD) com: arquitetura, explicações de complexidade, prints de execução e contribuição de cada membro.



##Estrutura Recomendada de Arquivos (Pasta do Projeto)
  project/
  ├─ data/
  │  └─ results.csv
  ├─ output/
  │  └─ matches_summary.csv
  ├─ src/
  │  ├─ data_structs.py
  │  ├─ bst.py
  │  ├─ avl.py
  │  ├─ sorting.py
  │  ├─ search.py
  │  └─ main.py
  └─ report.md



##Etapa 1 Modelagem: Classes Match, Team
CAPACIDADE:
Manipular estruturas de dados;
Implementar estruturas de dados;
Selecionar estruturas de dados de forma adequada para a resolução de problemas computacionais; 
Critérios avaliativos
Utilização Lógica das Estruturas;
Desenvolvimento Prático dos Algoritmos;
Objetivo: definir estruturas heterogênea que representa cada partida. (Utilize Class em python)
O que fazer:
Implementar src/data_structs.py:
Classe Team com atributos: name (string) e score (int).
Classe Match com atributos: date (datetime), home_team(Team), away_team(Team), tournament(string), city(string), country(string), neutral(bool).
Método total_goals() que retorna todos os gols da partida.
Método to_list() que retorna uma linha para gravação CSV (ano, país, home_team.name, away_team.name, placar (ex: 2 x 0).
Complexidade dos Algoritmos (Big O)




##Etapa 2  Leitura do CSV e população das estruturas
CAPACIDADE:
Manipular estruturas de dados;
Implementar estruturas de dados;
Manipular arquivos de dados (binários e texto) 
Critérios avaliativos
Utilização Lógica das Estruturas;
Desenvolvimento Prático dos Algoritmos;
Objetivo: ler results.csv, criar Match para cada linha e popular as estruturas básicas.
O que fazer:
Em main.py, abrir data/results.csv com o módulo csv.
Para cada linha válida, criar Match e inserir em uma estrutura de dados:
Escolha uma ED e popule com os objetos de Match (Lista, Fila, Pilha, Lista Encadeada, Fila Circular...)
Filtrar linhas com dados faltantes (explicar no relatório como trataram).
Complexidade dos Algoritmos (Big O)
Saída obrigatória nesta etapa: número total de jogos lidos e gravados.




##Etapa 3 : Implementar BSTs
CAPACIDADE:
Manipular estruturas de dados;
Implementar estruturas de dados;
Critérios avaliativos
Utilização Lógica das Estruturas;
Desenvolvimento Prático dos Algoritmos;
Objetivo: agrupar Seleções (Teams) por Gols Marcados usando uma BST simples (não balanceada).
O que fazer:
Implementar 2 BSTs em src/bst.py, ambas com nós contendo Seleção / Quantidade de Gols, porém, uma ordenada pelo nome de cada Seleção e a outra pela soma de gols de cada Seleção.
Inserção: Inserir na primeira árvore as seleções em ordem alfabética.  Criar uma lista para segunda árvore com as Seleções, comparar string home_team /away_team (lexicográfico). Se país já existe, somar os gols. Com a Lista Pronta, crie a BST com os dados da lista.
Funções: insert(seleção), inorder() (retorna seleções em ordem de gols).
Complexidade dos Algoritmos (Big O)



##Etapa 4  Ordenação
CAPACIDADE:
Manipular estruturas de dados;
Implementar estruturas de dados;
Selecionar e implementar métodos de ordenação. 
Critérios avaliativos
Utilização Lógica das Estruturas;
Desenvolvimento Prático dos Algoritmos;
Objetivo: implementar e comparar dois algoritmos de ordenação.
O que fazer:
src/sorting.py com:
Estável, O(n log n)
O(n²)
Aplicação prática: ordenar lista de Seleções(Teams) por Pontos ()
Cada Vitória = 3 pontos
Cada Empate = 1 ponto
Derrotas não valem pontos
Gerar duas saídas: top 10 Seleções com mais pontos e top 10 com menos pontos.
Complexidade dos Algoritmos (Big O)



##Etapa 5 AVL por Pontos 
CAPACIDADE:
Manipular estruturas de dados;
Implementar estruturas de dados;
Critérios avaliativos
Utilização Lógica das Estruturas;
Desenvolvimento Prático dos Algoritmos;
Objetivo: organizar partidas por Pontos de Cada Seleção (Team) numa árvore balanceada AVL, utilizando a lista ordenada da Etapa 5.

O que fazer:
Implementar src/avl_points.py com nó Seleção/Pontos.
Implementar rotações (left, right, left-right, right-left) e atualização de altura.
Usar a Lista com todas as Seleções e seus respectivos Pontos já ordenada da Etapa 5
Funções: insert(seleção), root() que retorna a raiz da árvore, height() retorna a altura da árvore.



##Etapa 6 Geração do CSV matches_summary.csv 
CAPACIDADE:
Manipular arquivos de dados (binários e texto); 
Selecionar e implementar métodos de pesquisa; 
Critérios avaliativos
Utilização Lógica das Estruturas;
Desenvolvimento Prático dos Algoritmos;
Objetivo: salvar resumo com campos essenciais.
Formato do CSV de saída:
year,country,home_team,away_team,score (score = "home_score-away_score")
O que fazer: ao final, gravar todos os Match processados em output/matches_summary.csv.



##Etapa 7 Relatório e Análise Assintótica
CAPACIDADE:
Manipular estruturas de dados;
Implementar estruturas de dados;
Critérios avaliativos
Desenvolvimento lógico e Teórico;
Cálculos e Análises das Complexidades de todas as Etapas;
Objetivo: descrever complexidades, justificar escolhas e assinar contribuições.
O que deve conter:
Complexidade das operações (inserção, remoção, busca) para cada estrutura implementada.
Comparação teórica BST vs AVL.

