import random

def get_random_word():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0, len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print(character, end="")
    print("")
    
def get_guess():
	print("Enter a letter: ")
	return input()

def process_letter(letter, secret_word, blanked_word):
    result = False
    
    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter # (2) ...and this line here should now work
    
    return result

def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True
    
    word = get_random_word()
    blanked_word = list("_" * len(word)) # (1) I'll convert the string to a list...
    
    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)
        
        if not found:
            strikes += 1
        
        if strikes >= max_strikes:
            playing = False
            
    if strikes >= max_strikes:
        print("Loser!")
    else:
        print("Winner!")

print("Game started")
play_word_game()
print("Game over")