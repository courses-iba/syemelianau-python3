from ch09_functions import gen_stream


# Classes: Practical Task 1
class Matrix:
    def __init__(self, rows, columns, gen):
        self.rows = rows
        self.cols = columns
        self.data = {(row, col): val for row, col, val in gen() if val}

    def __get(self, row, col):
        return self.data.get((row, col)) or 0

    def __operation(self, rows, cols, operation):
        return Matrix(
            rows,
            cols,
            lambda: (operation(row, col) for row in range(self.rows) for col in range(self.cols))
        )

    def mult(self, other):
        if self.cols != other.rows:
            raise ValueError
        return self.__operation(
            self.rows,
            other.cols,
            lambda row, col: (row, col, sum(self.__get(row, i) * other.__get(i, col) for i in range(self.cols)))
        )

    def mult_scalar(self, scalar):
        return self.__operation(
            self.rows,
            self.cols,
            lambda row, col: (row, col, self.__get(row, col) * scalar)
        )

    def sum(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError
        return self.__operation(
            self.rows,
            self.cols,
            lambda row, col: (row, col, self.__get(row, col) + other.__get(row, col))
        )

    def subt(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError
        return self.__operation(
            self.rows,
            self.cols,
            lambda row, col: (row, col, self.__get(row, col) - other.__get(row, col))
        )

    def transpose(self):
        return self.__operation(
            self.cols,
            self.rows,
            lambda row, col: (col, row, self.__get(row, col))
        )

    def __repr__(self):
        return '\n'.join([f'{row}' for row in zip(*[gen_stream(self.rows * self.cols, (
            (self.cols * row + col, self.__get(row, col))
            for row in range(self.rows) for col in range(self.cols)
            if self.__get(row, col)
        ))] * self.cols)])


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
