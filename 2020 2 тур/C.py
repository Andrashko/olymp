x1,y1,x2,y2,x3,y3 = list(map(int, input().split()))

if x1>x2:
    x1,y1,x2,y2 = x2,y2,x1,y1
if x1>x3:
    x1,y1,x3,y3 = x3,y3,x1,y1
if x2>x3:
    x2,y2,x3,y3 = x3,y3,x2,y2

l1 = abs(x2-x1) + abs(y2-y1) - 1
if y1<=y2<=y3 or y1>=y2>=y3:
    l2 = abs(x3-x2) + abs (y3-y2) - 1
elif y1<=y3<=y2 or y1>=y3>=y2:
    l2 = abs(x3-x2) - 1 
else:
    l2 = abs(x3-x2) + abs(y3-y1)-1

print(l1+l2)