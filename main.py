from stats import get_num_words  # and any other needed functions
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]
get_num_words(file_path) 