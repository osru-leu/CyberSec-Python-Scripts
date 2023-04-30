import random


guess_count = 0
#my_num = 7
num_of_guesses = int(input(" Lets play a guessing game. How many guesses would you like? "))
top_num = int(input(f"Pick a number greater than 3: "))
comp_choice = random.randint(1, top_num)


while guess_count != num_of_guesses:
    
    guess_count += 1
    guess = int(input(f"Pick a number between 1 and {top_num}. \n You have {num_of_guesses} chances to guess the number: "))
    if guess == comp_choice:
        print('You guessed it!')
        break
    elif guess < comp_choice:
        print('Higher')
    elif guess > comp_choice:
        print('Lower')
    else:
        print('Out of guesses!!!!')
