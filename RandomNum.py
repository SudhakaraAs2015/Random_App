import random

top_of_range = input("Please Enter Number")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please Enter number more than 0 next time")
        quit()
else:
    print("Please Enter Number next time")
    quit()
random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses+= 1
    user_guess = input("Make a Guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter number next time")
        continue
    if user_guess==random_number:
        print("You have got it")
        break
    elif user_guess>random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print(f"You have got in {guesses} guesses")