import string

def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
    texts = file_contents.split()
    num_words = len(texts)
    print(f"Found {num_words} total words")
    return file_contents

def get_num_of_chars(file_contents):
    new_file_contents = list(str(file_contents.lower()))
    letters = dict.fromkeys(string.ascii_lowercase, 0)
    for char in new_file_contents:
        if char in letters:
            letters[char] += 1
    
    return letters

def get_it_sorted(letters):
    char_list = dict(sorted(letters.items(), key = lambda x:x[1], reverse = True))    
    return char_list