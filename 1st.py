import random

# This is a basic Python progr

# def lucky_numer(name):
#     number = len(name) * 9 
#     print("Hello", name, "your lucky number is", str(number))

# lucky_numer("John")
# lucky_numer("Alice")

def number_guessing_game():
        secret_number = 90
        print("I have chosen a number between 1 and 100. Can you guess it?")
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You guessed the number.")
                    break
            except ValueError:
                print("Please enter a valid number.")

number_guessing_game()