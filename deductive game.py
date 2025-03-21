import random

def guess_the_number_game():
    rand_num = str(random.randint(100, 999))
    attempts = 10  

    print("Welcome to the Guessing Game!")
    print("You have 10 attempts to guess the secret 3-digit number.")

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}: Guess a 3-digit number: ")

        if len(guess) != 3 or not guess.isdigit():
            print("Invalid input. Please enter a 3-digit number.")
            continue

        result = []
        for i, digit in enumerate(guess):
            if digit == rand_num[i]:
                result.append("👌")  
            elif digit in rand_num:
                result.append("👍")  
            else:
                result.append("❌")  

        print(" ".join(result))

        if guess == rand_num:
            print("🎉 You Got It! The secret number is:", rand_num)
            break
    else:
        print("Game Over! The secret number was:", rand_num)

guess_the_number_game()
