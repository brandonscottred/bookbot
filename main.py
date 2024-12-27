def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()
        counter = len(words)
        print(counter)

        lowered_file_contents = file_contents.lower()
        character_dict = {}
        for char in lowered_file_contents:
            if char.isalpha():
                if char in character_dict:
                    character_dict[char] += 1
                else:
                    character_dict[char] = 1
        print(character_dict)

        char_list = [{"char": char, "count": character_dict[char]} for char in character_dict]
        char_list.sort(reverse=True, key=lambda x: x["count"])

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{counter} words found in the document")

        for entry in char_list:
            char = entry["char"]
            count = entry["count"]
            print(f"The '{char}' character was found {count} times")

        print("--- End Report ---")

main()
