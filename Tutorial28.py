# EXERCISE 3 - GUESS A NUMBER

actual = 45
attempt = 0

while True :
    attempt += 1
    guess = int(input("guess the number : \n "))
    if guess > actual :
        print("your guess is too high")
    elif guess < actual:
        print("your guess is too low")
    else :
        print(f"you guessed the number in {attempt} attempt")
        break

print("thanks for playing")



