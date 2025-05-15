from stats import *
import sys



def main():
    FILE_PATH= sys.argv[1]
    with open(file=FILE_PATH) as f:
        file_contents = f.read()

    # print(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FILE_PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")
        
    char_rep = count_char_rep(file_contents)    
    dct_lst = list_dct(char_rep)

    for dct in dct_lst:
        
        char = dct["char"]
        num = dct["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main()
