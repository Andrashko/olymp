n, M = list(map(int, input().split()))
a = list(map(int, input().split()))
edges = []
for i in range(n):
    for j in range(n):
        edges.append([(a[i]+a[j]) % M, j, i])
edges.sort()
comp = [i for i in range(n)]
ans = 0
for weight, start, end in edges:
    if comp[start] != comp[end]:
        ans += weight
        a = comp[start]
        b = comp[end]
        for i in range(n):
            if comp[i] == b:
                comp[i] = a

print(ans)
