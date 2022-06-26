# To make a random guess we use the module called RANDOM

import random
# Here we take number that they are going to guess between and we will store it in a variable.

top_of_range = input("Type a number: ")

# Now we will check wheather the number entered is digit or not to do that we will use .isdigit()

if top_of_range.isdigit():
    top_of_range = int(top_of_range) # int is used to convert the other form of data to int type
    if top_of_range <= 0: # here we will check the number entered is greater than 0.
        print("Please enter the number greater than 0.")
        quit()
else:
    print("Please type a number next time")
    quit()

# Now we will generate a ramdom number

random_number = random.randrange(0,top_of_range)
guesses = 0

# Now we will use an loop to generate random number 

while True:
    guesses+=1 # we will add every time with one if the guess is wrong 
    user_guess = input("Make a guess: ") #asking for a guess
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue                                

    if user_guess == random_number:   # here if the guess is equal to randon number we will stop the loop otherwise it will continue 
        print("You got it!!")
        break
    elif user_guess > random_number:
        print("Your guess is above the Number")
    else:
        print("Your guess is below the Number")

print("You got it in",guesses,"gusses!")  # finally we will print the number of gusses did the player took to gusses the number
    

    
   
