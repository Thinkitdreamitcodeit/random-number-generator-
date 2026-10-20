import random

def play_game():
    print("🤖 Welcome to the Ultimate Number Guessing Game! 🤖")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\n👉 Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("⚠️ Please pick a number strictly between 1 and 100!")
                continue
                
            if guess < number_to_guess:
                print("📈 Too low! Try a higher number.")
            elif guess > number_to_guess:
                print("📉 Too high! Try a lower number.")
            else:
                print(f"🎉 Boom! You got it in {attempts} attempts! Great job! 🚀")
                break
                
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    play_game()
