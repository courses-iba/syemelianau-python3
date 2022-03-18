# Strings: Practical Task 1
def remove_dots_quotas(text):
    return text.replace('.', '').replace('"', '')


print(remove_dots_quotas('Write a simple function which removes dots and "double quotes" from input text.'))


# Strings: Practical Task 2
def border_string(s):
    string = f'# {s} #'
    border = '#' * len(string)
    result = f'{border}\n{string}\n{border}'
    return result


print(border_string('some string'))


# Strings: Practical Task 3
def unborder_string(s):
    length = s.find('\n') + 1
    string = s[length:-length].replace('#', '').strip()
    return string


print(unborder_string(border_string('_some string_')))


# Strings: Practical Task 4
def normalize_name(s):
    return ' '.join(s.split()).title()


print(normalize_name(' sir Arthur Conan Doyle '))
print(normalize_name('sir    Arthur Conan  Doyle'))
