import random
guess_number=random.randint(1,100)
print("Welcome to the guessing game")
#print(f"guess num is {guess_number}") prints the number generated by the guess number
count=0
prev_guess=[0]
while True:
    user_guess = int(input("Enter your guessing number:"))
    if user_guess < 1 or user_guess > 100:
        print("out of bound")
    elif user_guess == guess_number:
        print("correct guess!!You have won the game!")
        break
    elif user_guess > guess_number:
        if user_guess - guess_number < 10:
            if count>0 and prev_guess[0]>user_guess:
                print("warmer")
            else:
                print("warm")
        else:
            if count > 0 and prev_guess[0] < user_guess:
                print("colder")
            else:
                print("cold")
    elif guess_number > user_guess:
        if guess_number - user_guess < 10:
            if count>0 and prev_guess[0]<user_guess:
                print("warmer")
            else:
                print("warm")
        else:
            if count > 0 and prev_guess[0] > user_guess:
                print("colder")
            else:
                print("cold")

    prev_guess.insert(0,user_guess)
    count+=1
    print(f"number of guesses:{count} ")