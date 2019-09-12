def distributed_dlog(h, delta, m, g, fi):
    """converts a multiplicative secret sharing of g^x
    to an additive secret sharing of the value x, with inverse polynomial probability of error.

    :param g: g from ElGamal.
    :param h: g^t, t is modulo q.
    :param delta: failure probability.
    :param m: a polynomial number smaller then q.
    :param fi: a PRF.
    :return:
    """
    from math import log
    h_tag = h
    i = 0
    t = (2 * m * log(2 / delta)) / delta
    # hash_len = log(2 * m / delta)
    while int(bin(fi(data=str(h_tag))), 2) != 0 and i < t:
        h_tag *= g
        i += 1
    return i


def generate_prf(lamda):
    """generate PRF.

    :param lamda: a length of the key.
    :return: a PRF list.
    :rtype: list of dictionary.
    """
    import hashlib

    def prf(data: str):
        """"hash the data
        """
        hash_num = hashlib.sha512()
        hash_num.update(bytes(data.encode("utf-8")))
        return int(hash_num.hexdigest()[:lamda], 16)

    return prf


def additive_secret_shares(c):
    """

    :param c: string, an encryption message.
    :return: a r and c-r as {r: c-t}.
    :rtype: tuple
    """
    import random
    r = random.getrandbits(512)
    return int(r, 16), hex(int(c, 16) - int(r, 16))


def multi_shares(h1, h2, y, cy):
    """

    :param h1:
    :type h1: str
    :param h2:
    :type h2: str
    :param y:
    :type y: str
    :param cy:
    :return:
    """
    return pow(int(h2, 16), int(y, 16)) * pow(int(h1, 16), -int(cy, 16))


def convert_shares(server_id, ):
    pass
