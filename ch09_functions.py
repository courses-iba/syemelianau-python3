from math import sin
from itertools import count


# Functions: Practical Task 1
def to_celsius(temperature_list):
    return list(map(lambda fahrenheit: round(5 / 9 * fahrenheit - 32, 2), temperature_list))


print(to_celsius([-30, 0, 5, 10, 21, 35]))


# Functions: Practical Task 2
def bold(func):
    def get_text_bold(*arg):
        return f'<b>{func(*arg)}</b>'

    return get_text_bold


def italic(func):
    def get_text_italic(*arg):
        return f'<i>{func(*arg)}</i>'

    return get_text_italic


def underline(func):
    def get_text_underline(*arg):
        return f'<u>{func(*arg)}</u>'

    return get_text_underline


@bold
@italic
@underline
def get_text():
    return 'hello world'


print(get_text())


# Functions: Practical Task 3
def fn(f, n):
    def callback(v):
        for _ in range(n):
            v = f(v)
        return v

    return callback


def fnr(f, n):
    return f if n == 1 else lambda v: v if n < 1 else fnr(f, n - 1)(f(v))


def golden_ratio(n):
    return fn(lambda i: 1 + 1 / i, n)(1)


f1 = fn(lambda x: 'sin(%s)' % x, 5)
f2 = fn(lambda x: sin(x), 5)

f3 = fn(lambda x: 'sin(%s)' % x, 5)
f4 = fn(lambda x: sin(x), 5)

print('%s = %f' % (f1('1'), f2(1)))
print('%s = %f' % (f1('2'), f2(2)))
print(fn(lambda x: sin(x), 0)(1000))

print('%s = %f' % (f3('1'), f4(1)))
print('%s = %f' % (f3('2'), f4(2)))
print(fnr(lambda x: sin(x), 0)(1000))

print(
    golden_ratio(0),
    golden_ratio(1),
    golden_ratio(2),
    golden_ratio(100)
)


# Functions: Practical Task 4
def gen_stream(total, sorted_iterable, extractor=lambda x: x):
    mapped = map(extractor, sorted_iterable)
    iterable = count() if total is None else range(total)
    item = next(mapped, None)
    for i in iterable:
        if item and i == item[0]:
            yield item[1]
            item = next(mapped, None)
        else:
            yield 0


def day_extractor(x):
    months = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    acc = sum(months[:x[1] - 1]) + x[0] - 1
    return acc, x[2]


print(list(gen_stream(9, [(4, 111), (7, 12)])))
print(list(gen_stream(59, [(3, 1, 4), (5, 2, 6)], day_extractor)))
