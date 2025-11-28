from stats import count_words, count_chars, sort_list
import importlib
import sys

def get_book_text(book):
    try:
        with open(book) as f:
            book_content = f.read()
    except Exception as e:
        print(f"Der skete en fejl: ", e)
    

    return book_content

def print_output(book_path, wordcount, list):

    lines = "" 
    
    for item in list:
        num = item["num"]
        char = item["char"]

        if char.strip() == "" and char.isalpha() == False:
            continue

        lines += f"{char}: {num} \n    "


    user_output = f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {wordcount} total words
    --------- Character Count -------
    {lines}
    ============= END ===============
    """

    return user_output

def analyze_book(book_path):

    book = get_book_text(book_path)
    wordcount = count_words(book)
    chars = count_chars(book)
    sorted_list = sort_list(chars)
    user_output = print_output(book_path, wordcount, sorted_list)

    return user_output

def main():

    try:
        if sys.argv[1]:
            book_path = sys.argv[1]
            print(book_path)
            print(analyze_book(book_path))

    except IndexError as e:
            print("Too few parameter - include a book. Usage: python3 main.py <path_to_book>", e)
            sys.exit(1)

    except UnboundLocalError as e:
        print("Fejl: ", e)

main()