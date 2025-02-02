from random import randint

random_number = randint(1, 20)
name = str(input("Hello! What is your name? \n"))
print("Well,",name+",","I am thinking of a number between 1 and 20.")

def game(): 
    count = 0
    while True:
        guessnum = int(input("Take a guess. \n"))
        if guessnum == random_number:
            count +=1
            print("Good job,",name+"!","You guessed my number in",count,"guesses!")
            break
        elif guessnum < random_number:
            print("Your guess is too low.")
            count += 1
        elif guessnum > random_number:
            print("Your guess is too high.")
            count += 1

game()
