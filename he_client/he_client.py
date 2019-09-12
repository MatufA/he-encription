import he_encryption


class HeClient:
    def __init__(self, n_server=2):
        self.n_server = n_server
        self.q, self.g = he_encryption.generate_primes(n=1024, k=2)
        self.prv_key = he_encryption.gen_key(self.q)
        self.pub_key = he_encryption.modular_exponentiation(self.g, self.prv_key, self.q)

    def decrypt_msg(self, enc_msg):
        """Decrypt ElGamal encryption messages.

        :param enc_msg: tuple, an ElGamal encrypted message (c1, c2).
        :return: an plain text message.
        """
        msg = he_encryption.decrypt(enc_msg[1], enc_msg[2], self.prv_key, self.q)
        return ''.join(msg)

    def encrypt_msg(self, plain_msg):
        """Encrypt messages with ElGamal.

        :param plain_msg: a message to encrypt.
        :return: an ElGamal encryption, (c1, c2).
        :rtype: tuple
        """
        return he_encryption.encrypt(plain_msg, self.q, self.pub_key, self.g)

    @staticmethod
    def bit_array_generator(bit_array):
        for bit in bit_array.to01():
            yield bit

    def encrypt_each_data_bit(self, data: str):
        from bitarray import bitarray
        bit_array = bitarray(data)
        return [self.encrypt_msg(bit) for bit in HeClient.bit_array_generator(bit_array=bit_array)]

    def encrypt_each_data_bit_with_prv_key(self, data: str):
        from bitarray import bitarray
        data_bit_array = bitarray(data)
        prv_bit_array = bitarray(self.prv_key)
        zip_bit_array = zip(HeClient.bit_array_generator(bit_array=data_bit_array),
                            HeClient.bit_array_generator(bit_array=prv_bit_array))
        return [self.encrypt_msg(bits[0] * bits[1]) for bits in zip_bit_array]

    @staticmethod
    def additive_each_data_bit(data: str):
        from bitarray import bitarray
        bit_array = bitarray(data)
        return [he_encryption.additive_secret_shares(bit) for bit in HeClient.bit_array_generator(bit_array=bit_array)]

    def additive_data_bit_with_prv_key(self, data: str):
        from bitarray import bitarray
        data_bit_array = bitarray(data)
        return [he_encryption.additive_secret_shares(bit * self.prv_key)
                for bit in HeClient.bit_array_generator(bit_array=data_bit_array)]

    def share(self, data: str):
        enc_each_data_bit = self.encrypt_each_data_bit(data=data)
        enc_data_prv_bit = self.encrypt_each_data_bit_with_prv_key(data=data)
        additive_data_bit = HeClient.additive_each_data_bit(data=data)
        additive_data_bit_with_prv = self.additive_data_bit_with_prv_key(data=data)
        return {
            "enc_each_data_bits": enc_each_data_bit,
            "enc_data_with_prv": enc_data_prv_bit,
            "additive_data": additive_data_bit,
            "additive_data_mul_prv": additive_data_bit_with_prv
        }
