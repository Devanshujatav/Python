import random
from enum import nonmember


def number_guessing_game():
    print("="*40)
    print("        NUMBER GUESSING GAME")
    print("="*40)

    # difficulty settings
    difficulties = {
        "1" : ("easy" , 1 , 50 , 8),
        "2" : ("medium" , 1 , 100 , 10),
        "3" : ("hard" , 1 , 200 , 12),
    }


    print("\nChoose difficulty:")
    print("  1. Easy   (1 – 50,  8 attempts)")
    print("  2. Medium (1 – 100, 10 attempts)")
    print("  3. Hard   (1 – 200, 12 attempts)")

    while True:
        choice = input("\n Enter 1 / 2 / 3 : ").strip()
        if choice in difficulties:
            label , low , high , max_attempts = difficulties[choice]
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    secret = random.randint(low , high)
    attempts = 0
    best_score = None

    print(f"\n[{label}] Guess a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts

        try:
            guess = int(input(f"\n Attempt {attempts+1} / {max_attempts} ->"))
        except ValueError:
            print("  Please enter a valid integer.")
            continue

        if guess < low or guess > high:
            print(f"  Out of range! Enter a number between {low} and {high}.")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n  Correct! The number was {secret}.")
            print(f" Solved in {attempts} guess{'es' if attempts > 1 else '' }!")

            if best_score is None or attempts < best_score:
                best_score = attempts

            break

        elif guess < secret:
            print(f"  Too low!  ({remaining - 1} guess{'es' if remaining - 1 != 1 else ''} left)")
        else:
            print(f"  Too high!  ({remaining - 1} guess{'es' if remaining - 1 != 1 else ''} left)")

    else:
        print(f"\n  Out of guesses! The number was {secret}. Better luck next time!")

    # Play Again
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        number_guessing_game()
    else:
        if best_score:
            print(f"\nThanks for playing! Your best score: {best_score} guess{'es' if best_score > 1 else ''}.")
        else:
            print("\nThanks for playing!")

if __name__ == "__main__":
    number_guessing_game()