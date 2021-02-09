#НСД

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
        c = self.num // self.denum
        d = self.num % self.denum
        if d == 0:
            return f"{c}"
        elif c == 0:
            return f"{d}/{self.denum}"
        else:
            return f"{c} {d}/{self.denum}"

f1 , f2 = input().split("+")
c1, d1 = list(map(int, f1.split("/")))
c2, d2 = list(map(int, f2.split("/")))
print(frac(c1, d1)+frac(c2, d2))