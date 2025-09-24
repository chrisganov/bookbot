import sys
from stats import format_char_count, get_text_size, get_char_count

def get_book_text(file_path: str) -> str:
  with open(file_path) as f:
    file_content = f.read()
    return file_content

def main():
  args = sys.argv;

  if len(args) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path = args[1]

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")

  book_content = get_book_text(path)

  book_size = get_text_size(book_content)
  char_size_dict = get_char_count(book_content)
  sorted_char_size = format_char_count(char_size_dict)

  print("----------- Word Count ----------")
  print(f"Found {book_size} total words")

  print("--------- Character Count -------")

  for item in sorted_char_size:
    char = item["char"]
    val = item["num"]

    if not char.isalpha():
      continue

    print(f"{char}: {val}")

  print("============= END ===============")

main()
