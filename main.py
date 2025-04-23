import sys
from stats import count_words
from stats import count_chars
from stats import sorted_char_dict

def get_book_text(bookpath):
    with open(bookpath) as f:
        book_content = f.read()
    return book_content

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book = get_book_text(book_path)
        num_words = count_words(book)
        char_dict = count_chars(book)
        sorted_alpha_list = sorted_char_dict(char_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for char_dict in sorted_alpha_list:
            print(f"{char_dict['char']}: {char_dict['num']}")

        print("============= END ===============")


main()
