from operator import add, sub, mul
from ch09_functions import gen_stream


# Classes: Practical Task 1
class Matrix:
    def __init__(self, rows, columns, gen):
        self.rows = rows
        self.cols = columns
        self.data = gen

    def __gen(self):
        return gen_stream(self.rows * self.cols, self.data(), lambda c: (c[0] * self.cols + c[1], c[2]))

    def mult(self, other):
        if self.cols != other.rows:
            raise ValueError

        res = ((
            sum(a * b for a, b in zip(row, col))
            for col in zip(*[other.transpose().__gen()] * other.rows)
        ) for row in zip(*[self.__gen()] * self.cols))

        return Matrix(
            self.rows,
            other.cols,
            lambda: (
                (i // other.cols, i % other.cols, c)
                for i, c in enumerate(el for row in res for el in row) if c
            )
        )

    def mult_scalar(self, scalar):
        other = Matrix(
            self.rows,
            self.cols,
            lambda: ((i // self.cols, i % self.cols, scalar) for i in range(self.rows * self.cols))
        )
        return Matrix(
            self.rows,
            self.cols,
            lambda: (
                (i // self.cols, i % self.cols, c)
                for i, c in enumerate(map(mul, self.__gen(), other.__gen())) if c
            )
        )

    def sum(self, other):
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError
        return Matrix(
            self.rows,
            self.cols,
            lambda: (
                (i // self.cols, i % self.cols, c)
                for i, c in enumerate(map(add, self.__gen(), other.__gen())) if c
            )
        )

    def subt(self, other):
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError
        return Matrix(
            self.rows,
            self.cols,
            lambda: (
                (i // self.cols, i % self.cols, c)
                for i, c in enumerate(map(sub, self.__gen(), other.__gen())) if c
            )
        )

    def transpose(self):
        return Matrix(
            self.cols,
            self.rows,
            lambda: sorted(
                ((i % self.cols, i // self.cols, c) for i, c in enumerate(self.__gen()) if c),
                key=lambda c: c[0]
            )
        )

    def __repr__(self):
        return '\n'.join([f'{row}' for row in zip(*[self.__gen()] * self.cols)])


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
