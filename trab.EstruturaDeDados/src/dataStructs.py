from datetime import datetime
import csv

class Fila:
    def __init__(self):
        self.fila = []
    
    def queue(self, item):
        self.fila.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.fila.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.fila[0]
    
    def is_empty(self):
        return self.fila == []
    
    def size(self):
        return len(self.fila)


class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.filaC = [None] * self.tamanho
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, item):
        if self.is_full():
            print("Fila cheia")
            return
        
        self.rear = (self.rear + 1) % self.tamanho
        self.filaC[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Fila vazia")
            return None
        
        item = self.filaC[self.front]
        self.filaC[self.front] = None
        self.front = (self.front + 1) % self.tamanho
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.tamanho

    def peek(self):
        if self.is_empty():
            return None
        return self.filaC[self.front]

    def print(self):
        print(self.filaC)
    

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, data):
        novo = Node(data)

        if self.head is None:
            self.head = novo
            return
        
        atual = self.head
        while atual.next:
            atual = atual.next
        
        atual.next = novo

    def remover(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        atual = self.head
        while atual.next and atual.next.data != data:
            atual = atual.next
        
        if atual.next:
            atual.next = atual.next.next

    def imprimir(self):
        atual = self.head
        while atual:
            print(atual.data, end=" -> ")
            atual = atual.next
        print("None")


class Pilha:
    def __init__(self):
        self.pilha = []
    
    def push(self, item):
        self.pilha.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.pilha.pop(-1)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.pilha[-1]
    
    def is_empty(self):
        return self.pilha == []
    
    def size(self):
        return len(self.pilha)

class Team:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Team(name={self.name!r}, score={self.score})"


class Match:
    def __init__(
        self,
        date: datetime,
        home_team: Team,
        away_team: Team,
        tournament: str,
        city: str,
        country: str,
        neutral: bool,
    ):
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.tournament = tournament
        self.city = city
        self.country = country
        self.neutral = neutral

    def score_str(self) -> str:
        """Retorna o placar no formato 'home-away', ex: '2-1'."""
        return f"{self.home_team.score}-{self.away_team.score}"
