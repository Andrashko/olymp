def gcd (a ,b):
    if a<b:
        a,b = b,a
    if b==0:
        return a
    else:
        return gcd (b, a%b)

class frac:
    def __init__(self, num = 0, denum = 1):
        self.num, self.denum = num, denum
        self.simplify()
    
    def simplify(self):
        g = gcd(self.num, self.denum)
        self.num //= g
        self.denum //= g
    
    def __add__(self, other):
        return frac(self.num*other.denum+other.num*self.denum, self.denum*other.denum)
    
    def __str__(self):
        return f"{self.num}/{self.denum}"

a, b = list(map(int, input().split()))
print (frac (a*b, 2))