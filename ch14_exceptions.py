from functools import reduce


# Exceptions: Practical Task 1
def retrieve_age(person):
    try:
        age = int(person['age'])
        if age < 0:
            raise ValueError()
        return age
    except ValueError:
        print('ValueError')
    except KeyError:
        print('KeyError')
    except TypeError:
        print('TypeError')


print(retrieve_age({'age': 22}))
print(retrieve_age({'age': -22}))
print(retrieve_age({}))
print(retrieve_age([]))


# Exceptions: Practical Task 2
def parse_id3v2(file_path):
    header_size, tag_data = 10, []
    encoding = {
        0: 'ISO-8859-1',
        1: 'UTF-16',
        2: 'UTF-16BE',
        3: 'UTF-8'
    }
    try:
        with open(file_path, 'rb') as file:
            tag_header = file.read(header_size)

            if tag_header[:3] != b'ID3':
                return tag_data
            elif tag_header[3] not in [3, 4]:
                return tag_data
            elif tag_header[5] & 64 == 64:
                return tag_data

            tag_body_size = reduce(lambda a, b: a * 128 + b, tag_header[-4:], 0)
            total = 0
            while True:
                frame_header = file.read(header_size)
                frame_id = frame_header[:4]
                frame_size = reduce(lambda a, b: a * (128 if tag_header[3] == 4 else 256) + b, frame_header[4:8], 0)
                if not frame_size:
                    break
                frame_body = file.read(frame_size)
                try:
                    frame_body_encoded = frame_body[1:].decode(encoding[frame_body[0]])
                except UnicodeDecodeError:
                    frame_body_encoded = None
                tag_data.append((frame_id, frame_size, frame_body, frame_body_encoded))
                total += frame_size + header_size
                if tag_body_size - total < header_size:
                    break
    except FileNotFoundError:
        return tag_data
    except IOError:
        return tag_data
    return tag_data


print(parse_id3v2('ch14_ariya_ulitsa_roz.mp3'))
print(parse_id3v2('ch14_ariya_produmai_svetlii_mir.mp3'))
print(parse_id3v2('ch14_therion_dreams_of_swedenborg.mp3'))
