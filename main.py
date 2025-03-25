import sys
from stats import *

def main(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    book = get_num_words(path)
    print("--------- Character Count -------")
    char_dict = get_num_of_chars(book)
    char_list = get_it_sorted(char_dict)
    for key, value in char_list.items():
        print(f"{key}: {value}")
    print("============= END ===============")
    #print(get_book_text("books/frankenstein.txt"))

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

main(path)