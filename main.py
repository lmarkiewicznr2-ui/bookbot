import sys
from stats import get_num_words,get_char_counts,sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        char = entry["char"]
        count = entry["num"]
        if char.isalpha():  # Skip non-alphabetic characters
            print(f"{char}: {count}")
    print("============= END ================")
if __name__ == "__main__":
    main()

    