class HeServer:
    def __init__(self, server_id, op_instruction, error_bound):
        """Homomorphic Share Evaluation of RMS Programs

        :param server_id: a server identifier. (0 or 1)
        """
        self.op_instruction = op_instruction
        self.error_bound = error_bound
        self.id = server_id

    def add(self, a: dict, b: dict):
        """Compute a + b.

        :param a: dict, key: an hex number, value: an hex number additive.
        :param b: dict, key: an hex number, value: an hex number additive.
        :return: an a + b operations. (for key and additive as well).
        :rtype: dict.
        """
        a_val = list(a.keys())[0]
        b_val = list(b.keys())[0]
        val = hex(a_val) + hex(b_val)
        additive = hex(a[a_val]) + hex(b[b_val])
        return {val: additive}

    def mul(self, a: dict, b: dict):
        """Compute a * b.

        :param a: dict, key: an hex number, value: an hex number additive.
        :param b: dict, key: an hex number, value: an hex number additive.
        :return: an a * b operations. (for key and additive as well).
        :rtype: dict.
        """
        pass

    def instruction(self, id, y):
        """

        :param id:
        :return:
        """
        z = -1 * self.id * y
