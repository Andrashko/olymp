from math import inf


class Node:
    def __init__(self, value, order):
        self.value = value
        self.order = order
        self.left = None
        self.right = None

    def insert(self, node):
        if node.value < self.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

    def count(self):
        res = 1
        order = inf
        if self.left:
            if self.right:
                order = self.right.order
            res += self.left.count_left(order)
        if self.right:
            if self.left:
                order = self.left.order
            res += self.right.count_right(order)
        return res

    def count_left(self, order):
        if self.order>order:
            return 0
        res = 1
        if self.left:
            res += self.left.count_left(order)
        return res

    def count_right(self, order):
        if self.order>order:
            return 0
        res = 1
        if self.right:
            res += self.right.count_right(order)
        return res

    def __str__(self) -> str:
        return f"{self.value} [{self.order}]"

    def __repr__(self) -> str:
        return str(self)


n = int(input())
p = list(map(int, input().split()))

count = 0
for start in range(n):
    tree = Node(p[start], start)
    for i in range(start+1, n):
        tree.insert(Node(p[i], i))
    count += tree.count()

print(count)
