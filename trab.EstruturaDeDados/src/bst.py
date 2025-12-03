import csv


class Node:
    def __init__(self, selecao, gols):
        self.selecao = selecao  
        self.gols = gols         
        self.left = None
        self.right = None


class BST:
    def __init__(self, criterio='nome'):
        self.root = None
        self.criterio = criterio

    def insert(self, selecao, gols):
        new_node = Node(selecao, gols)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_rec(self.root, new_node)

    def _insert_rec(self, node, new_node):
        if self.criterio == 'nome':
            key_node = node.selecao
            key_new = new_node.selecao
        elif self.criterio == 'gols':
            key_node = node.gols
            key_new = new_node.gols
        else:
            raise ValueError("Critério inválido")

        if key_new < key_node:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_rec(node.left, new_node)
        elif key_new > key_node:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_rec(node.right, new_node)
            if self.criterio == 'nome':
                node.gols += new_node.gols

    def inorder(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node, result):
        if node:
            self._inorder_rec(node.left, result)
            result.append((node.selecao, node.gols))
            self._inorder_rec(node.right, result)


bst_nome = BST(criterio='nome')

with open("data/results.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for linha in reader:
        home_team = linha[1]
        away_team = linha[2]
        home_score = int(linha[3])
        away_score = int(linha[4])

        bst_nome.insert(home_team, home_score)
        bst_nome.insert(away_team, away_score)


gols_por_selecao = {}

with open("data/results.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    for linha in reader:
        home_team = linha[1]
        away_team = linha[2]
        home_score = int(linha[3])
        away_score = int(linha[4])

        gols_por_selecao[home_team] = gols_por_selecao.get(home_team, 0) + home_score
        gols_por_selecao[away_team] = gols_por_selecao.get(away_team, 0) + away_score

bst_gols = BST(criterio='gols')
for selecao, total_gols in gols_por_selecao.items():
    bst_gols.insert(selecao, total_gols)

#Por Nome
print("BST por Nome (in-order):")
for selecao, gols in bst_nome.inorder():
    print(f"{selecao}: {gols} gols")

#Por gols
print("\nBST por Gols (in-order):")
for selecao, gols in bst_gols.inorder():
    print(f"{selecao}: {gols} gols")

