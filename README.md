# PYTHON PROJECT
This file(VITYARTHI.py), is collection of Python programmes contains various concepts and algorithms from number theory. This file is divided into many subparts

#Part-1 : Basic Integer Properties and Calculations(1-10)

Section--Functionality--Description
1 & 6: - Factorial Calculation -- Computes the factorial of a non-negative integer using a simple iterative approach.
2 & 7: - Palindrome Check -- Determines if an integer is a palindrome (reads the same forwards and backwards).
3 & 8: - Mean of Digits -- Calculates the arithmetic mean of the digits of an integer.
4 & 9: - Digital Root -- Finds the digital root of an integer (the single-digit result of iteratively summing its digits).
5 & 10: - Abundant Number Check -- Determines if a number is abundant by checking if the sum of its proper divisors is greater than the number itself.

#Part-2 : Number Classification(11-14)

Section -- Functionality -- Description
11-Deficient Number Check (is_deficient) -- Checks if a number is deficient (sum of proper divisors is less than the number).
12-Harshad (Niven) Number Check (is_harshad) -- Checks if a number is divisible by the sum of its digits.
13-Automorphic Number Check (is_automorphic) -- Checks if a number appears as the last digits of its own square (e.g., 52=25, 762=5776)."
14-Pronic (Oblong) Number Check (is_pronic) -- Checks if a number is the product of two consecutive integers, n(n+1)."

#Part-3 : Divisibilty, Factors and Prime Number(15-20)

Section,Functionality,Description
15-Prime Factorization (prime_factors) -- Computes and returns a list of all prime factors of a given integer.
16-Count Distinct Prime Factors (count_distinct_prime_factors) -- Counts the number of unique prime factors of an integer.
17-Prime Power Check (is_prime_power) -- Determines if a number is a prime power (e.g., 8=23).
18-Mersenne Prime Check (is_mersenne_prime) -- Checks if 2p−1 is a Mersenne prime for a given exponent p. Uses basic trial division for primality testing.
19-Twin Primes (twin_primes-) -- Generates a list of twin prime pairs (primes (p,p+2)) up to a given limit. Includes an efficient O(n​) primality test (is_prime).
20-Count Divisors (count_divisors) -- Counts the total number of positive divisors for an integer.

#Part-4: Advanced Divisor Properties(21-24)

Section -- Functionality -- Description
21-Aliquot Sum (aliquot_sum) -- Computes the sum of all proper divisors (divisors excluding the number itself).
22-Amicable Number Check (are_amicable) -- "Checks if two distinct numbers a and b are amicable, where the sum of proper divisors of a equals b and vice-versa."
23-Multiplicative Persistence (multiplicative_persistence) -- Finds the number of steps required to reduce a number to a single digit by iteratively multiplying its digits.
24-Highly Composite Number Check (is_highly_composite) -- Determines if a number n has more divisors than any positive integer less than n.

#Part 5: Modular Arithmetic and Cryptography Primitive (25-29)

Section,Functionality,Description
25 & 28-Modular Exponentiation (mod_exp, power) -- Calculates (baseexponent)(modmodulus) efficiently using the method of exponentiation by squaring (binary exponentiation).
26-Modular Inverse (mod_inverse) -- Computes the modular multiplicative inverse of a modulo m using the Extended Euclidean Algorithm (extended_gcd).
27-Chinese Remainder Theorem (CRT) (crt) -- Solves a system of linear congruences using the modular inverse and Extended Euclidean Algorithm.
29-Order of an Element Modulo n (order_mod) -- "Finds the smallest positive integer k such that ak≡1(modn), provided gcd(a,n)=1."

#Part-6: Sequence and Number Algorithms (30-34)

Section-Functionality-Description
30-Fibonacci Number Check (is_fibonacci) - Checks if a number is a Fibonacci number using the mathematical property based on perfect squares (5n2±4).
31-Lucas Sequence (lucas_sequence) - "Generates the Lucas numbers Ln​ where L0​=2,L1​=1, and Ln​=Ln−1​+Ln−2​."
32-Perfect Power Check (is_perfect_power) - Determines if a positive integer n can be expressed as ab for integers a≥2 and b≥2.
33-Collatz Sequence Length (collatz_lenght) - Computes the number of steps required to reach 1 in the Collatz sequence.
34-Polygonal Number (polygonal_number) - Calculates the nth polygonal number for a polygon with s sides.

#Part-7: Advanced Primality and Factorization (35,36 and 37)
Section - Functionality - Description
35-Carmichael Number Check (is_carmichael) - "Checks if a number n is a Carmichael number (a composite number n such that an−1≡1(modn) for all integers a with gcd(a,n)=1)."
36-Miller-Rabin Primality Test (is_prime_miller_rabin) - A probabilistic primality test used for efficiently determining if large numbers are likely prime.
37-Pollard's Rho Algorithm (pollard_rho) - "A specialized integer factorization algorithm, effective for finding small factors of a large composite number."

#Part-8: Analytical Number Theory(38 and 39)
Section,Functionality,Description
38-Riemann Zeta Function Approximation (zeta_approx) - Approximates the value of the Riemann Zeta function ζ(s) by summing the first N terms of the series ∑n=1∞​ns1​.
39-Partition Function (partition_function) - "Calculates p(n), the number of ways a positive integer n can be written as a sum of positive integers, using Euler's pentagonal number theorem."
