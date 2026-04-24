import random
import matplotlib.pyplot as plt
<<<<<<< HEAD
from trees import BST, SplayTree, RedBlackTree, Process

bst = BST()
splay_tree = SplayTree()
rb_tree = RedBlackTree()
=======
from trees import BST, SplayTree, Process

bst = BST()
splay_tree = SplayTree()
>>>>>>> 48569a9ad15bc27257f15b74c6038332f9cf90c1
procesos = []

for i in range(1, 1001):
    vruntime = random.randint(1, 50000)
    p = Process(i, vruntime)
    procesos.append(p)
    bst.insert(p)
    splay_tree.insert(p)
<<<<<<< HEAD
    rb_tree.insert(p)
=======
>>>>>>> 48569a9ad15bc27257f15b74c6038332f9cf90c1

proceso_frecuente = random.choice(procesos)

iteraciones_bst = []
iteraciones_splay = []
<<<<<<< HEAD
iteraciones_rb = []
=======
>>>>>>> 48569a9ad15bc27257f15b74c6038332f9cf90c1
busquedas = list(range(1, 51))

for _ in range(50):
    _, pasos_bst = bst.search(proceso_frecuente.vruntime)
    _, pasos_splay = splay_tree.search(proceso_frecuente.vruntime)
<<<<<<< HEAD
    _, pasos_rb = rb_tree.search(proceso_frecuente.vruntime)
    
    iteraciones_bst.append(pasos_bst)
    iteraciones_splay.append(pasos_splay)
    iteraciones_rb.append(pasos_rb)

promedio_bst = sum(iteraciones_bst) / len(iteraciones_bst)
promedio_splay = sum(iteraciones_splay) / len(iteraciones_splay)
promedio_rb = sum(iteraciones_rb) / len(iteraciones_rb)
=======
    
    iteraciones_bst.append(pasos_bst)
    iteraciones_splay.append(pasos_splay)

promedio_bst = sum(iteraciones_bst) / len(iteraciones_bst)
promedio_splay = sum(iteraciones_splay) / len(iteraciones_splay)
>>>>>>> 48569a9ad15bc27257f15b74c6038332f9cf90c1

print(f"Iteraciones promedio (50 búsquedas del mismo proceso):")
print(f"En el BST: {promedio_bst:.2f}")
print(f"En el Splay Tree: {promedio_splay:.2f}")
<<<<<<< HEAD
print(f"En el Red-Black Tree: {promedio_rb:.2f}")
=======
>>>>>>> 48569a9ad15bc27257f15b74c6038332f9cf90c1

plt.figure(figsize=(10, 6))
plt.plot(busquedas, iteraciones_bst, marker='o', linestyle='-', color='blue', label='BST')
plt.plot(busquedas, iteraciones_splay, marker='s', linestyle='-', color='green', label='Splay Tree')
<<<<<<< HEAD
plt.plot(busquedas, iteraciones_rb, marker='^', linestyle='-', color='red', label='Red-Black Tree')
=======
>>>>>>> 48569a9ad15bc27257f15b74c6038332f9cf90c1

plt.title('Escenario C: Búsqueda del mismo proceso 50 veces seguidas')
plt.xlabel('Número de Búsqueda (1 a 50)')
plt.ylabel('Cantidad de Iteraciones')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
