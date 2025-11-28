def count_words(book_content):

    wordlist = book_content.split()
    num_words = len(wordlist)

    print(f"Found {num_words} total words")

    return len(wordlist)

def count_chars(book_content):

    char_dict = {}

    for char in book_content.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def sort_list(dict):

    sorted_list = []

    for char in dict:
        
        #Creating the dict inside the loop to refresh and not keep same value over iterations
        sorted_dict = {}
        
        # Defining the original dicts values
        num = dict[char]  

        # Adding the original values to the new sorted dictionary
        sorted_dict["char"] = char
        sorted_dict["num"] = num
        sorted_list.append(sorted_dict)
        
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def sort_on(dict):
    return dict["num"]