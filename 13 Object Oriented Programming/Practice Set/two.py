class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n * self.n

num = Calculator(5)
print(num.square())