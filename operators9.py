print("ASCII Value Checker")
print("=" * 40)

a = input("Enter a single character: ").strip()

if len(a) == 1:
    b = ord(a)

    print(f"\nCharacter: '{a}'")
    print(f"ASCII Value: {b}")

    print("Character Type:", end=" ")

    if 65 <= b <= 90:
        print("Uppercase Letter")

    elif 97 <= b <= 122:
        print("Lowercase Letter")

    elif 48 <= b <= 57:
        print("Digit")

    elif b == 32:
        print("Space")

    else:
        print("Special Character")

else:
    print("Error: Please enter exactly ONE character!")