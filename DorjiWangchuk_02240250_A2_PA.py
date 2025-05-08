import random

# ----- Game 1: Number Guessing -----
def play_number_guess():
    target = random.randint(1, 100)
    print("\nGuess a number from 1 to 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print("Nice! You got it!")
                break
        except ValueError:
            print("Please enter a valid number.")

# ----- Game 2: Rock, Paper, Scissors -----
def play_rps():
    options = ["rock", "paper", "scissors"]
    player = input("Choose rock, paper, or scissors: ").strip().lower()
    if player not in options:
        print("That's not a valid choice.")
        return
    computer = random.choice(options)
    print(f"Computer picked: {computer}")
    if player == computer:
        print("Draw!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

# ----- Game 3: Simple Quiz Game -----
def play_quiz():
    questions = [
        {"q": "What color is the sky?", "choices": ["Blue", "Green", "Yellow", "Red"], "correct": "Blue"},
        {"q": "10 + 5 equals?", "choices": ["15", "12", "20", "10"], "correct": "15"},
        {"q": "Which animal barks?", "choices": ["Cat", "Dog", "Bird", "Fish"], "correct": "Dog"}
    ]
    score = 0
    for q in questions:
        print("\n" + q["q"])
        for i, choice in enumerate(q["choices"], start=1):
            print(f"{i}. {choice}")
        try:
            answer = int(input("Pick 1-4: "))
            if q["choices"][answer - 1] == q["correct"]:
                print("Correct!")
                score += 1
            else:
                print(f"Oops! It's {q['correct']}.")
        except (ValueError, IndexError):
            print("Invalid input.")
    print(f"\nFinal Score: {score} / {len(questions)}")

# ----- Game 4: Pokémon Card Collection -----
pokemon_deck = []

def add_card():
    name = input("Pokémon Name: ")
    card_type = input("Type: ")
    hp = input("HP: ")
    pokemon_deck.append({"Name": name, "Type": card_type, "HP": hp})
    print("Card added successfully.")

def show_cards():
    if not pokemon_deck:
        print("No cards yet.")
    else:
        print("\nYour Pokémon Cards:")
        for card in pokemon_deck:
            print(f"Name: {card['Name']}, Type: {card['Type']}, HP: {card['HP']}")

def manage_cards():
    while True:
        print("\nPokémon Card Manager")
        print("1. Add New Card")
        print("2. View Cards")
        print("3. Go Back")
        option = input("Pick an option (1-3): ")
        if option == "1":
            add_card()
        elif option == "2":
            show_cards()
        elif option == "3":
            break
        else:
            print("Invalid option.")

# ----- Main Menu -----
def main_menu():
    while True:
        print("\n--- Game Menu ---")
        print("1. Play Number Guess")
        print("2. Rock, Paper, Scissors")
        print("3. Trivia Quiz")
        print("4. Pokémon Card Manager")
        print("5. Quit")
        user_choice = input("Choose 1-5: ")

        if user_choice == "1":
            play_number_guess()
        elif user_choice == "2":
            play_rps()
        elif user_choice == "3":
            play_quiz()
        elif user_choice == "4":
            manage_cards()
        elif user_choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("That’s not a valid choice.")

# Start the program
main_menu()
