def count_book_words(book_text):
    return len(book_text.split())

def count_book_chars(book_text):
    book_text = book_text.lower()
    char_dict = {}
    for char in book_text:
        if char in char_dict:
            char_dict[char] += 1
        else: char_dict[char] = 1
    return(char_dict)

def get_num_key(dict_to_pull):
    return dict_to_pull["num"]

def sort_results(char_dict):
    dict_list = []
    for key in char_dict:
        if not key.isalpha():
            continue
        dict_to_add = {}
        dict_to_add["char"] = key
        dict_to_add["num"] = char_dict[key]
        dict_list.append(dict_to_add)
    
    dict_list.sort(key=get_num_key, reverse=True)
    return dict_list

def write_results(dict_list):
    for pair in dict_list:
        print(f"{pair["char"]}: {pair["num"]}")