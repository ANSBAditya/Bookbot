from stats import *


def main():
    book_content = get_book_text("books/frankenstein.txt")
    sorted_list = get_sorted_list(get_char_count_dict(book_content))
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt..")
    print("----------- Word Count ----------")
    print(num_words(book_content))
    print("--------- Character Count -------")
    
    #to print output of each alpha occurance in the format:
    # 'char: count'
    for element in sorted_list:
        if element["char"].isalpha():
            print(f"{element['char']}: {element['num']}", end='\n')
    
    print("============= END ===============")



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents


main()
