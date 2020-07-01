class CompDig:
    def __init__(self, real_num, imag_num):
        self.real = real_num
        self.imag = imag_num

    def __str__(self):
        return ''.join(f"{self.real} {self.imag}")

    def __add__(self, other):
        return CompDig(self.real + other.real,
                       self.imag + other.imag)

    def __mul__(self, other):
        return CompDig(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)


c_1 = CompDig(2, -1)
c_2 = CompDig(3, 1)
print(c_1 + c_2)
print(c_1 * c_2)

