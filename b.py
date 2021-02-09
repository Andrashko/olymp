n, m = list(map(int, input().split()))
x,y = list(map(int, input().split()))
k = int(input())

x-=1
y-=1
a = [["." for i in range(m)] for j in range(n)]
a[x][y] = "*"
for _ in range(k):
    dir, l = input().split()
    l = int(l)
    for s in range(l):
        if dir == "U":
            x-=1
        elif dir == "D":
            x+=1
        elif dir == "L":
            y-=1
        elif dir == "R":
            y+=1
        a[x][y] = "*"

for i in range(n):
    for j in range(m):
        print(a[i][j], end="")
    print()