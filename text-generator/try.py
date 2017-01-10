number_list = [6, 2, 3, 4, 5, 2, 3, 5, 3]
number = 'Hello'

def get_common(array):
    if not array:
        return ''
    common_elem = array[0]
    most_freq = 1
    for elem in array:
        elem_freq = array.count(elem)
        if elem_freq > most_freq:
            most_freq = elem_freq
            common_elem = elem
    return common_elem

indices = [i for i, x in enumerate(number_list) if x == number]

print get_common(number_list)