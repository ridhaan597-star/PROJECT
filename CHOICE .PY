print("Choose your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Choose a Bike:")
    print("1. Scooty")
    print("2. Scooter")
    choice2 = int(input("Enter your bike choice: "))

    if choice2 == 1:
        print("You have selected Scooty")
    elif choice2 == 2:
        print("You have selected Scooter")
    else:
        print("Wrong choice!")  # Catch invalid bike input

elif choice == 2:
    print("Choose a Car:")
    print("1. Sedan")
    print("2. XUV")
    choice3 = int(input("Enter your car choice: "))

    if choice3 == 1:
        print("You have selected Sedan")
    elif choice3 == 2:
        print("You have selected XUV")
    else:
        print("Wrong choice!")  # Catch invalid car input

else:
    print("Wrong choice! Please enter 1 or 2.")