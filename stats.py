from typing import Literal, TypedDict


CharCount = dict[str , int]

class FormattedCharCount(TypedDict):
  char: str
  num: int

def get_text_size(text: str) -> int:
  text_split = text.split()

  return len(text_split)

def get_char_count(text: str) -> CharCount:
  char_dict_count: CharCount = {}

  word_arr = text.split()

  for word in word_arr:
    lower_case = word.lower()
    char_arr = list(lower_case)

    for char in char_arr:
      if char in char_dict_count:
        char_dict_count[char] = char_dict_count[char] + 1

      else:
        char_dict_count[char] = 1



  return char_dict_count


def sort_by_key(key: Literal["num", "char"]):
  def sort_dict(dict: FormattedCharCount):
    return dict[key]

  return sort_dict


def format_char_count(char_count: CharCount) -> list[FormattedCharCount]:
  formatted_dict: list[FormattedCharCount] = []

  for key in char_count:
    value = char_count[key]

    formatted_dict.append({"char": key, "num": value})

  formatted_dict.sort(key=sort_by_key("num"), reverse=True)

  return formatted_dict;
