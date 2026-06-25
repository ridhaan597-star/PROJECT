import random
playing = True
number = str(random.randint(0,9))
while playing:
    guess = input("give me your best shot! \n")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break
    else:
        print("our guess isn't quite right, try again. \n")