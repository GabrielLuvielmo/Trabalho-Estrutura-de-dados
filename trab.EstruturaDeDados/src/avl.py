
class AVLNode:
    def __init__(self, team_name, points):
        self.team_name = team_name
        self.points = points
        self.left = None   # filho esquerdo
        self.right = None  # filho direito
        self.height = 1    # altura do nó (folha = 1)

    def __repr__(self):
        return f"AVLNode({self.team_name!r}, {self.points}, h={self.height})"


class AVLPointsTree:
    def __init__(self):
        self._root = None

    # ----------------- Funções auxiliares -----------------

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(
            self._get_height(node.left),
            self._get_height(node.right),
        )

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # ----------------- Rotações -----------------

    def _rotate_right(self, y):
        r"""
            y                x
           / \              / \
          x   T3   ->      T1  y
         / \                  / \
        T1  T2               T2  T3
        """
        x = y.left
        T2 = x.right

     
        x.right = y
        y.left = T2

        
        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, y):
        r"""
           y                 x
          / \               / \
         T1  x     ->      y  T3
            / \           / \
           T2 T3         T1 T2
        """
        x = y.right
        T2 = x.left

     
        x.left = y
        y.right = T2

      
        self._update_height(y)
        self._update_height(x)

        return x

    # ----------------- Inserção -----------------

    def insert(self, team_name, points):
        """
        Insere uma seleção na AVL, organizada por pontos.
        Empate em pontos é desempate por nome (ordem alfabética).
        """
        self._root = self._insert(self._root, team_name, points)

    def _insert(self, node, team_name, points):
     
        if node is None:
            return AVLNode(team_name, points)

        if points < node.points or (points == node.points and team_name < node.team_name):
            node.left = self._insert(node.left, team_name, points)
        elif points > node.points or (points == node.points and team_name > node.team_name):
            node.right = self._insert(node.right, team_name, points)
        else:
         
            return node

      
        self._update_height(node)

       
        balance = self._get_balance(node)

        # Casos de desbalanceamento:

        # LL (esquerda-esquerda)
        if balance > 1 and (points < node.left.points or
                            (points == node.left.points and team_name < node.left.team_name)):
            return self._rotate_right(node)

        # RR (direita-direita)
        if balance < -1 and (points > node.right.points or
                             (points == node.right.points and team_name > node.right.team_name)):
            return self._rotate_left(node)

        # LR (esquerda-direita)
        if balance > 1 and (points > node.left.points or
                            (points == node.left.points and team_name > node.left.team_name)):
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # RL (direita-esquerda)
        if balance < -1 and (points < node.right.points or
                             (points == node.right.points and team_name < node.right.team_name)):
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # ----------------- Funções pedidas na etapa -----------------

    def root(self):
        """Retorna a raiz da árvore."""
        return self._root

    def height(self):
        """Retorna a altura da árvore."""
        return self._get_height(self._root)

    def in_order(self):
        """
        Retorna lista em-ordem (do menor para o maior número de pontos),
        no formato [(team_name, points), ...]
        """
        resultado = []

        def _in_order(node):
            if node is None:
                return
            _in_order(node.left)
            resultado.append((node.team_name, node.points))
            _in_order(node.right)

        _in_order(self._root)
        return resultado

import csv

# Dicionário para armazenar pontos por seleção
pontos_por_selecao = {}

with open("data/results.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)  # pula cabeçalho
    for linha in reader:
        home_team = linha[1]
        away_team = linha[2]
        home_score = int(linha[3])
        away_score = int(linha[4])

        # Exemplo: soma de gols como "pontos"
        pontos_por_selecao[home_team] = pontos_por_selecao.get(home_team, 0) + home_score
        pontos_por_selecao[away_team] = pontos_por_selecao.get(away_team, 0) + away_score

avl = AVLPointsTree()

for selecao, pontos in pontos_por_selecao.items():
    avl.insert(selecao, pontos)

print("Raiz da árvore:", avl.root())
print("Altura da árvore:", avl.height())
print("Seleções em ordem crescente de pontos:")
for team, points in avl.in_order():
    print(f"{team}: {points} pontos")
