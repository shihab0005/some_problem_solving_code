import random
number = []
count = 0

def random_number():
    for i in range(4):
        x = random.randrange(0, 5)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        random_number()


def play_game():
    global count
    count += 1
    cows = 0
    bulls = 0
    choice = input("Please Enter a 4 digit number :")
    guess = []
    for i in range(4):
        guess.append(int(choice[i]))
    for j in range(4):
        if guess[j] == number[j]:
            bulls += 1
        else:
            cows += 1
    print("Bulls :", bulls)
    print("Cows :", cows)
    if (bulls == 4):
        print(f"You win after {count} times")
    else:
        play_game()

random_number()
play_game()


