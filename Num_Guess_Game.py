import random

# ---------------- SELECT DIFFICULTY ----------------

def select_difficulty():

    print()
    print("Select Difficulty Level")
    print("1. Basic")
    print("2. Medium")
    print("3. Hard")
    print()

    level = 0

    while level not in [1, 2, 3]:

        level = int(input("Enter your choice: "))

        if level == 1:

            print()
            print("## Guess The Number Between 1 to 10 in 5 Attempts ##")

            num = random.randint(1, 10)
            max_attempt = 5
            score = 100
            wrong = 20

        elif level == 2:

            print()
            print("## Guess The Number Between 1 to 100 in 7 Attempts ##")

            num = random.randint(1, 100)
            max_attempt = 7
            score = 200
            wrong = 25

        elif level == 3:

            print()
            print("## Guess The Number Between 1 to 1000 in 10 Attempts ##")

            num = random.randint(1, 1000)
            max_attempt = 10
            score = 300
            wrong = 30

        else:
            print("Please choose correct option!")

    return num, max_attempt, score, wrong


# ---------------- PLAY GAME ----------------

def play_game(num, max_attempt, score, wrong):

    attempt = 0
    won = False

    for i in range(max_attempt):

        print()

        guess = int(input("Enter the guess number: "))

        attempt = attempt + 1

        print("Remaining attempts:", max_attempt - attempt)

        if guess == num:

            print()
            print("Congratulations..! 🎉")
            print("You guessed the correct number:", num)
            print("Attempts:", attempt)

            won = True

            break

        else:

            score = max(0, score - wrong)

            if guess < num:
                print("Too Low...!")

            else:
                print("Too High...!")

    return score, won, attempt


# ---------------- MAIN PROGRAM ----------------

print()
print("1. Start")
print("2. Exit")

p = int(input("Enter your choice: "))

high_score = 0


while p != 2:

    # Select difficulty
    num, max_attempt, score, wrong = select_difficulty()

    # Play game
    score, won, attempt = play_game(num,max_attempt,score,wrong)
    # Update High Score
    if won and score > high_score:
        high_score = score
    # ---------------- RESULT ----------------
    if not won:
        print()
        print("Game Over..!")
        print("You reached the maximum attempts.")
        print("The correct number is:", num)
    else:
        print()
        print("Score:", score)
        print("High Score:", high_score)
    # ---------------- PLAY AGAIN ----------------
    print()
    print("Do you want to play again?")
    print("1. Yes")
    print("2. No")
    p = int(input("Enter your choice: "))

print()
print("## Game Closed ##")