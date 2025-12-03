# ETAPA 7 — RELATÓRIO E ANÁLISE ASSINTÓTICA (Big O)

## 1. Introdução

Esta etapa tem como objetivo apresentar a análise assintótica (Big O) de todas as estruturas de dados e algoritmos implementados no projeto, bem como uma comparação teórica entre a BST e a AVL, justificando as escolhas realizadas ao longo do desenvolvimento.

A notação Big O é utilizada para expressar o comportamento de crescimento do tempo de execução dos algoritmos em função do tamanho da entrada (n).

---

## 2. Estruturas de Dados Utilizadas e Suas Complexidades

### 2.1 Lista (List)

Utilizada para armazenar todos os objetos da classe `Match`.

| Operação | Complexidade |
|----------|--------------|
| Inserção no final | O(1) |
| Busca | O(n) |
| Remoção | O(n) |

Justificativa: a lista foi utilizada por sua simplicidade e eficiência na leitura sequencial do arquivo CSV.

---

### 2.2 Dicionário (Dict)

Utilizado para agrupar seleções, gols e pontos.

| Operação | Complexidade |
|----------|--------------|
| Inserção | O(1) |
| Busca | O(1) |
| Remoção | O(1) |

Justificativa: permite acesso direto por chave, garantindo rapidez no cálculo dos pontos.

---

### 2.3 Pilha, Fila e Fila Circular

| Estrutura | Inserção | Remoção | Busca |
|----------|----------|----------|--------|
| Pilha | O(1) | O(1) | O(n) |
| Fila | O(1) | O(1) | O(n) |
| Fila Circular | O(1) | O(1) | O(n) |

---

## 3. Árvores

### 3.1 BST (Árvore Binária de Busca)

| Operação | Melhor Caso | Pior Caso |
|----------|-------------|-----------|
| Inserção | O(log n) | O(n) |
| Busca | O(log n) | O(n) |
| Remoção | O(log n) | O(n) |

A BST foi utilizada para organizar as seleções por nome e por gols. Por não ser balanceada, seu pior caso ocorre quando se torna semelhante a uma lista.

---

### 3.2 AVL (Árvore Balanceada)

| Operação | Complexidade |
|----------|--------------|
| Inserção | O(log n) |
| Busca | O(log n) |
| Remoção | O(log n) |

A AVL garante balanceamento automático através de rotações, mantendo sempre a altura da árvore como O(log n), garantindo desempenho constante.

---

## 4. Algoritmos de Ordenação

### 4.1 Insertion Sort — O(n²)

O algoritmo Insertion Sort apresenta dois laços aninhados, o que caracteriza complexidade quadrática.

| Caso | Complexidade |
|------|--------------|
| Melhor | O(n) |
| Médio | O(n²) |
| Pior | O(n²) |

Foi utilizado como algoritmo menos eficiente para fins comparativos.

---

### 4.2 Merge Sort — O(n log n)

O algoritmo Merge Sort utiliza a técnica de divisão e conquista.

| Caso | Complexidade |
|------|--------------|
| Melhor | O(n log n) |
| Médio | O(n log n) |
| Pior | O(n log n) |

Foi utilizado para ordenação eficiente das seleções por pontos.

---

## 5. Algoritmos de Busca

### 5.1 Busca Linear

| Complexidade |
|--------------|
| O(n) |

Percorre todos os elementos até encontrar o valor desejado.

---

### 5.2 Busca Binária

| Complexidade |
|--------------|
| O(log n) |

Utilizada apenas em listas ordenadas, dividindo o vetor ao meio a cada iteração.

---

## 6. Aplicação Prática no Projeto

- As partidas foram armazenadas em listas.
- As seleções e suas estatísticas foram organizadas em dicionários.
- As BSTs foram utilizadas para organização por nome e por gols.
- A AVL foi utilizada para organizar seleções por pontos.
- Dois algoritmos de ordenação foram implementados: um O(n²) e outro O(n log n).

---

## 7. Comparação Teórica: BST vs AVL

| Característica | BST | AVL |
|----------------|-----|-----|
| Balanceamento | Não automático | Automático |
| Altura | Pode ser O(n) | Sempre O(log n) |
| Inserção | Mais simples | Mais custosa |
| Busca | Pode degradar | Sempre eficiente |
| Rotação | Não possui | Possui |
| Uso de memória | Menor | Maior |

Conclusão: a BST é mais simples de implementar, porém pode perder desempenho em casos degenerados. A AVL, embora mais complexa, garante alto desempenho em todas as operações.

---

## 8. Contribuição dos Integrantes

- Gabriel Luvielmo: Leitura do CSV e implementação das classes.
- Vitor Kurth: Implementação das Bst's
- Pedro Zanette: Algoritmos de ordenação e busca.
- Arthur Kremer: Implementação da AVL.
- Guilherme Santos Oliveira: Relatório e geração do HTML.

---

## 9. Conclusão Final

O projeto permitiu aplicar na prática os conceitos de estruturas de dados, algoritmos de ordenação, árvores binárias e análise assintótica. A escolha das estruturas foi feita visando desempenho, organização e clareza dos dados.

---
