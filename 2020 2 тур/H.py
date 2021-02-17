n = int(input())
balls = list(map(int, input().split()))
arrows = [0]*1000001

for i in range(n):
    if arrows[balls[i]]>0:
        arrows[balls[i]] -= 1    
    arrows[balls[i]-1] += 1
print(sum(arrows))   
