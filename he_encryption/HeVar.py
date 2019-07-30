class HeVar:
    def __init__(self, w, cw, server_id):
        self.y = w
        self.cy = cw
        self.server_id = server_id

    def __add__(self, other):
        assert isinstance(other, HeVar)
        y = self.y + other.y
        cy = self.cy + other.cy
        return HeVar(w=y, cw=cy, server_id=self.server_id)

    def __mul__(self, other):
        assert isinstance(other, HeVar)
        pass

    def __sub__(self, other):
        assert isinstance(other, HeVar)
        y = self.y + (-1) * other.y
        cy = self.cy + (-1) * other.cy
        return HeVar(w=y, cw=cy, server_id=self.server_id)

    def __truediv__(self, other):
        assert isinstance(other, HeVar)
        count_y = count_cy = 0

        divisor_y = abs(other.y)
        divisor_cy = abs(other.cy)

        for dividend in range(abs(self.y), abs(divisor_y) + divisor_y, divisor_y):
            count_y += 1
        for dividend in range(abs(self.cy), abs(divisor_cy) + divisor_cy, divisor_cy):
            count_cy += 1

        count_y *= -1 if (self.y < 0 < other.y) or (self.y > 0 > other.y) else 1
        count_cy *= -1 if (self.cy < 0 < other.cy) or (self.cy > 0 > other.cy) else 1
        return HeVar(w=count_y, cw=count_cy, server_id=self.server_id)

    def __pow__(self, power, modulo=None):
        return sum([HeVar(w=self.y, cw=self.cy, server_id=self.server_id) for _ in range(power)])
