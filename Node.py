from collections import deque

class Node:
    def __init__(self):
        self.cumulativecost = 0
        self.visited = False
        self.parent = ""
        self.children = deque()
        self.name = ""
        self.heuristic = 0
