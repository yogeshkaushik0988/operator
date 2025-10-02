class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector objects to another Vector")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Can only multiply Vector by a scalar (int or float)")

    def __rmul__(self, scalar): # For scalar * Vector
        return self.__mul__(scalar)

if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    v_sum = v1 + v2
    print(f"Vector Sum: {v_sum}")

    v_scaled = v1 * 5
    print(f"Scaled Vector: {v_scaled}")

    v_reversed_scaled = 2 * v2 # Demonstrates __rmul__
    print(f"Reversed Scaled Vector: {v_reversed_scaled}")