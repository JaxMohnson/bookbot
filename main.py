def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    count_words = get_count_of_words(text)
    count_letters = get_count_of_characters(text)
    sorted_list = dict_to_list_sort(count_letters)
    print("fucntion 1: print book info")
    print(text)
    print("function 2: count the # of words in the book")
    print(f"There are {count_words} words in this book")
    print("function 3: count the # of characters in the book")
    print(count_letters)


    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_of_words(text):
    count = len(text.split())
    return count

def get_count_of_characters(text):
    letters_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in letters_dict:
            letters_dict[lowered] += 1
        else:
            letters_dict[lowered] = 1
    return letters_dict

def dict_to_list_sort(letters_dict):
    sorted_list = []
    for ch in letters_dict:
        sorted_list.append({"char": ch, "num": letters_dict[ch]})
    return sorted(sorted_list, key=lambda x: x['num'])

main()