secret = 28
count = 0

print("Welcome to the guessing game. You have infinite number of guesses to guess the secret number")

option = input("Press '1' to play and press '0' to exit. ENTER: ").strip()

while option != "1" and option!= "0":
    print("invalid")
    option = input("Press '1' to play and press '0' to exit. ENTER: ").strip()

if option == "0":
    print("GOODBYE :<")
    exit()

if option == "1":
    print("Clue: the secret number is within 0 to 50")
    print("GOOD LUCK")
    print() #Add blank line for better visibility

while option == "1":
    while True:
        try:
            guess = int(input("Guess a number: "))
            count = count + 1
            break
        except ValueError:
            print("invalid")

    if guess == secret:
        print("Congrats! You guessed the secret number in", count, "guesses.")
        break

#Checking if the guess is within 5 numbers of the secret. abs accounts for both +ve and -ve 
    elif abs(secret - guess) <= 5:
         print("Your guess is within 5 of the secret number")
    
    elif guess > secret:
        print("Too high")

#Last condition should be else not elif
    else:
        print("Too low")
