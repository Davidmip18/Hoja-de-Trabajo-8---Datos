from graphviz import Digraph
from trees import BST, SplayTree, RedBlackTree, Process

def generate_representative_graphviz(tree, filename="bst_secuencial"):
    dot = Digraph(strict=True)
    if tree.root is None:
        return dot

    node_count = 0
    def add_nodes_edges(node):
        nonlocal node_count
        if node_count >= 50:
            return
        
        dot.node(str(node.process.pid), f"PID: {node.process.pid}\nVR: {node.process.vruntime}")
        node_count += 1
        
        if node.left and node_count < 50:
            dot.edge(str(node.process.pid), str(node.left.process.pid))
            add_nodes_edges(node.left)
        if node.right and node_count < 50:
            dot.edge(str(node.process.pid), str(node.right.process.pid))
            add_nodes_edges(node.right)

    add_nodes_edges(tree.root)
    dot.render(filename, format='png', cleanup=True)

bst = BST()
splay_tree = SplayTree()
rb_tree = RedBlackTree()

procesos = []
for i in range(1, 1001):
    p = Process(i, i)
    procesos.append(p)
    bst.insert(p)
    splay_tree.insert(p)
    rb_tree.insert(p)

generate_representative_graphviz(bst)

nodo_bst, pasos_bst = bst.search(1000)
nodo_splay, pasos_splay = splay_tree.search(1000)
nodo_rb, pasos_rb = rb_tree.search(1000)

print(f"Iteraciones BST para proceso 1000: {pasos_bst}")
print(f"Iteraciones Splay Tree para proceso 1000: {pasos_splay}")
print(f"Iteraciones Red-Black Tree para proceso 1000: {pasos_rb}")
