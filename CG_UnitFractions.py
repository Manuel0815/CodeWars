import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# 1/n = 1/(n+1) + 1/[n*(n+1)]
# x = n+1
# y = n*(n+1)

# 1/n = 1/(n+a) + 1/(n+b)
# n^2 = a*b
# a and b have to be divisors of n^2

n = int(input())

def get_divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    yield from generate(0)

solutions = []
n_square = pow(n, 2)
divisors = get_divisors(n_square)

for a in divisors:
    # for b in divisors:
    b = int(n_square / a)
    if a >= b and n_square == a*b:
        if a not in solutions:
            solutions.append(a)

solutions.sort(reverse=True)

for a in solutions:
    print("1/" + str(n) + " = 1/" + str(n + a) + " + 1/" + str(n + int(n_square / a)))