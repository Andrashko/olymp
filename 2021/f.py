from copy import copy

class DataStructure:
    def __init__(self, min, max, count=1):
        self.min = min
        self.max = max
        self.count = count

    def __str__(self) -> str:
        return f"({self.min}, {self.max}) -> {self.count}"

    def __repr__(self) -> str:
        return str(self)


n = int(input())
p = list(map(int, input().split()))

matrix = []

for end in range(n):
    row = []
    
    for start in range(end):
        f_start_end = copy(matrix[end-1][start])

        if f_start_end.min > p[end]:
            f_start_end.min = p[end]
            f_start_end.count += 1
        if f_start_end.max < p[end]:
            f_start_end.max = p[end]
            f_start_end.count += 1

        row.append(f_start_end)

    row.append(DataStructure(p[end], p[end]))

    matrix.append(row)

print(sum(map(lambda f: f.count, matrix[n-1])))
