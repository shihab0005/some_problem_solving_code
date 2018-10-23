

import random
winning_number =random.randint(1,100)
guess = 1
number = int(input("Guess A Number Between 1 to 100 :"))
game_over = False
while not game_over:
    if number == winning_number:
        print(f" You Win !! And You Guessed {guess} times")
        game_over = True
    else:
        if number > winning_number:
            print(" Too High !!")
        else:
            print(" Too Low !!")

        guess += 1
        number = int(input("Guess Again : "))
