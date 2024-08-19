import random

# List of words to choose from
words = ["hangman", "programming", "openai", "developer", "code", "algorithm", "function", "variable", "loop","Python", "Giraffe", "Tropical", "Umbrella",
    "Diamond", "Oxygen", "Library", "Picture", "Computer",
    "Elephant", "Mountain", "Sandbox", "Rainbow", "Adventure",
    "Treasure", "Keyboard", "Guitar", "Cyclone", "Mystery",
    "Galaxy", "Volcano", "Jigsaw", "Cryptic", "Astronaut", "Butterfly", "Courage", "Dolphin", "Eclipse",
    "Forest", "Horizon", "Island", "Journey", "Whisper", "Samsung", "automation", "Calculator", "iphone", "Windows", "Science", "Elements", "Physics", "Chemistry", "Biology", "Mathematics", "Organism", "Google", "Engine", "Search"]

def choose_word(words):
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 20
    
    print("Welcome to Hangman!")
    print("Guess the word,")
    print("one letter at a time!")
    print("You have "+str(max_incorrect_guesses)+" tries!")
    
    while True:
        print(display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've guessed '"+guess+"'")
            print("Try a different letter")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess! '"+guess+"'")
            print("is in the word!")
        else:
            incorrect_guesses += 1
            left = max_incorrect_guesses - incorrect_guesses
            print("Sorry, '"+guess+"' is not")
            print("in the word")
            print("You have "+str(left)+" attempts.")

        if all(letter in guessed_letters for letter in word):
            print("You've guessed the word!")
            print(word)
            break

        if incorrect_guesses >= max_incorrect_guesses:
            print("You've run out of attempts.")
            print("The word was")
            print(word)
            print("Better luck next time!")
            break

hangman()
