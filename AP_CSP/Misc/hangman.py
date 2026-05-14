import sys
import time
import random

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m' 

WORD_BANK = {
    3: ["cat", "sun", "sky", "cup", "bat"],
    4: ["code", "fire", "blue", "wind", "game"],
    5: ["apple", "bread", "cloud", "dance", "earth"],
    6: ["python", "planet", "guitar", "silver", "winter"],
    7: ["desktop", "monitor", "kitchen", "picture", "weather"],
    8: ["keyboard", "mountain", "notebook", "universe", "calendar"],
    45: ["pneumonoultramicroscopicsilicovolcanoconiosis"] 
}

def typing_print(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush() 
        time.sleep(delay) 
    print() 

def spin_animation():
    symbols = ['@', '#', '$', '%', '&', '*', '?', '!', '>', '<']
    duration = 2 
    start_time = time.time()
    
    while time.time() - start_time < duration:
        char = random.choice(symbols)
        sys.stdout.write(f'\rSpinning: {char}')
        sys.stdout.flush()
        time.sleep(0.05) 
        
    if random.random() < 0.1:
        final_number = 45
        print(f"\n{BOLD}{RED}!!! BEAST MODE !!!{RESET}")
    else:
        final_number = random.randint(3, 8)
        
    print(f"\n{BOLD}Your word has {final_number} characters!{RESET}")
    return final_number

def play_hangman(word_length):
    secret_word = random.choice(WORD_BANK[word_length]).lower()
    guessed_letters = []
    attempts = 15 if word_length == 45 else 8
    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {GREEN}{display_word}{RESET}")
        print(f"Attempts left: {RED}{attempts}{RESET}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")
        
        if "_" not in display_word:
            typing_print(f"{BOLD}{GREEN}CONGRATULATIONS! You found the word: \n{secret_word.upper()}!{RESET}")
            return True

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'!")
            continue
            
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"{GREEN}Yes!{RESET} '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"{RED}Nope!{RESET} '{guess}' is not there.")

    typing_print(f"{RED}GAME OVER!{RESET} The word was: {BOLD}{secret_word.upper()}{RESET}")
    return False

def main():
    while True:
        typing_print("Welcome to the "+RED+ "Word Wheel!" +RESET, delay=0.03)
        time.sleep(0.5)
        typing_print("The wheel determines the length of your secret word!", delay=0.03)
        time.sleep(0.3)
        typing_print("Ready...", delay=0.03)
        time.sleep(0.3)
        typing_print("Steady...", delay=0.03)
        time.sleep(0.3)
        typing_print(BOLD+CYAN+"SPIN!!!"+RESET, delay=0.02)
        
        length = spin_animation()
        play_hangman(length)
        
        print("\n" + "-"*30)
        again = input(f"{BOLD}Would you like to play again? (y/n): {RESET}").lower()
        if again != 'y':
            typing_print("Thanks for playing! Goodbye!", delay=0.05)
            break
        print("\n" * 2) 

if __name__ == '__main__':
    main()