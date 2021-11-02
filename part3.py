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
    total_words.add(word)
    map_100.put(word, len(word))
    whole_map.put(word, len(word))

for word in holy_rows:
    holy_words.add(word)
    total_words.add(word)
    holy_map.put(word, len(word))
    whole_map.put(word, len(word))

lst_100 = map_100.as_list()
holy_list = holy_map.as_list()

print('The 100K setences file has ', words_100.size, ' unique words.')
print('Max bucket size for all the words: ', total_words.max_bucket_size())
print('Max depth in the BST for all the words: ', whole_map.max_depth())
print('The holy Grail script has ', holy_words.size, ' unique words.')
