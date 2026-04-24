import random
import matplotlib.pyplot as plt
from graphviz import Digraph
from trees import BST, SplayTree, RedBlackTree, Process

def generate_graphviz(tree, filename="bst_1000_procesos"):
    dot = Digraph(strict=True)
    
    if tree.root is None:
        return dot

    def add_nodes_edges(node):
        dot.node(str(node.process.pid), f"PID: {node.process.pid}\nVR: {node.process.vruntime}")
        if node.left:
            dot.edge(str(node.process.pid), str(node.left.process.pid))
            add_nodes_edges(node.left)
        if node.right:
            dot.edge(str(node.process.pid), str(node.right.process.pid))
            add_nodes_edges(node.right)

    add_nodes_edges(tree.root)
    dot.render(filename, format='png', cleanup=True)

bst = BST()
splay_tree = SplayTree()
rb_tree = RedBlackTree()
procesos_generados = []

for i in range(1, 1001):
    vruntime = random.randint(1, 50000)
    p = Process(i, vruntime)
    procesos_generados.append(p)
    bst.insert(p)
    splay_tree.insert(p)
    rb_tree.insert(p)

generate_graphviz(bst)

procesos_a_buscar = random.sample(procesos_generados, 100)

iteraciones_bst = []
iteraciones_splay = []
iteraciones_rb = []
nombres_procesos = []

for idx, p in enumerate(procesos_a_buscar):
    _, pasos_bst = bst.search(p.vruntime)
    _, pasos_splay = splay_tree.search(p.vruntime)
    _, pasos_rb = rb_tree.search(p.vruntime)
    
    iteraciones_bst.append(pasos_bst)
    iteraciones_splay.append(pasos_splay)
    iteraciones_rb.append(pasos_rb)
    nombres_procesos.append(str(idx + 1))

promedio_bst = sum(iteraciones_bst) / len(iteraciones_bst)
promedio_splay = sum(iteraciones_splay) / len(iteraciones_splay)
promedio_rb = sum(iteraciones_rb) / len(iteraciones_rb)

print(f"Promedio de iteraciones con el BST: {promedio_bst:.2f}")
print(f"Promedio de iteraciones con el Splay Tree: {promedio_splay:.2f}")
print(f"Promedio de iteraciones con el Red-Black Tree: {promedio_rb:.2f}")

plt.figure(figsize=(14, 6))
plt.plot(nombres_procesos, iteraciones_bst, marker='o', linestyle='-', color='blue', label='BST')
plt.plot(nombres_procesos, iteraciones_splay, marker='s', linestyle='-', color='green', label='Splay Tree')
plt.plot(nombres_procesos, iteraciones_rb, marker='^', linestyle='-', color='red', label='Red-Black Tree')

plt.title('Escenario A: Búsqueda de 100 procesos aleatorios')
plt.xlabel('Proceso Buscado (Índice 1-100)')
plt.ylabel('Cantidad de Iteraciones')
plt.xticks(rotation=90, fontsize=8)
plt.legend()
plt.tight_layout()
plt.show()
