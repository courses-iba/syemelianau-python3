# Lists, tuples and sets: Practical Task 1
def remove_3_largest(lst):
    cp = lst.copy()
    cp.reverse()
    cp.remove(max(cp))
    cp.remove(max(cp))
    cp.remove(max(cp))
    cp.reverse()
    return cp


print(remove_3_largest([1, 2, 3, 1, 2, 3]))


# Lists, tuples and sets: Practical Task 2
def get_unique_lists_num(a, b, c, d):
    return len(set(map(tuple, [a, b, c, d])))


print(get_unique_lists_num(
    [1, 2, 3],
    [1, 2, 3],
    [3, 4, 5],
    [3, 2, 1]
))


# Lists, tuples and sets: Practical Task 3
def get_max_common(a, b):
    return max(set(a) & set(b), default=0)


print(get_max_common([1, 3, 2], [5, 6, 3]))
print(get_max_common([1, 2, 3], [4, 5, 6]))
