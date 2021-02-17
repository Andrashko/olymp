# count = 1000000
# is_prime = [True]*count
# is_prime [0] , is_prime[1] = False, False
# primes = []

# number = 2
# while number < count:
#     if is_prime[number]:
#         primes.append(number)
#         for np in range (2*number, count, number):
#             is_prime[np] = False
#     number +=1 

# def isPrime (number):
#     for p in primes:
#         if p>= number:
#             break
#         if number%p == 0:
#             return False
#     return True

# import random
 
# # Iterative Function to calculate 
# # (a^n)%p in O(logy) 
# def power(a, n, p):
     
#     # Initialize result 
#     res = 1
     
#     # Update 'a' if 'a' >= p 
#     a = a % p  
     
#     while n > 0:
         
#         # If n is odd, multiply 
#         # 'a' with result 
#         if n % 2:
#             res = (res * a) % p
#             n = n - 1
#         else:
#             a = (a ** 2) % p
             
#             # n must be even now 
#             n = n // 2
             
#     return res % p
     
# # If n is prime, then always returns true,
# # If n is composite than returns false with
# # high probability Higher value of k increases
# # probability of correct result
# def isPrime(n, k):
     
#     # Corner cases
#     if n == 1 or n == 4:
#         return False
#     elif n == 2 or n == 3:
#         return True
     
#     # Try k times 
#     else:
#         for i in range(k):
             
#             # Pick a random number 
#             # in [2..n-2]      
#             # Above corner cases make 
#             # sure that n > 4 
#             a = random.randint(2, n - 2)
             
#             # Fermat's little theorem 
#             if power(a, n - 1, n) != 1:
#                 return False
                 
#     return True
             

a, b=list(map(int, input().split()))

k = 0
for number in range(a, b+1):
    if number%2 == 0 or isPrime(number-2):
        k += 1
print(k)
