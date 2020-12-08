prime_list = []

n = int(input("pls enter a number "))
# importing time module
import time
# importing math module for sqrt function
import math
# checking for prime
def is_prime(n):
   if n <= 1:
      return False
   else:
      # iterating loop till square root of n
      for i in range(2, int(math.sqrt(n)) + 1):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
      prime_list.append(n)
      print(n)
      return True
# starting time
start_time = time.time()
primes = 0
for i in range(n):
   if is_prime(i):
      primes += 1
print(f'Total primes in the range {primes}')
# ending time
end_time = time.time()
print(f'Execution time: {end_time - start_time}')
print("the largest prime is " + str(prime_list[-1]))
    