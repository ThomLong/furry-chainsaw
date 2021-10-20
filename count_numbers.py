# returns the different occurrencies from a file and how many time they appear
import os


def cleaning_file(file, banned):
    lst = []
    render_list = []
    with open(file, 'r') as brut:
        for entry in brut:
            lst.append(entry.split(banned))

        for entry in lst:
            for c in entry:
                render_list.append(int(c))

    return render_list


def count_diff(lst):
    numbers = set(lst)

    return len(numbers)


def count_occurrencies(lst):
    order = sorted(lst)
    counters = []
    numbers = set(lst)
    numbers = list(numbers)
    occurrencies = {}
    output = {}

    for c in numbers:
        counters.append(order.count(c))

    for c in range(len(counters)):
        occurrencies[numbers[c]] = counters[c]

    reverse = sorted(occurrencies.items(), key=lambda x: x[1], reverse=True)

    for i in range(10):
        sort = {reverse[i][0]: reverse[i][1]}
        output.update(sort)
    return output


hun_thou = os.getcwd() + '/src/large_texts.txt/eng_news_100K-sentences.txt-copy.txt'
holy_grail = os.getcwd() + '/src/large_texts.txt/holy_grail.txt-copy.txt'

different_hun_thou = count_diff(hun_thou)
count_hun_thou = count_occurrencies(hun_thou)

different_grail = count_diff(holy_grail)
count_grail = count_occurrencies(holy_grail)

print(different_A, different_B)
print(count_A, count_B)
