import he_encryption


class HeClient:
    def __init__(self, n_server=1):
        self.n_server = n_server
        self.q, self.g = he_encryption.generate_primes(n=1024, k=2)
        self.dec_key = he_encryption.gen_key(self.q)
        self.prv_key = he_encryption.modular_exponentiation(self.g, self.dec_key, self.q)

    def eval(self):
        pass

    def decrypt_msg(self, enc_msg):
        """Decrypt ElGamal encryption messages.

        :param enc_msg: tuple, an ElGamal encrypted message (c1, c2).
        :return: an plain text message.
        """
        msg = he_encryption.decrypt(enc_msg[1], enc_msg[2], self.dec_key, self.q)
        return ''.join(msg)

    def encrypt_msg(self, plain_msg):
        """Encrypt messages with ElGamal.

        :param plain_msg: a message to encrypt.
        :return: an ElGamal encryption, (c1, c2).
        :rtype: tuple
        """
        return he_encryption.encrypt(plain_msg, self.q, self.prv_key, self.g)
# el gamal encryption

# secret sharing
# multiply each bits. (private * info)

# additive secret sharing
#
