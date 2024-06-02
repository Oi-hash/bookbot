import sys

def main():
    
    try:
        with open('books/frankenstein.txt') as f: # sys.argv[1]
            file_contents = f.read()
    
    except IndexError:
        print(f'Usage: main.py bookpath/book.txt')

    except FileNotFoundError:
        print(f'File has not been found')

    output = file_contents.split()

    print(f'### Stats of {f.name} ')
    words = count_word(output)
    characters = count_characters(output)
    print(f'# Words found: {words}')
    print(f'# Characters found: {characters}')
    return 

def sort_on(dict):
    return dict["sum"]

def count_characters(list):
    characters_list = [
        {"letter": chr(x + 97), "sum" : 0} for x in range(26)
    ]
    for element in list:
        if element.isalpha():
            for character in element.lower():
                val = ord(character) - 97
                characters_list[val] = {"letter" : character, "sum" : characters_list[val].get("sum") + 1}                
    
    characters_list.sort(reverse=True, key=sort_on)
    characters_sum = 0
    for letter in characters_list:
        characters_sum = characters_sum + letter["sum"]
        print(f'# [{letter["letter"]}] has been founded {letter["sum"]} times')
    return characters_sum

def count_word(list):
    return len(list)

main()
