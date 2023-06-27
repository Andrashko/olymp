n = int(input())
numbers_count = [0]*101
numbers_string = input()
for number in numbers_string.split(" "):
    numbers_count[int(number)] += 1
squares_count = 0
for count in numbers_count:
    squares_count += count // 4
print(squares_count)
