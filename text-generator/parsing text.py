import time
start_time = time.time()

START_ID = 0


class Word:
    len = 0
    freq = 0
    id = 0
    text = 0
    next = ''
    prev = ''

    def __init__(self, word):
        global START_ID
        global word_list
        self.text = word
        self.id = START_ID
        START_ID += 1
        self.len = len(word)
        self.freq = word_list.count(word)

    def __str__(self):
        return self.text


def get_indices(word):
    global word_list
    indices = [i for i, x in enumerate(word_list) if x == word]
    return indices


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


def check_neigh(word):
    global word_list
    next_list = []
    prev_list = []

    indices = get_indices(word.text)
    global word_list
    for ind in indices:
        if ind == len(word_list)-1:
            next_list.append('')
        else:
            next_list.append(word_list[ind+1])

        if ind == 0:
            prev_list.append('')
        else:
            prev_list.append(word_list[ind - 1])
    return get_common(prev_list), get_common(next_list)

f = open("example.txt")

nonletter_set = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '.', ',', '!', '(', ')', '-', '?', '"', '\'', ';', ':', 'X', 'I', chr(10))

# print chr(208), chr(209)

letter_count = 0
word_list = []
for line in f:
    if len(line) == 1:
        continue
    for nonletter in nonletter_set:
        line = line.replace(nonletter, '')

    for word in line.split(' '):
        if word == '' or word == ' ':
            continue
        word_list.append(word)
f.close()
word_set_temp = set(word_list)

word_set = [Word(text) for text in word_set_temp]

'''
for word in word_set:
    print word.id, word.freq, word.text
'''

for word in word_set:
    word.prev, word.next = check_neigh(word)
    print word.prev, word, word.next

print time.time() - start_time





