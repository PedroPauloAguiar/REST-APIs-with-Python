number = 7

# While loop
while True:
    user_input = input("Would you like to play ? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

# For loop

friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend}is my friend")
