from stats import get_word_count, get_char_count, get_sorted_char_count
import sys

def get_book_text (filepath):
    with open(filepath) as f:
        content = f.read()
        return content
    
def main(args):
    if len(args) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    filepath = args[1]
    book = get_book_text(filepath)
    
    word_count = get_word_count(book=book)
    char_count = get_char_count(book=book)
    sorted_chars = get_sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")



if __name__ == "__main__":
    main(sys.argv)