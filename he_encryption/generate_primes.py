#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://incolumitas.com/2018/08/12/finding-large-prime-numbers-and-rsa-miller-rabin-test/

import re
import random
import math

"""
Generate prime numbers with the Miller-Rabin Primality Test.
"""


def fermat_primality_test(p, s=5):
    """
    a^(p-1) ? 1 mod p
    Input: prime candidate p and security paramter s
    Output: either p is a composite (always trues), or
            p is a prime (with probability)
    """
    if p == 2:
        return True
    if not p & 1:  # if p is even, number cant be a prime
        return False

    for i in range(s):
        a = random.randrange(2, p - 2)
        x = pow(a, p - 1, p)  # a**(p-1) % p
        if x != 1:
            return False
    return True


def square_and_multiply(x, k, p=None):
    """
    Square and Multiply Algorithm
    Parameters: positive integer x and integer exponent k,
                optional modulus p
    Returns: x**k or x**k mod p when p is given
    """
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r ** 2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r


def miller_rabin_primality_test(p, s=5):
    if p == 2:  # 2 is the only prime that is even
        return True
    if not (p & 1):  # n is a even number and can't be prime
        return False

    p1 = p - 1
    u = 0
    r = p1  # p-1 = 2**u * r

    while r % 2 == 0:
        r >>= 1
        u += 1

    # at this stage p-1 = 2**u * r  holds
    assert p - 1 == 2 ** u * r

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2 ** i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p - 2)
        if witness(a):
            return False

    return True


def generate_primes(n=512, k=1):
    """
    Generates prime numbers with bitlength n.
    Stops after the generation of k prime numbers.

    Caution: The numbers tested for primality start at
    a random place, but the tests are drawn with the integers
    following from the random start.
    """
    assert k > 0
    assert 0 < n < 4096

    # follows from the prime number theorem
    necessary_steps = math.floor(math.log(2 ** n) / 2)
    # get n random bits as our first number to test for primality
    x = random.getrandbits(n)

    primes = []

    while k > 0:
        if miller_rabin_primality_test(x, s=7):
            primes.append(x)
            k = k - 1
        x = x + 1

    return primes


def generate_creator(q):
    """generate a creator for cyclic group of Z*q. (Lagrange's theorem - group theory)

    :param q: a big prime. (the order of the group)
    :return: a creator of the cyclic group.
    """
    for num in range(1, q):
        p = (num * q) + 1
        if miller_rabin_primality_test(p, s=7):
            g_tag = random.getrandbits(len(str(p))) % p
            return pow(g_tag, num, q)


def main():
    n = 2048
    primes = generate_primes(n=n)
    for p in primes:
        print('{} \nis prime with bitlength={}'.format(p, n))


if __name__ == '__main__':
    main()
