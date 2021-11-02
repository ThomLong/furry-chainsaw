import HashSet as hset
import BstMap as bst
import os

# Program starts


def read_file(file_path):
    with open(file_path, "r", encoding='utf8') as file:
        words = []
        for word in file:
            words.append(word[:-1])
    return words


# Initialize word set
words_100 = hset.HashSet()   # Create new empty HashSet
words_100.init()             # Initialize with eight empty buckets

holy_words = hset.HashSet()   # Create new empty HashSet
holy_words.init()

total_words = hset.HashSet()   # Create new empty HashSet
total_words.init()

map_100 = bst.BstMap()
holy_map = bst.BstMap()
whole_map = bst.BstMap()

# get my paths to the documents
home = os.getcwd()
home = os.chdir(home + "/src/large_texts.txt")
home = os.getcwd()

path_100 = home + '/words_100k.txt'
holy_path = home + '/words_holygrail.txt'
rows_100 = read_file(path_100)
holy_rows = read_file(holy_path)

for word in rows_100:
    words_100.add(word)
    if len(word) >= 4:
        value = map_100.get(word)
        if value is None:
            map_100.put(word, 1)
        else:
            value += 1
            map_100.put(word, value)

for word in holy_rows:
    holy_words.add(word)
    if len(word) >= 4:
        value = holy_map.get(word)
        if value is None:
            holy_map.put(word, 1)
        else:
            value += 1
            holy_map.put(word, value)

top_100 = sorted(map_100.as_list(), key=lambda x: x[1], reverse=True)[:10]
holy_top = sorted(holy_map.as_list(), key=lambda x: x[1], reverse=True)[:10]

print('The 100K setences file has ', words_100.size, ' unique words.')
print('The top 10 occurrences are ', top_100)
print('Max bucket size for all the words: ', words_100.max_bucket_size())
print('Max depth in the BST for all the words: ', map_100.max_depth())

print('\nThe holy Grail script has ', holy_words.size, ' unique words.')
print('The top 10 occurrences are ', holy_top)
print('Max bucket size for all the words is: ', holy_words.max_bucket_size())
print('Max depth in the BST for all the words is: ', holy_map.max_depth())
