# 1. 

import time
import tracemalloc


n = int(input("Enter a number :- "))

start_time =  time.time()
tracemalloc.start()
if n < 0:
    print("Please Enter non negative integer")
else:
    prod = 1
    for i in range(2, n+1):
       prod = prod*i
    print(f"The factorial of {n} is : {prod}")

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")


#2.

import time
import tracemalloc

n = int(input("Enter a number :- "))

start_time =  time.time()
tracemalloc.start()

temp = n
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")


#3
import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

n = int(input("Enter a number :- "))

total = 0
count = 0
num = abs(n)
while num > 0:
    digit = num % 10
    total += digit
    count += 1
    num //= 10
if count == 0:
    mean = 0
else:
    mean = total / count

print(f"The mean of the digits is: {mean}") 

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

print("")
print("")

#4

print("4.")

n = int(input("Enter a number :- "))

num = abs(n)
while num >= 10:
    digit_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10
    num = digit_sum

digital_root = num
print(f"Desird output is: {digital_root}")  

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

print("")
print("")

#5

print("5.")

n = int(input("Enter a number :- "))

proper_divisors_sum = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        proper_divisors_sum += i

is_abundant = proper_divisors_sum > n
print(f"Output of the code is: {is_abundant}")  

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

#6 .

import time
import tracemalloc


n = int(input("Enter a number :- "))

start_time =  time.time()
tracemalloc.start()
if n < 0:
    print("Please Enter non negative integer")
else:
    prod = 1
    for i in range(2, n+1):
       prod = prod*i
    print(f"The factorial of {n} is : {prod}")

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")


#7 . 

n = int(input("Enter a number :- "))

temp = n
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")


#8 .


n = int(input("Enter a number :- "))

total = 0
count = 0
num = abs(n)
while num > 0:
    digit = num % 10
    total += digit
    count += 1
    num //= 10
if count == 0:
    mean = 0
else:
    mean = total / count

print(f"The mean of the digits is: {mean}") 

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

print("")
print("")

#9.)

n = int(input("Enter a number :- "))

num = abs(n)
while num >= 10:
    digit_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10
    num = digit_sum

digital_root = num
print(f"Desird output is: {digital_root}")  

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")


# 10.)


n = int(input("Enter a number :- "))

proper_divisors_sum = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        proper_divisors_sum += i

is_abundant = proper_divisors_sum > n
print(f"Output of the code is: {is_abundant}")  

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

# 11.)

