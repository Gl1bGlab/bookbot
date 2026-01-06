import sys
from stats import count_book_chars, count_book_words, write_results, sort_results

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    path = sys.argv[1]
    print(f"Analyzing book found at {path}")
    book = get_book_text(path)

    print("----------- Word Count ----------")
    word_count = count_book_words(book)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_dict = count_book_chars(book)
    char_dict = sort_results(char_dict)
    write_results(char_dict)
    print("============= END ===============")
    pass

main()