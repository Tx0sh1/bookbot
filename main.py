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

print(char_count)

def formatted_output():
    for char in char_count:
        print(char)
        
formatted_output()
               
