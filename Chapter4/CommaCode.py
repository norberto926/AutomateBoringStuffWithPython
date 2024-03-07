spam = ['apples', 'bananas', 'tofu', 'cats']

def CommaCode(given_list):
    string = ""
    for index, word in enumerate(given_list):
        if index == len(given_list) - 1:
            string = string + "and "  + word
        else:
            string += word + ", "
            
    return string


print(CommaCode(spam))
        