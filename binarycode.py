print("Decimal to Binary Converter")

num = float(input("Enter a decimal number: "))

if num == 0:
    print("Binary equivalent is 0")
else:
    binary = ""

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    print("Binary equivalent is", binary)