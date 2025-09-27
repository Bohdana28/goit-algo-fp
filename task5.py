import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color          # колір вузла
        self.id = str(uuid.uuid4()) # унікальний id для графа

# Генерація кольорів
def get_color_gradient(n):
    """
    Повертає список n кольорів від темного до світлого через палітру
    """
    colors = []
    for i in range(n):
        # використовуємо RGB від темного синьо-червоного до світлого
        r = int(50 + (205 * i / max(n-1,1)))
        g = int(50 + (155 * i / max(n-1,1)))
        b = int(150 +(105 * i / max(n-1,1)))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors

# BFS - обхід у ширину
def bfs_coloring(root):
    queue = deque([root])
    nodes_in_order = []

    while queue:
        node = queue.popleft()
        nodes_in_order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    colors = get_color_gradient(len(nodes_in_order))
    for node, color in zip(nodes_in_order, colors):
        node.color = color

# DFS - обхід у глибину
def dfs_coloring(root):
    stack = [root]
    nodes_in_order = []

    while stack:
        node = stack.pop()
        nodes_in_order.append(node)
        # Спочатку додаємо праву, щоб ліва оброблялась першою
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    colors = get_color_gradient(len(nodes_in_order))
    for node, color in zip(nodes_in_order, colors):
        node.color = color

# Додавання вузлів та ребер у граф
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Візуалізація дерева
def draw_tree(tree_root, title="Бінарне дерево"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title, fontsize=16)
    plt.show()

# Приклад використання
if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Візуалізація BFS
    bfs_coloring(root)
    draw_tree(root, title="BFS - Обхід у ширину")

    # Візуалізація DFS
    dfs_coloring(root)
    draw_tree(root, title="DFS - Обхід у глибину")
