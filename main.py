def main():
    with open("bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letters = ct_let(file_contents)
        sorted_letters = check(letters)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for letter in sorted_letters:
            print(f"The '{letter['letter']}' character was found {letter['count']} times")
        print("--- End report ---")


def count_words(tekst):
    words = tekst.split()
    return len(words)

def ct_let(tekst):
    lowered_string = tekst.lower()
    ltsc = {}

    for t in lowered_string:
        if t.isalpha():
            if t in ltsc:
                ltsc[t]+=1
            else:
                ltsc[t] =1
    return ltsc
def check(letter_dict):
    letter_list = [{'letter': k, 'count': v} for k, v in letter_dict.items()]

    letter_list.sort(reverse=True, key=lambda x: x['count'])

    return letter_list
     

main()