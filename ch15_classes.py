from operator import add, sub, mul
from ch09_functions import gen_stream


# Classes: Practical Task 1
class Matrix:
    def __init__(self, rows, columns, gen):
        self.rows = rows
        self.cols = columns
        self.data = sorted(sorted(tuple(c for c in gen() if c[2]), key=lambda c: c[1]), key=lambda c: c[0])

    def __gen(self):
        return tuple(gen_stream(self.rows * self.cols, self.data, lambda c: (c[0] * self.cols + c[1], c[2])))

    def __operator(self, other, operation):
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError
        return Matrix(
            self.rows,
            self.cols,
            lambda: tuple(
                (i // self.cols, i % self.cols, c)
                for i, c in enumerate(map(operation, self.__gen(), other.__gen())) if c
            )
        )

    def mult(self, other):
        if self.cols != other.rows:
            raise ValueError
        return Matrix(
            self.rows,
            other.cols,
            lambda: sum((tuple(filter(
                lambda c: c[2],
                tuple((row, col, sum(map(
                    mul,
                    self.__gen()[row * self.cols:row * self.cols + self.cols],
                    other.transpose().__gen()[col * other.rows:col * other.rows + other.rows]
                ))) for col in range(other.cols))
            )) for row in range(self.rows)), ())
        )

    def mult_scalar(self, scalar):
        return Matrix(self.rows, self.cols, lambda: tuple((row, col, val * scalar) for row, col, val in self.data))

    def sum(self, other):
        return self.__operator(other, add)

    def subt(self, other):
        return self.__operator(other, sub)

    def transpose(self):
        return Matrix(self.cols, self.rows, lambda: tuple((col, row, val) for row, col, val in self.data))

    def __repr__(self):
        return '\n'.join([f'{row}' for row in zip(*[iter(self.__gen())] * self.cols)])


def gen():
    yield 0, 0, 1
    yield 0, 1, 2
    yield 1, 0, 1
    yield 1, 2, 1


def gen_ex(rows, cols):
    def callback():
        for row in range(rows):
            for col in range(cols):
                yield row, col, row

    return callback


print('----------------------------------------')

m = Matrix(2, 3, gen)
print(m)
print(m.transpose())
print(m.sum(m))
print(m.subt(m))
print(m.mult_scalar(5))
print(m.mult(m.transpose()))

m = Matrix(3, 3, lambda: ())
print(m)

m = Matrix(3, 3, gen_ex(3, 3))
print(m)
print(m.mult(m.transpose()).mult_scalar(10))
