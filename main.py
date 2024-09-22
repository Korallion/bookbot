def get_character_counts(text):
    lower_case_text = text.lower()
    char_counts = {}

    for char in lower_case_text:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts

def get_word_count(text):
    return len(text.split())

def convert_dict_to_array(dict):
    dict_array = []

    for key in dict.keys():
        dict_to_append = {"character": key, "num": dict[key]}
        dict_array.append(dict_to_append)

    return dict_array

def sort_on_num(dict):
    return dict["num"]

def get_book_report(text):
    word_count = get_word_count(text)
    dict_char_counts = get_character_counts(text)
    array_char_counts = convert_dict_to_array(dict_char_counts)

    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{word_count} words found in the document\n\n"
    
    array_char_counts.sort(reverse=True, key=sort_on_num)

    for dict in array_char_counts:
        char = dict["character"]
        num = dict["num"]
        
        if char.isalpha():
            report += f"The '{char}' character was found {num} times\n"

    report += "--- End report ---\n"

    return report
    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report = get_book_report(file_contents)
        print(report)

main()
