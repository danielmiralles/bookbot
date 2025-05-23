from stats import get_num_words, get_dict_characters, get_sorted_dict_characters
import sys


def get_book_text(filename):
    file_content = ""
    with open(filename) as f:
         file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    content = get_book_text(book)
    num_words = get_num_words(content)
    dict_characters = get_sorted_dict_characters(get_dict_characters(content))
    print_dict = ""
    for dict_actual in dict_characters:
        char = dict_actual["char"]
        num = dict_actual["num"]
        print_dict += f"{char}: {num}\n"
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{print_dict}============= END ===============
""")

main()

