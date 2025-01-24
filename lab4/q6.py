class PowerCalculator:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def pow(self):
        # If exponent is negative, calculate the positive power and take reciprocal
        if self.n < 0:
            return 1 / self._pow_helper(self.x, -self.n)
        else:
            return self._pow_helper(self.x, self.n)

    def _pow_helper(self, x, n):
        # Base case: If exponent is 0, return 1
        if n == 0:
            return 1
        # If exponent is 1, return x
        if n == 1:
            return x
        # Divide and conquer approach for exponentiation by squaring
        half = self._pow_helper(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

# Taking user input for the base (x) and exponent (n)
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))

# Creating an instance of PowerCalculator
calculator = PowerCalculator(x, n)

# Calculating x raised to the power of n
result = calculator.pow()

# Printing the result
print(f"{x} raised to the power of {n} is: {result}")


""" Enter the base (x): 4
Enter the exponent (n): 2
4.0 raised to the power of 2 is: 16.0  """