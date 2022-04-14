from operator import add, sub, mul
from ch09_functions import gen_stream


# Classes: Practical Task 1
class Matrix:
    def __init__(self, rows, columns, gen):
        self.rows = rows
        self.cols = columns
        self.data = tuple(tuple(gen_stream(
            rows * columns,
            [cell for cell in gen()],
            self.__extractor
        ))[i:i + columns] for i in range(0, rows * columns, columns))

    def __extractor(self, cell):
        row, col, val = cell
        if row >= self.rows or col >= self.cols:
            raise ValueError
        return row * self.cols + col, val

    def __operator(self, other, operation):
        return tuple(tuple(map(operation, self.data[i], other[i])) for i in range(len(self.data)))

    def __operate(self, other, operation):
        rows = len(other)
        cols = len(other[0]) if rows else 0
        if self.rows != rows and self.cols != cols:
            raise ValueError
        return self.__operator(other, operation)

    def mult(self, other):
        rows = len(other)
        if self.cols != rows:
            raise ValueError
        return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in zip(*other)) for row in self.data)

    def mult_scalar(self, scalar):
        return self.__operator(tuple((scalar,) * len(row) for row in self.data), mul)

    def sum(self, other):
        return self.__operate(other, add)

    def subt(self, other):
        return self.__operate(other, sub)

    def transpose(self):
        return tuple(zip(*list(self.data)))

    def __repr__(self):
        return '\n'.join([f'{row}' for row in self.data])


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

m = m.mult(m.transpose())
print(m)

m = Matrix(3, 3, lambda: ())
m_gen = Matrix(3, 3, gen)
m_gen_ex = Matrix(3, 3, gen_ex(3, 3))

print(m_gen_ex.sum(m_gen.data))
print(m_gen_ex.subt(m_gen.data))
print(m_gen_ex.mult_scalar(5))
