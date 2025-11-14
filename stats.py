
def num_words(content):
    word_list = content.split()
    return f"Found {len(word_list)} total words"

def get_char_count_dict(content):
    char_log_dict = {}

    for char in content.lower():
        try:
            char_log_dict[char] += 1
        except KeyError:
            char_log_dict[char] = 1
    
    return char_log_dict

def get_sorted_list(char_dict):
    final_list = []

    for key in char_dict:
        list_element = {"char": key, "num": char_dict[key]}
        final_list.append(list_element)
    
    final_list.sort(reverse=True, key=sort_on)
    return final_list

def sort_on(element):
    return element["num"]
