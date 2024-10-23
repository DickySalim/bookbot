book_path = "books/frankenstein.txt"


def main(path):
    file_contents = read_book(path)
    words = split_word(file_contents)
    word_count = len(words)
    character_count = count_character(file_contents)
    character_list = build_list(character_count)
    character_list.sort(reverse=True, key=sort_on)

    print()
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for entry in character_list:
        print(f"The '{entry["char"]}' character was found '{entry["count"]}' times")
    print()
    print("--- End Report ---")
    print()

    

def read_book(path):
    with open(path) as book:
        file_contents = book.read()
        return file_contents
    

def split_word(file_contents):
    words = file_contents.split()
    return words


def count_character(file_contents):
    lowered_string = file_contents.lower()
    characters = list(lowered_string)
    character_count = {}
    for char in characters:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count


def build_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_dict_items = {"char": char, "count": count}
        char_list.append(char_dict_items)
    return char_list


def sort_on(dict):
    return dict["count"]



main(book_path)