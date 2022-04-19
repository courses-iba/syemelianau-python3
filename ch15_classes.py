from operator import add, sub
from ch09_functions import gen_stream


# Classes: Practical Task 1
class Matrix:
    def __init__(self, rows, columns, gen):
        self.rows = rows
        self.cols = columns
        self.data = tuple(cell for cell in gen())

    def __stream(self):
        return gen_stream(self.rows * self.cols, self.data, lambda cell: (cell[0] * self.cols + cell[1], cell[2]))

    def __matrix(self):
        return zip(*[iter(self.__stream())] * self.cols)

    def __operator(self, other, operation):
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError
        return Matrix(
            self.rows,
            self.cols,
            lambda: tuple(
                (int(index / self.cols), int(index % self.cols), cell)
                for index, cell in enumerate(map(operation, self.__stream(), other.__stream())) if cell
            )
        )

    def mult(self, other):
        if self.cols != other.rows:
            raise ValueError
        data = tuple()
        for i, row in enumerate(
                tuple(tuple(
                    sum(a * b for a, b in zip(row, col)) for col in zip(*other.__matrix())
                ) for row in self.__matrix())
        ):
            data += tuple((i, j, val) for j, val in enumerate(row) if val != 0)
        return Matrix(self.rows, other.cols, lambda: data)

    def mult_scalar(self, scalar):
        return Matrix(self.rows, self.cols, lambda: tuple((row, col, val * scalar) for row, col, val in self.data))

    def sum(self, other):
        return self.__operator(other, add)

    def subt(self, other):
        return self.__operator(other, sub)

    def transpose(self):
        return Matrix(
            self.cols,
            self.rows,
            lambda: tuple(sorted([(col, row, val) for row, col, val in self.data], key=lambda tup: tup[0]))
        )

    def __repr__(self):
        return '\n'.join([f'{row}' for row in self.__matrix()])


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
