import he_encryption
from bitarray import bitarray


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
        """bit generator of bitarray object.

        :param bit_array: a bitarray object.
        """
        for bit in bit_array.to01():
            yield int(bit, 2)

    def encrypt_each_data_bit(self, data_bit_array):
        """encrypt each bit of data with el-gamal.

        :param data_bit_array: a data bitarray.
        :return: a list of bits encrypted with el-gamal.
        :rtype: list
        """
        return [self.encrypt_msg(bit) for bit in HeClient.bit_array_generator(bit_array=data_bit_array)]

    def encrypt_each_data_bit_with_prv_key(self, data_bit_array):
        """encrypt each bit of data multiple by each bit of private key.

        :param data_bit_array: a data bitarray of data.
        :return: a list of bit of data multiple by each bit of private key.
        :rtype: list
        """
        total_data_bit_with_prv_key = []
        for data_bit in HeClient.bit_array_generator(bit_array=data_bit_array):
            total_data_bit_with_prv_key = [self.encrypt_msg(data_bit*prv_bit) for prv_bit in bin(int(self.prv_key, 16))]
        return total_data_bit_with_prv_key

    @staticmethod
    def additive_each_data_bit(data_bit_array):
        """generate an additive share of each bit of data.

        :param data_bit_array: a data bitarray of data.
        :return: a list of additive share of each bit of data.
        :rtype: list
        """
        return [he_encryption.additive_secret_shares(bit)
                for bit in HeClient.bit_array_generator(bit_array=data_bit_array)]

    def additive_data_bit_with_prv_key(self, data_bit_array):
        """generate an additive share of each bit of data multiple by private key.

        :param data_bit_array: a data bitarray of data.
        :return: a list of additive share of each bit of data multiple by private key.
        :rtype: list
        """
        return [he_encryption.additive_secret_shares(bit * self.prv_key)
                for bit in HeClient.bit_array_generator(bit_array=data_bit_array)]

    def share(self, data: str):
        """main algorithm, generate a homomorphic secret sharing scheme.
        algorithm:
        for each input of 'data', do the following:
        1. ElGamal encryption:
            i)  encrypt each bit of 'data' with ElGamal.
            ii) encrypt each bit of 'data' multiple by each bit of private key.
        2. Additive secret sharing:
            i)  generate additive share to each bit of 'data'.
            ii) generate additive share to each bit of 'data' multiple by private key.

        :param data: a data to encrypt.
        :return: a homomorphic secret sharing scheme.
        :rtype: dict
        """
        data_bit_array = bitarray(data)
        enc_each_data_bit = self.encrypt_each_data_bit(data_bit_array=data_bit_array)
        enc_data_prv_bit = self.encrypt_each_data_bit_with_prv_key(data_bit_array=data_bit_array)
        additive_data_bit = HeClient.additive_each_data_bit(data_bit_array=data_bit_array)
        additive_data_bit_with_prv = self.additive_data_bit_with_prv_key(data_bit_array=data_bit_array)
        return {
            "enc_each_data_bits": enc_each_data_bit,
            "enc_data_with_prv": enc_data_prv_bit,
            "additive_data": additive_data_bit,
            "additive_data_mul_prv": additive_data_bit_with_prv
        }
