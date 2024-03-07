def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(str):
    words = str.split()
    return len(words)


def letter_counter(text):
    letters = {}
    arr = []
    for letter in text.lower():
        if not letter.isalpha():
            continue
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    for l in letters:
        arr.append({"name": l, "num": letters[l]})
    return arr


def sort_on(d):
    return d["num"]


def print_report(text):
    count = word_count(text)
    letters = letter_counter(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    letters.sort(reverse=True, key=sort_on)
    for obj in letters:
        print("The '{}' character was found {} times".format(obj["name"], obj["num"]))
    print("--- End Report ---")


main()
