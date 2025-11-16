import sys

def sort_on(item):
    return item[1]

def get_num_words(file_path):
    with open(f"{file_path}") as file:
        content = file.read()
        words_count = len(content.split())
        dictionary = {}
        letters_count = 0
        
        for letter in content:
            if letter.isalpha():
                letters_count += 1
                letter = letter.lower()
                if letter in dictionary:
                    dictionary[letter] += 1
                else:
                    dictionary[letter] = 1
        
        list_letters = []
        for key in dictionary:
            list_letters.append((key, dictionary[key]))
        list_letters.sort(key=sort_on, reverse=True)
        
        # Print formatted output
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")
        
        for item in list_letters:
            letter, frequency = item
            print(f"{letter}: {frequency}")
        
        print("============= END ===============")