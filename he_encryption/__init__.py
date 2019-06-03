#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .el_gamal import encrypt
from .el_gamal import decrypt
from .el_gamal import gen_key
from .el_gamal import modular_exponentiation
from he_encryption import generate_primes
from he_encryption.generate_primes import generate_primes


def distributed_dlog(h, delta, m, g):
    """

    :param g: g from ElGamal.
    :param h: g^t, t is modulo q.
    :param delta: failure probability.
    :param m: a polynomial number smaller then q.
    :return:
    """
    from math import log
    import hashlib
    h_tag = h
    i = 0
    t = (2 * m * log(2/delta))/delta
    hash_len = log(2 * m / delta)
    while hashlib.sha512(h_tag).hexdigest()[:hash_len] != 0 and i < t:
        h_tag *= g
        i += 1
    return i


def generate_random_seed(num_range, key):
    """generate PRF.

    :param num_range: a range of generate random.
    :param key: a key from table.
    :return: a PRF list.
    :rtype: list of dictionary.
    """
    import os
    prf_table = {}
    for num in range(num_range):
        if key in prf_table:
            yield prf_table[key]
        num_gen = os.urandom(num_range)
        prf_table[key] = num_gen
        yield num_gen
    return prf_table


def additive_secret_shares(c):
    """

    :param c: string, an encryption message.
    :return: a r and c-rב.
    :rtype: tuple
    """
    import random
    r = random.getrandbits(512)
    return hex(r), hex(int(c, 16) - r)
