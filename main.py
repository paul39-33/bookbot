import sys
from stats import *

def main():
    path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    book = get_num_words(path)
    print("--------- Character Count -------")
    char_dict = get_num_of_chars(book)
    char_list = get_it_sorted(char_dict)
    for key, value in char_list.items():
        print(f"{key}: {value}")
    print("============= END ===============")
    #print(get_book_text("books/frankenstein.txt"))

#if __name__ == "__main__":
#    if len(sys.argv) < 2:
#        print("Usage: python3 main.py <file_path>")
#        sys.exit(1)

#    file_path = sys.argv[1]
#    main(file_path)
main()