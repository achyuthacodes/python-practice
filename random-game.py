# Program
import random 

def rand_num():
    random_number = random.randint(1,100)
    user_number = int(input("Guess the Number : "))
    while random_number != user_number:
        # print("Your guess is wrong Try again!")
        user_number = int(input("Guess the Number Again : "))
        
        if user_number > random_number:
            print("You are above the line")
        elif user_number < random_number:
            print("You are below the line")

        
    print("You are absolutely right!")

rand_num()


                