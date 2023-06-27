from math import sqrt


def max_divisor(number):
    return int(sqrt(number))+1


def is_prime(number):
    for divisor in range(2, max_divisor(number)):
        if number % divisor == 0:
            return False
    return True


number = int(input())
if is_prime(number):
    print(1)
else:
    print(0)
