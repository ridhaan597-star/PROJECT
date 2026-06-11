temperature = float(input("Enter the current temperature in Celsius: "))

if temperature < 20:
    print("It's cold! Wear warm clothes.")
elif temperature > 35:
    print("It's really warm! Wear light clothes.")
else:
    print("It's mild. A moderate layer should be fine.")