def is_deficient(n):
  if n <= 0:
    return False

  sum_of_proper_divisors = 0

  for i in range(1, n // 2 + 1):
    if n % i == 0:
      sum_of_proper_divisors += i

  return sum_of_proper_divisors < n

print(f"Is 8 deficient? {is_deficient(8)}")
print(f"Is 12 deficient? {is_deficient(12)}")
print(f"Is 21 deficient? {is_deficient(21)}")

#12.)

def is_harshad(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    sum_of_digits = 0
    temp_n = n
    while temp_n > 0:
        sum_of_digits += temp_n % 10
        temp_n //= 10

    return n % sum_of_digits == 0

print(is_harshad(4563897))
print(is_harshad(7698707))
print(is_harshad(5658))

#13.)

def is_automorphic(n):
   
    if n < 0:
        n = -n # Automorphic property applies to the absolute value 
    square = n * n
    
    # Convert both the number and its square to strings for easy comparison of endings
    str_n = str(n)
    str_square = str(square)

    return str_square.endswith(str_n)

print(f"Is 5 automorphic? {is_automorphic(5)}")
print(f"Is 6 automorphic? {is_automorphic(6)}")
print(f"Is 25 automorphic? {is_automorphic(25)}")
print(f"Is 76 automorphic? {is_automorphic(76)}")
print(f"Is 7 automorphic? {is_automorphic(7)}")

#14. 
import math

def is_pronic(n):
    
    if n < 0:
        return False  # Pronic numbers are typically defined for non-negative integers

    for i in range(int(math.sqrt(n)) + 2): # Add 2 to ensure we check i*(i+1) where i is sqrt(n)
        if i * (i + 1) == n:
            return True
        elif i * (i + 1) > n:
            # If the product exceeds n, further iterations will also exceed n
            return False
    return False
print(is_pronic(66565))
print(is_pronic(7869))
print(is_pronic(562))

#15.)

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # We only need to check up to the square root of n
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2  # Increment by 2 to check only odd numbers

    # If n is still greater than 2, it means n itself is a prime factor
    if n > 2:
        factors.append(n)

    return factors

print(prime_factors(675412))
print(prime_factors(23247))
print(prime_factors(3764))

#16.

def count_distinct_prime_factors(n):
   
    if n <= 1:
        return 0  
    distinct_prime_factors = set()
    d = 2

    while n % d == 0:
        distinct_prime_factors.add(d)
        n //= d

    # odd factors
    d = 3
    while d * d <= n:
        while n % d == 0:
            distinct_prime_factors.add(d)
            n //= d
        d += 2

    # If n is still greater than 1, it must be a prime factor itself
    if n > 1:
        distinct_prime_factors.add(n)

    return len(distinct_prime_factors)
print(count_distinct_prime_factors(65445))
print(count_distinct_prime_factors(2434))

#17.)

import math

def is_prime_power(n):
    """
    Checks if a number n is a prime power (p^k where p is prime and k >= 1).
    """
    if n <= 1:
        return False

    # Find the smallest prime factor, p
    p = -1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = i
            break
    
    # If no factor was found within the loop, n itself is prime
    if p == -1:
        p = n
    
    # Check if n can be fully divided by only this single prime factor p
    temp_n = n
    while temp_n % p == 0:
        temp_n //= p
        
    # If temp_n becomes 1, then n was a power of p
    return temp_n == 1

# Examples:
print(f"8 is a prime power: {is_prime_power(8)}")       # 8 = 2^3 -> True
print(f"12 is a prime power: {is_prime_power(12)}")     # 12 = 2^2 * 3 -> False
print(f"1 is a prime power: {is_prime_power(1)}")       # False by definition

#18.)

import sys
import time
start_time=time.time()

def is_mersenne_prime(p):
   
    n = 2**p - 1
    if n <= 1:
        return False
    
    # Trial division to check for primality
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True


# p=3, Mersenne number is 2^3 - 1 = 7, which is prime
print(f"Is 2^3 - 1 a Mersenne prime? {is_mersenne_prime(3)}")

# p=5, Mersenne number is 2^5 - 1 = 31, which is prime
print(f"Is 2^5 - 1 a Mersenne prime? {is_mersenne_prime(5)}")

# p=11, Mersenne number is 2^11 - 1 = 2047 = 23 * 89, not prime
print(f"Is 2^11 - 1 a Mersenne prime? {is_mersenne_prime(11)}")
print(f"Is 2^22 - 1 a Mersenne prime? {is_mersenne_prime(22)}")

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(is_mersenne_prime))

#19.)

def is_prime(n):
   
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def twin_primes(limit):
   
    twin_prime_pairs = []
    for num in range(3, limit - 1):  # Start from 3 as 2 is not part of a twin prime pair (2,4)
        if is_prime(num) and is_prime(num + 2):
            twin_prime_pairs.append((num, num + 2))
    return twin_prime_pairs
print(is_prime(65779))
print(twin_primes(8))

#20.)

import math

def count_divisors(n):
    count = 0
    # Iterate from 1 up to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If i is a divisor, then n/i is also a divisor.
            # If i * i == n, then i and n/i are the same (e.g., for n=9, i=3, n/i=3).
            # In this case, we count it only once.
            if i * i == n:
                count += 1
            # Otherwise, i and n/i are distinct divisors, so we count both.
            else:
                count += 2
    return count
p=count_divisors(84)
print(p)

#21.)

def aliquot_sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer."

    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors

print(aliquot_sum(12))  
print(aliquot_sum(15))  
print(aliquot_sum(6))   
print(aliquot_sum(1))   

#22.)

def sum_proper_divisors(n):
   
    if n <= 1:
        return 0  # No proper divisors for 0 or 1
    
    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid adding the same divisor twice for perfect squares
                divisor_sum += n // i
    return divisor_sum

def are_amicable(a, b):
    
    if a == b:  # Amicable numbers must be distinct
        return False
    
    sum_div_a = sum_proper_divisors(a)
    sum_div_b = sum_proper_divisors(b)
    
    return sum_div_a == b and sum_div_b == a
print(sum_proper_divisors(4))
print(are_amicable(65,78))
print(are_amicable(43,43))

#23.)

def multiplicative_persistence(n):
        if n < 10:
            return 0  

        persistence_count = 0
        current_number = n

        while current_number >= 10:
            product = 1
            for digit_char in str(current_number):
                product *= int(digit_char)
        
            current_number = product
            persistence_count += 1
        
        return persistence_count
p=multiplicative_persistence(456789)
print(p)

#24.)
import math

def count_divisors(num):
    divisor_count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i:
                divisor_count += 1
            else:
                divisor_count += 2
    return divisor_count

def is_highly_composite(n):

    if n <= 0:
        return False

    original_divisors = count_divisors(n)
    # Check all numbers from n-1 down to 1
    for i in range(n - 1, 0, -1):
        if count_divisors(i) >= original_divisors:
            return False
    return True

# Example usage:
print(f"Is 12 highly composite? {is_highly_composite(12)}") 
print(f"Is 10 highly composite? {is_highly_composite(10)}") 
print(f"Is 1 highly composite? {is_highly_composite(1)}")   
print(f"Is 60 highly composite? {is_highly_composite(60)}") 

#25.)
def mod_exp(base, exponent, modulus):
    
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer.")
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    result = 1
    base = base % modulus
    while exponent > 0:
        
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus

    return result


base_val = 2
exponent_val = 10
modulus_val = 3
result = mod_exp(base_val, exponent_val, modulus_val)
print(f"({base_val}**{exponent_val}) % {modulus_val} = {result}")

base_large = 5
exponent_large = 100
modulus_large = 13
result_large = mod_exp(base_large, exponent_large, modulus_large)
print(f"({base_large}**{exponent_large}) % {modulus_large} = {result_large}")


#26.)

import time 
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    g, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return g, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    
    if g != 1:
        return None
    else:
        return (x % m + m) % m

# --- Function Call Examples ---

a1 = 3
m1 = 11
inverse1 = mod_inverse(a1, m1)
print(f"The modular inverse of {a1} mod {m1} is: {inverse1}")

a2 = 17
m2 = 20
inverse2 = mod_inverse(a2, m2)
print(f"The modular inverse of {a2} mod {m2} is: {inverse2}")

a3 = 6
m3 = 12
inverse3 = mod_inverse(a3, m3)
print(f"The modular inverse of {a3} mod {m3} is: {inverse3}")

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

#27.)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    g, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return g, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    
    if g != 1:
        return None
    else:
        return (x % m + m) % m
def crt(remainders, moduli):
    if not remainders or not moduli or len(remainders) != len(moduli):
        return None
    
    x = remainders[0]
    M = moduli[0]
    
    for i in range(1, len(moduli)):
        r_i = remainders[i]
        m_i = moduli[i]
        
        b = r_i - x
        
        M_inv = mod_inverse(M, m_i)
        
        if M_inv is None:
            return None
            
        k = (b * M_inv) % m_i
        
        x = x + k * M
        
        M = M * m_i
        
    return x % M

# --- Function Call Example (Chinese Remainder Theorem) ---

remainders = [2, 3, 2]
moduli = [3, 5, 7]

solution = crt(remainders, moduli)

print(f"The system of congruences:")
print(f"x ≡ {remainders[0]} (mod {moduli[0]})")
print(f"x ≡ {remainders[1]} (mod {moduli[1]})")
print(f"x ≡ {remainders[2]} (mod {moduli[2]})")

if solution is not None:
    print(f"\nThe smallest non-negative solution for x is: {solution}")
else:
    print("\nNo unique solution exists (mod M) because the moduli are not pairwise coprime.")


#28.)

def power(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        b = b // 2
        a = (a * a) % m
    return res

# --- Function Call Example (Modular Exponentiation) ---

# Calculate 3^5 mod 7
a = 3
b = 5
m = 7
result = power(a, b, m)

print(f"The result of {a}^{b} mod {m} is: {result}")

a2 = 2
b2 = 10
m2 = 13

result2 = power(a2, b2, m2)

print(f"The result of {a2}^{b2} mod {m2} is: {result2}")


#29.)

import math

def gcd(a, b):
    return math.gcd(a, b)

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None 
    
    k = 1
    current_power = a % n
    
    while current_power != 1:
        current_power = (current_power * a) % n
        k += 1
        
        if k > n: 
            return None 

    return k

# --- Function Call Example ---

a1 = 3
n1 = 7
order1 = order_mod(a1, n1)
print(f"The order of {a1} mod {n1} is: {order1}") # Expected: 6

a2 = 2
n2 = 5
order2 = order_mod(a2, n2)
print(f"The order of {a2} mod {n2} is: {order2}") # Expected: 4

a3 = 4
n3 = 6
order3 = order_mod(a3, n3)
print(f"The order of {a3} mod {n3} is: {order3}") # Expected: None

#30.
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(k):
    if k < 0:
        return False
    if k == 0:
        return True
    # Using math.isqrt is more robust and efficient for integer square roots in Python 3.8+
    # For compatibility, using **0.5 with int() is also common.
    s = int(k**0.5) 
    return s * s == k

def is_fibonacci(n):
    if n <= 0:
        return False
    # A positive integer n is a Fibonacci number if and only if
    # 5n^2 + 4 or 5n^2 - 4 is a perfect square.
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# --- Function Call Examples ---

# 1. Check a known Fibonacci number (e.g., 21)
f1 = 21
check1 = is_fibonacci(f1)
print(f"Is {f1} a Fibonacci number? {check1}") # Expected: True (5 * 21^2 + 4 = 2209, sqrt(2209) = 47)

# 2. Check a non-Fibonacci number (e.g., 14)
f2 = 14
check2 = is_fibonacci(f2)
print(f"Is {f2} a Fibonacci number? {check2}") # Expected: False

# 3. Check the smallest Fibonacci number (e.g., 1)
f3 = 1
check3 = is_fibonacci(f3)
print(f"Is {f3} a Fibonacci number? {check3}") # Expected: True


#31.)
import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def lucas_sequence(n):
    if n<=0:
        raise ValueError
    if n==1:
        return[2]
    sequence = [2,1]
    for i in range(2,n):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(lucas_sequence(7))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

# 32.) 
import math
import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def is_perfect_power(n):
    if n < 2:
        return False
    for b in range(2, int(math.log2(n)) + 1):
        a = round(n**(1.0 / b))
        for base in (a, a-1, a+1):
            if base> 1 and base ** b == n:
                return True
    return False

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(is_perfect_power(16))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

#33). 

import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def collatz_lenght(n):
    if n<= 0:
        raise ValueError("Input must be a positive integer.")
    
    steps = 0
    while n !=1:
        if n % 2==0:
            n //= 2 
        else:
            n = 3*n+1
        steps += 1
    return steps
end_time = time.time()
curr , max = tracemalloc.get_traced_memory()
    
print(collatz_lenght(6))
print(collatz_lenght(19))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

#34.)
import time
import tracemalloc
start_time =  time.time()
tracemalloc.start()

def polygonal_number(s,n):
    p = ((s-2)*(n**2) -(s-4)*n)//2
    return p

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(polygonal_number(3,5))

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

#35.)

import math
import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def is_carmichael(n):
    if n<2 :
        return False
    if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
        return False
    for a in range(2, n):
        if gcd(a, n) ==1:
           if pow(a, n-1, n) != 1:
              return False
    return True

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(gcd(7,5) ,is_carmichael(81))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

#36.)
import random

def power(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        b = b // 2
        a = (a * a) % m
    return res

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        # random.randint(2, n - 2) might fail if n <= 3, but is handled by base cases
        a = random.randint(2, n - 2)
        x = power(a, d, n)

        if x == 1 or x == n - 1:
            continue
        
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        
        if composite:
            return False

    return True

# --- Function Call Examples ---

# 1. Test a known prime number (53)
n1 = 53
result1 = is_prime_miller_rabin(n1)
print(f"Is {n1} prime? (Miller-Rabin): {result1}")

# 2. Test a known composite number (51 = 3 * 17)
n2 = 51
result2 = is_prime_miller_rabin(n2)
print(f"Is {n2} prime? (Miller-Rabin): {result2}")

# 3. Test a large prime number (997)
n3 = 997
result3 = is_prime_miller_rabin(n3)
print(f"Is {n3} prime? (Miller-Rabin): {result3}")


#37.)
import random
import math

def gcd(a, b):
    return math.gcd(a, b)

def pollard_rho(n):
    if n <= 1:
        return None
    if n % 2 == 0:
        return 2
    
    # Check if n is prime before starting the algorithm (optional but good practice)
    # A simple primality test could be added here, but we proceed with the core algorithm.

    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    
    # Define the pseudo-random function f(x) = (x^2 + c) mod n
    def f(x):
        return (x * x + c) % n

    # The loop implements Floyd's cycle-finding algorithm (tortoise and hare)
    while d == 1:
        x = f(x)
        y = f(f(y))
        
        # d = gcd(|x - y|, n)
        d = gcd(abs(x - y), n)

        if d == n:
            # Cycle detected without finding a factor, restart with new initial values
            # This happens if the cycle forms entirely within the group of residues modulo n, 
            # and no collision has occurred modulo a factor p.
            x = random.randint(2, n - 1)
            y = x
            c = random.randint(1, n - 1)
            d = 1
        elif d != 1:
            # We found a non-trivial factor
            return d

    return d # Should be unreachable if the logic is correct, but kept for completeness

# --- Function Call Examples ---

# 1. Factor a small composite number (e.g., 91 = 7 * 13)
n1 = 91
factor1 = pollard_rho(n1)
print(f"A factor of {n1} is: {factor1}")

# 2. Factor another composite number (e.g., 87 = 3 * 29)
n2 = 87
factor2 = pollard_rho(n2)
print(f"A factor of {n2} is: {factor2}")

# 3. Factor a number with a small prime factor (e.g., 143 = 11 * 13)
n3 = 143
factor3 = pollard_rho(n3)
print(f"A factor of {n3} is: {factor3}")

#38.)

import math
import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()
def zeta_approx(s, terms):
    if s == 1:
        # Harmonic series diverges, but we'll return the sum up to 'terms'
        pass
    
    zeta_sum = 0
    for n in range(1, terms + 1):
        try:
            term = 1.0 / math.pow(n, s)
            zeta_sum += term
        except OverflowError:
            return float('inf') 
        except ZeroDivisionError:
            pass

    return zeta_sum

# --- Function Call Examples ---

# Known value: zeta(2) = pi^2 / 6 ≈ 1.644934
s1 = 2
terms1 = 1000
approximation1 = zeta_approx(s1, terms1)
exact_value1 = (math.pi**2) / 6
print(f"Approximation of Zeta({s1}) using {terms1} terms: {approximation1}")
print(f"Known exact value of Zeta({s1}): {exact_value1}")

print("-" * 30)

# Known value: zeta(4) = pi^4 / 90 ≈ 1.082323
s2 = 4
terms2 = 100
approximation2 = zeta_approx(s2, terms2)
exact_value2 = (math.pi**4) / 90
print(f"Approximation of Zeta({s2}) using {terms2} terms: {approximation2}")
print(f"Known exact value of Zeta({s2}): {exact_value2}")

print("-" * 30)

# Case s=1 (Harmonic Series) - Diverges
s3 = 1
terms3 = 1000
approximation3 = zeta_approx(s3, terms3)

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"Approximation of Zeta({s3}) (Harmonic Series) using {terms3} terms: {approximation3}")

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")

#39.)

import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def partition_function(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    p = [0] * (n + 1)
    p[0] = 1

    for i in range(1, n + 1):
        j = 1
        while True:
            # Generalized pentagonal number k(3k-1)/2
            g1 = j * (3 * j - 1) // 2
            
            # The sign pattern is based on k: k=1, 2 have sign +, k=3, 4 have sign -, etc.
            # Sign is determined by j: 1, 2 (j=1), 3, 4 (j=2), ...
            sign = (-1)**(j - 1)
            
            if i - g1 >= 0:
                p[i] += sign * p[i - g1]
            else:
                break
                
            # Second generalized pentagonal number k(3k+1)/2
            g2 = j * (3 * j + 1) // 2
            
            if i - g2 >= 0:
                p[i] += sign * p[i - g2]
            else:
                break

            j += 1
            
    return p[n]

# --- Function Call Examples ---

# 1. Calculate p(5): 5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1. Total 7.
n1 = 5
result1 = partition_function(n1)
print(f"The number of partitions for n={n1} is: {result1}")

# 2. Calculate p(10): Total 42.
n2 = 10
result2 = partition_function(n2)
print(f"The number of partitions for n={n2} is: {result2}")

# 3. Calculate p(20): Total 627.
n3 = 20
result3 = partition_function(n3)
end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(f"The number of partitions for n={n3} is: {result3}")

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")