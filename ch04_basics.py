import math


# The basics: Practical Task 1
def get_day_week(day, starting_dotw):
    week_length = 7
    result = (starting_dotw + day - 1) % week_length
    return result if result else week_length


print(get_day_week(7, 3))


# The basics: Practical Task 2
def count_digits(n):
    if isinstance(n, int) and n > 0:
        return math.ceil(math.log10(n + .1))
    return 0


print(count_digits(123456789))
