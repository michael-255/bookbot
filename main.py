
def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def sort_on(dict):
    return dict["num"]


def count_characters(file_contents):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z']
    char_memo = {}
    file_contents = file_contents.lower()
    for c in file_contents:
        if c in char_memo:
            char_memo[c] += 1
        else:
            char_memo[c] = 1

    char_list = []
    for key in char_memo:
        if key in characters:
            char_list.append({
              "name": key,
              "num": char_memo[key],
            })

    char_list.sort(reverse=True, key=sort_on)
    return char_list


def print_report(file_path, file_contents):
    word_count = count_words(file_contents)
    char_list = count_characters(file_contents)

    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(file_contents)} words found in the document\n")

    for x in char_list:
        print(f"The '{x["name"]}' character was found {x["num"]} times")

    print("--- End report ---")


file_path = "books/frankenstein.txt"
with open("books/frankenstein.txt") as f:
    file_contents = f.read()


print_report(file_path, file_contents)
