import sys
from stats import *

def main():
    path = "books/frankenstein.txt"
    get_num_words(path)
    get_num_of_chars(path)
    #print(get_book_text("books/frankenstein.txt"))

#if __name__ == "__main__":
#    if len(sys.argv) < 2:
#        print("Usage: python3 main.py <file_path>")
#        sys.exit(1)

#    file_path = sys.argv[1]
#    main(file_path)
main()