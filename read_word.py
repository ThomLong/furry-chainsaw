import os
# read the file & return list of string


def read_file(file_path):
    with open(file_path, "r", encoding='utf8') as file:
        word = file.read()
        word = word.lower()
    return word
# splits & seperates special characters


def get_words(row):
    new = ""
    for sign in row:
        if sign.isalpha() or sign == "\n" or sign == "\t" or sign == "-"\
                or sign == " ":
            new = new + sign
    return new.split()
# returns list of words in string


def clean(word):
    new_lst = []
    for w in word:
        if len(w) == 1 and not w[0] == 'a' and not w[0] == 'i':
            continue
        if len(w) > 1 and w[0].isalpha():
            new_lst.append(w)
    return new_lst
# function to save all the words from list


def save_words(file_path, word):
    with open(file_path, "w") as file:
        for w in word:
            file.write(w + '\n')


# main program
# file path
home = os.getcwd()
home = os.chdir(home + "/src/large_texts.txt")
home = os.getcwd()
path_1 = home + "/holy_grail.txt"
rows_1 = read_file(path_1)
words = get_words(rows_1)
clean_words = clean(words)
print(f'\nRead {len(rows_1)} lines from file {path_1}')

# saving words to new file
outpath_1 = home + "/words_holygrail.txt"
save_words(outpath_1, clean_words)
print(f'saved {len(clean_words)} words in file {outpath_1}')
print()
# opening and collecting the words from the path file:
path_2 = home + "/eng_news_100K-sentences.txt"
rows_2 = read_file(path_2)
words1 = get_words(rows_2)
clean_words1 = clean(words1)
print(f'\nRead {len(rows_2)} lines from file {path_2}')
# saving words to news file
outpath_2 = home + "/words_100k.txt"
save_words(outpath_2, clean_words1)
print(f'saved {len(clean_words1)} words in file {outpath_2}')
