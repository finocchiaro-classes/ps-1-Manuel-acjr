
def heart_rate(age, goal):
    max_HR = 220 - age
    print(f"Your maximum heart rate is: {max_HR}")

    if goal == "S":
        low = max_HR * 0.8
        high = max_HR * 1.0
    elif goal == "E":
        low = max_HR * 0.6
        high = max_HR * 0.8
    else:
        print("Invalid goal. Please enter 'S' or 'E'.")
        return

    print(f"Your target heart rate is between {low} and {high}")


user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")


heart_rate(user_age, user_goal)

