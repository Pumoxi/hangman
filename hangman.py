import random
def generate_word():

    # word list of 10 fruits and vegetables

    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "apricot", "avocado", "blueberry", "coconut", "dragonfruit", "elderberry", "guava", "honeydew", "jackfruit", "kiwano", "lime", "lychee", "mango", "nectarine", "olive", "papaya", "passionfruit", "quince", "raspberry", "starfruit", "tangerine", "watermelon", "ximenia", "yuzu", "zucchini"]
    word = random.choice(word_list)

    return word

def generate_blank(word):

    blank = []

    for letter in word:
        blank.append("_")

    return blank

def generate_hangman(lives):

    hangman = [
        r"""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        r"""
        +---+
        |   |
            |
            |
            |
            |
        =========
        """
    ]

    return hangman[lives]

def ask_guess():

    guess = input("Guess a letter for fruit and vegetable: ").lower()

    return guess

def validate_guess(guess, word):

    if guess in word:
        return True
    else:
        return False
    
def if_true(guess, word, blank):

    for i in range(len(word)):
        if word[i] == guess:
            blank[i] = guess

    return blank

def if_false(guess, lives):

    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1

    return lives

def win_or_lose (blank, lives):

    if "_" not in blank:
        print("You win!")
        return True
    elif lives == 0:
        print("You lose!")
        return True
    else:
        return False
    
def main():

    word = generate_word()
    blank = generate_blank(word)
    lives = 7
    guess_list = []

    while True:

        print(" ".join(blank))
        print(f"You have {lives} lives left.")
        print("")
        guess = ask_guess()
        print("")

        if guess in guess_list:
            print(f"You have already guessed {guess}.")
        else:
            guess_list.append(guess)
            
            if validate_guess(guess, word):
                blank = if_true(guess, word, blank)
            else:
                lives = if_false(guess, lives)
                hangman = generate_hangman(lives)
                print (hangman)

        print("")

        if win_or_lose(blank, lives):
            print(f"The word was {word}.")
            break

if __name__ == "__main__":
    main()