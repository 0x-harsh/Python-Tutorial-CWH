class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, other):
        # Formula: (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        real_part = (self.r * other.r) - (self.i * other.i)
        imag_part = (self.r * other.i) + (self.i * other.r)
        return Complex(real_part, imag_part)

    def __str__(self):
        sign = "+" if self.i >= 0 else "-"
        return f"{self.r} {sign} {abs(self.i)}i"

c1 = Complex(3, -4)
c2 = Complex(5, -6)

print(c1 + c2)
print(c1 * c2)