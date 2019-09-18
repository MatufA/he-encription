#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ElGamal encryption is an public-key cryptosystem. It uses asymmetric key encryption for communicating
between two parties and encrypting the message.This cryptosystem is based on the difficulty of finding
discrete logarithm in a cyclic group that is even if we know g^a and g^k, it is extremely difficult to compute g^ak.

@url: https://www.geeksforgeeks.org/elgamal-encryption-algorithm/
"""
import random
from math import pow
from math import gcd
import time
from he_encryption.generate_primes import generate_primes
from he_encryption.generate_primes import generate_creator


def gen_key(q):
    """generate private key.

    :param q:
    :return:
    """
    key = random.randint(pow(10, 20), q-1)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q-1)
    return key


# Modular exponentiation
def modular_exponentiation(b, e, m):
    """produced modular exponentiation.
    https://en.wikipedia.org/wiki/Modular_exponentiation

    :param b: a base number.
    :param e: an exponent.
    :param m: a modulo.
    :return: a reminder of b modulo m.
    """
    x = 1
    y = b
    while e > 0:
        if e % 2 == 0:
            x = (x * y) % m
        y = (y * y) % m
        e = int(e / 2)
    return x % m


def encrypt(msg, q, h, g):
    """encrypt massage with ElGamal.

    :param msg: a message data.
    :param q: a prime number modulo.
    :param h: a public key ElGamal.
    :param g: a prime number g.
    :return: an encrypted message. (ElGamal output, g^k and g^ak)
    """
    en_msg = []

    k = gen_key(q)  # Private key for sender
    s = modular_exponentiation(h, k, q)
    p = modular_exponentiation(g, k, q)

    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p


def decrypt(en_msg, p, key, q):
    """decrypt massage with ElGamal.

    :param en_msg: an encrypted message with ElGamal.
    :param p: a g^k.
    :param key: a private key.
    :param q: a prime number modulo.
    :return: a decrypted message.
    """
    dr_msg = []
    h = modular_exponentiation(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))

    return dr_msg


def main():
    msg = 'encryption'
    print("Original Message :", msg)

    q = generate_primes(n=1024, k=1)[0]
    g = generate_creator(q=q)
    print("q: " + str(q))
    print("g: " + str(g))

    key = gen_key(q)  # Private key for receiver
    h = modular_exponentiation(g, key, q)  # public key (g^c)
    print("g used : ", g)
    print("g^a used : ", h)

    en_msg, p = encrypt(msg, q, h, g)
    print("The encryption message:", en_msg)
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    print("Decrypted Message :", dmsg)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("----------{0} seconds----------".format(time.time()-start_time))
