class Process:
    def __init__(self, pid, vruntime):
        self.pid = pid
        self.vruntime = vruntime

class Node:
    def __init__(self, process, parent=None):
        self.process = process
        self.left = None
        self.right = None
        self.parent = parent
        self.color = "RED"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, process):
        if self.root is None:
            self.root = Node(process)
        else:
            self._insert_recursive(self.root, process)

    def _insert_recursive(self, current, process):
        if process.vruntime < current.process.vruntime:
            if current.left is None:
                current.left = Node(process, current)
            else:
                self._insert_recursive(current.left, process)
        else:
            if current.right is None:
                current.right = Node(process, current)
            else:
                self._insert_recursive(current.right, process)

    def search(self, vruntime):
        return self._search_recursive(self.root, vruntime, 0)

    def _search_recursive(self, current, vruntime, steps):
        if current is None:
            return None, steps
        
        if vruntime == current.process.vruntime:
            return current, steps
        
        steps += 1
        if vruntime < current.process.vruntime:
            return self._search_recursive(current.left, vruntime, steps)
        else:
            return self._search_recursive(current.right, vruntime, steps)

class SplayTree(BST):
    def splay(self, node):
        pass

class RedBlackTree(BST):
    def check_rules(self, node):
        pass
