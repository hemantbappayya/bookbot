FILE_PATH= "books/frankenstein.txt"


def count_words(text: str):
    return len(text.split())

def count_char_rep(text: str):
    lower_case = text.lower()

    char_dct ={}
    for char in lower_case:
        if char not in char_dct:
            char_dct[char] = 1
        
        else:
            char_dct[char] +=1

    return char_dct

def list_dct(dct: dict):
    new_lst=[]

    for key in dct:
        new_key = str(key)
        new_dct ={}
        if new_key.isalpha():
            new_dct["character"] = key
            new_dct["count"] = dct[key]
            new_lst.append(new_dct)
        else: 
            pass

    return new_lst

def sort_on(dict):
    return dict["count"]
        


def main():
    with open(file=FILE_PATH) as f:
        file_contents = f.read()

    # print(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print ("")
    
    char_rep = count_char_rep(file_contents)
    dct_lst = list_dct(char_rep)
    dct_lst.sort(reverse=True, key= sort_on)

    for dct in dct_lst:
        
        char = dct["character"]
        count = dct["count"]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
