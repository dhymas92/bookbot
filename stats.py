def count_words(book):
    words= book.split()
    return len(words)

#Add a new function to your stats.py
#file that takes the text from the book
#as a string, and returns the number of
#times each character, (including symbols and spaces), appears in the string.
def count_chars(book):
    char_count = {}
    for char in book:
        low_char = char.lower()
        if low_char in char_count:
            char_count[low_char]+=1
        else:
            char_count[low_char]=1
    return char_count

def sort_on(dict):
    return dict["num"]

def sorted_char_dict (dict):
    list_of_dicts = []
    for char in dict:
        if char.isalpha():
            list_of_dicts.append({"char": char, "num": dict[char]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
