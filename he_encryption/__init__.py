#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .el_gamal import encrypt
from .el_gamal import decrypt
from math import log2
from he_encryption import generate_primes


def distributed_dlog(h, delta, m, p_func, g):
    """

    :param g: g from el gamal.
    :param h: g^t, t is modulo q.
    :param delta: safety factor
    :param m:
    :param p_func: pseudo-function.
    :return:
    """
    h_tag = h
    i = 0
    t = (2 * m * log2(2/delta))/delta
    while p_func(h_tag) != 0 and i < t:
        h_tag *= g
        i += 1
    return i
