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


def analyze_face(face_description):
    emotions = ["happy", "sad", "angry", "surprised", "neutral"]
    print("Analyzing face...")
    if face_description.lower() in emotions:
        print(f"The face shows a {face_description} emotion.")
    else:
        print("Unable to determine the emotion from the description.")

# Example usage:
analyze_face("happy")
analyze_face("confused")