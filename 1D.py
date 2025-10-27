class Vector:
    def __init__(self, x, y=None, z=None):
        assert isinstance(x, (int, float))
        self.x = x

        assert isinstance(y, (int, float))
        self.y = y

        assert isinstance(z, (int, float))
        self.z = z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def center_mass(points):
    X = Y = Z = 0
    n = len(points)
    for point in points:
        X += point.x
        Y += point.y
        Z += point.z
    return Vector(X / n, Y / n, Z / n)

def max_square(points):
    maxi = 0
    for point1 in points:
        for point2 in points:
            for point3 in points:
                a = abs(point1 - point2)
                b = abs(point2 - point3)
                c = abs(point3 - point1)
                p = (a + b + c)/2
                square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                if square > maxi:
                    maxi = square
    return maxi

points = [
    Vector(0, 0, 0),
    Vector(1, 0, 0),
    Vector(0, 0, 2),
    Vector(0, 0, 1),
    Vector(1, 1, 1),
    Vector(2, 0, 0),
    Vector(0, 3, 0)
]
d = center_mass(points)
print(d)
m = max_square(points)
print(m)
# задание 1

# спасибо дипсику за помощь с правильным считыванием данных в нужном формате: {x, y, z}

