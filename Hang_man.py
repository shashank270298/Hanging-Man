import random

# LIST OF WORDS
word_list =['computer',
            'programming',
            'python',
            'networking',
            'database',
            'skills',
            'coding',
            'processing',
            'participation',
            'pateince',
            'motivated',
            'curious',
            'intelligence',
            'knowledge',
            'technical',
            'thinking',
            'optimal',
            'communication'
            'certificate',
            'official',
            'calm',
            'action',
            'rctangle',
            'square',
            'circle',
            'cube',
            'cylinder',
            'cone',
            'celebration',
            'India,'
            'counting',
            'comedy',
            'rainy',
            'sunny',
            'winter',
            'autmun',
            'bus',
            'train',
            'airplane',
            'truck',
            'car',
            'bicycle',
            'tricycle',
            'hangeman',
            'tea',
            'coffee',
            'waffers',
            'drinks',
            'story',
            'tree',
            'river',
            'books',
            'woods',
            'forests',
            'mountains',
            'hills',
            'valley',
            'institute',
            'science',
            'mathematics',
            'school',
            'bag',
            'bridge',
            'swimming',
            'swing',
            'playful',
            'powerful',
            'fearful',
            'joyful',
            'painful',
            'chair',
            'table',
            'door',
            'window',
            'bottle',
            'speaker',
            'sweater',
            'red',
            'yellow',
            'blue',
            'orange',
            'green']

# RANDOMLY SELECTING WORDS FROM THE LIST
def get_word():
    word = random.choice(word_list)
    return word.upper()

# DEFINING THE FUNCTION PLAY FOR MATCHING THE WORDS
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the correct word! You won!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Better luck next time!")


def display_hangman(tries):
    stages = [  # final state: full body
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, body, both arms, one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, body, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

# MAIN FUNCTION 
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main() 