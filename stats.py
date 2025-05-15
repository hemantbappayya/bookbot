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
            new_dct["char"] = key
            new_dct["num"] = dct[key]
            new_lst.append(new_dct)
        else: 
            pass
    
    new_lst.sort(reverse=True, key= lambda dct: dct["num"])
    return new_lst