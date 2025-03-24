import string

def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
    texts = file_contents.split()
    #print(f"texts : {texts}")
    num_words = len(texts)
    return print(f"{num_words} words found in the document")

def get_num_of_chars(path):
    with open(path) as f:
        file_contents = list(str(f.read().lower()))
    #print(f"file cntnt: {file_contents}")
    letters = dict.fromkeys(string.ascii_lowercase, 0)
    for char in file_contents:
        if char in letters:
            letters[char] += 1
    return print(f"result : {letters}")
