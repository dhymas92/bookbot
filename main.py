def get_book_text(bookpath):
    with open(bookpath) as f:
        book_content = f.read()
    return book_content

def count_words(book):
    word_count = len(book.split())
    return word_count

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f"{num_words} words found in the document")
    #print(book.split('"\n"', ' '))




if __name__ == '__main__':
    main()
