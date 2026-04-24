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
        new_node = Node(process)
        if self.root is None:
            self.root = new_node
            return new_node
        
        current = self.root
        while True:
            if process.vruntime < current.process.vruntime:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return new_node
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return new_node
                current = current.right

    def search(self, vruntime):
        current = self.root
        steps = 0
        while current is not None:
            if vruntime == current.process.vruntime:
                return current, steps
            steps += 1
            if vruntime < current.process.vruntime:
                current = current.left
            else:
                current = current.right
        return None, steps

class SplayTree(BST):
    def _left_rotate(self, x):
        y = x.right
        if y is not None:
            x.right = y.left
            if y.left is not None:
                y.left.parent = x
            y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        if y is not None:
            y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        if y is not None:
            x.left = y.right
            if y.right is not None:
                y.right.parent = x
            y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        if y is not None:
            y.right = x
        x.parent = y

    def splay(self, n):
        while n.parent is not None:
            if n.parent.parent is None:
                if n == n.parent.left:
                    self._right_rotate(n.parent)
                else:
                    self._left_rotate(n.parent)
            elif n == n.parent.left and n.parent == n.parent.parent.left:
                self._right_rotate(n.parent.parent)
                self._right_rotate(n.parent)
            elif n == n.parent.right and n.parent == n.parent.parent.right:
                self._left_rotate(n.parent.parent)
                self._left_rotate(n.parent)
            elif n == n.parent.right and n.parent == n.parent.parent.left:
                self._left_rotate(n.parent)
                self._right_rotate(n.parent)
            else:
                self._right_rotate(n.parent)
                self._left_rotate(n.parent)

    def insert(self, process):
        new_node = super().insert(process)
        self.splay(new_node)
        return new_node

    def search(self, vruntime):
        node, steps = super().search(vruntime)
        if node is not None:
            self.splay(node)
        return node, steps

class RedBlackTree(BST):
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, process):
        new_node = Node(process)
        new_node.color = "RED"
        if self.root is None:
            self.root = new_node
            self.root.color = "BLACK"
            return new_node
        
        current = self.root
        while True:
            if process.vruntime < current.process.vruntime:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right

        self._fix_insert(new_node)
        return new_node

    def _fix_insert(self, k):
            while k.parent is not None and k.parent.color == "RED":
                if k.parent == k.parent.parent.left:
                    u = k.parent.parent.right
                    if u is not None and u.color == "RED":
                        k.parent.color = "BLACK"
                        u.color = "BLACK"
                        k.parent.parent.color = "RED"
                        k = k.parent.parent
                    else:
                        if k == k.parent.right:
                            k = k.parent
                            self._left_rotate(k)
                        k.parent.color = "BLACK"
                        k.parent.parent.color = "RED"
                        self._right_rotate(k.parent.parent)
                else:
                    u = k.parent.parent.left
                    if u is not None and u.color == "RED":
                        k.parent.color = "BLACK"
                        u.color = "BLACK"
                        k.parent.parent.color = "RED"
                        k = k.parent.parent
                    else:
                        if k == k.parent.left:
                            k = k.parent
                            self._right_rotate(k)
                        k.parent.color = "BLACK"
                        k.parent.parent.color = "RED"
                        self._left_rotate(k.parent.parent)
            self.root.color = "BLACK"
