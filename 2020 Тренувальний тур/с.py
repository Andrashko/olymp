# обхід графа в глибину, поинаємо із вершин де нема вихідних дуг
n, m = list(map(int, input().split()))


class Node:
    def __init__(self, val):
        self.val = val
        self.inv = []
        self.outv = []
        self.status = "Not visited"

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"(val:{self.val} in:{self.inv} out:{self.outv} staus:{self.status})"


graf = [Node(i+1) for i in range(n)]
for _ in range(m):
    begin, end = list(map(int, input().split()))
    graf[begin-1].outv.append(end-1)
    graf[end-1].inv.append(begin-1)


def depth(graf, current):
    graf[current].status = "In process"
    way = ""
    for node in graf[current].inv:
        if graf[node].status == "In process":
            raise Exception("Cicle")
        if graf[node].status == "Not visited":
            way += depth(graf, node)
    graf[current].status = "Visited"
    return way+" "+str(graf[current].val)


try:
    way = ""
    for node in range(n):
        if len(graf[node].outv) == 0 and graf[node].status == "Not visited":
            way += depth(graf, node)
    if all(map(lambda node: node.status == "Visited", graf)):
        print("Yes")
        print(way)
    else:
        print("No")
except:
    print("No")
