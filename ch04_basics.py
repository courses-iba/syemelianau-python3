import math


# The basics: Practical Task 1
def get_day_week(day, starting_dotw):
    return (starting_dotw + day - 2) % 7 + 1


print(get_day_week(7, 3))


# The basics: Practical Task 2
def count_digits(n):
    return math.ceil(math.log10(n + .1))


print(count_digits(123456789))
