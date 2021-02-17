# пряма реалізація бінарного дерева
class Bin_tree_node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def add(self, val):
        if val<self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = Bin_tree_node(val)
        elif val>self.value:
            if self.right:
                self.right.add(val)
            else:
                self.right = Bin_tree_node(val)
    
    def height(self):
        res = 1
        if self.left:
            h = self.left.height()
            res = h + 1 
        if self.right:
            h = self.right.height()
            if h>=res:
                res = h+1 
        return res


n = int(input())
max_h = 0
max_index = -1
for index in range(n):
    tree = list(map(int, input().split()))
    root= Bin_tree_node(tree[1])
    for i in range(2, tree[0]+1):
        root.add(tree[i])
    h=root.height()
    if h>max_h:
        max_h = h
        max_index = index + 1
print(max_index, max_h)