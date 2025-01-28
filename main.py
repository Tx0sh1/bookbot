def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents.lower()
    
def count_characters(letters):
    char = {}      
    for letter in letters:
        if letter.isalpha():
            char[letter] = char.get(letter, 0) + 1
    return char

letters = main()
char_count = count_characters(letters)

def formatted_output():
    
    print("--- Begin report of books/frankenstein.txt --- \n")
    for letter, count in char_count.items():
        print(f"{letter} appears {count} times")
    print("--- End report ---")
        
formatted_output()
               
