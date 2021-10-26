# returns the different occurrencies from a file and how many time they appear
import os


def read_file(file_path):
    with open(file_path, "r", encoding='utf8') as file:
        words = []
        for word in file:
            words.append(word[:-1])
    return words


def count_diff(lst):
    words = set(lst)

    return len(words)


def count_occurrencies(lst):
    setlist = set(lst)
    order = sorted(lst)
    counters = []
    occurrences = {}
    output = {}

    for i in range(len(order)):
        if order[i] in occurrences:
            occurrences[order[i]] += 1
        else:
            occurrences[order[i]] = 1
    reverse = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)[:5]
    return reverse

home = os.getcwd()
home = os.chdir(home + "/src/large_texts.txt")
home = os.getcwd()

path_100 = home + '/words_100k.txt'
holy_path = home + '/words_holygrail.txt'
rows_100 = read_file(path_100)
holy_rows = read_file(holy_path)

different_100k = count_diff(rows_100)
count_100k = count_occurrencies(rows_100)

different_grail = count_diff(holy_rows)
count_grail = count_occurrencies(holy_rows)

print(different_100k, count_100k)
print(different_grail, count_grail)
