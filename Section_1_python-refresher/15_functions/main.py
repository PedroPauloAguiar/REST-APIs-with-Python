def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


user_age_in_seconds()


friends = []


def add_friend():
    friends.append("Rolf")


add_friend()
print(friends)
