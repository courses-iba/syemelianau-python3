# Dictionaries: Practical Task 1
def swap_dict(d):
    swapped_dict = {}
    for key, value in d.items():
        swapped_dict[value] = swapped_dict.get(value, tuple()) + (key,)
    return swapped_dict


print(swap_dict({1: 2, 3: 4, 5: 4, 7: 2, 9: 4}))


# Dictionaries: Practical Task 2
def compact_dict(d):
    comp_dict = {}
    for key, value in swap_dict(d).items():
        comp_dict[value] = key
    return comp_dict


print(compact_dict({1: 2, 3: 4, 5: 4, 7: 2, 9: 4}))
