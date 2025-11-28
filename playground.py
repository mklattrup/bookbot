dict = {'\ufeff': 1, 't': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7631, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}

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

print(sort_list(dict))