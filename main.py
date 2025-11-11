from stats import num_words


def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(num_words(book_content))


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents


main()
