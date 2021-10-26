import HashSet as hset
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

for word in holy_rows:
    holy_words.add(word)

print('The 100K setences file has ', words_100.size, ' unique words.')
print('The holy Grail script has ', holy_words.size, ' unique words.')

