n = int(input())
a = list(map(int, input().split()))
a.sort()
max = 0
for i in range(1, n):
    d = a[i-1]*a[i] / abs(a[i-1]-a[i])
    if d > max:
        max = d
print(max)
