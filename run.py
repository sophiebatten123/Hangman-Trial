from words import word_list
import random

def get_word():
    """
    This function generates a random word from the list 
    it then returns the variable once it has been ran
    """
    word = random.choice(word_list)
    
    return word

def make_board(word):
    word_grid = "_" * len(word)
    letters = list(word)
    grid = list(word_grid)

    print(letters)
    print(grid)

    return word_grid

def main():
    word = get_word()
    make_board(word)

print("Welcome to Hangman!")
print("To begin playing you must first guess a letter contained within the word:\n")
main()