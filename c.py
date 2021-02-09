def findMin(V):
    deno = [7,8]
    n = len(deno)
    ans = []
    i = n - 1
    k = V
    while(i >= 0):
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
        i -= 1
    res = sum(ans)
    if res == k:
        print("YES")
    else:
        print("NO")
        
n = int(input())
findMin(n)
